from models.experimental import attempt_load
from utils.datasets import LoadStreams
from utils.general import scale_coords, check_img_size, non_max_suppression
import torch.backends.cudnn as cudnn
from utils.torch_utils import select_device
import torch
import time

def detect(source):
    imgsz = 640
    weights = 'weights/v5lite-s.pt'
    # weights = 'weights/v5lite-e.pt'
    # weights = 'weights/v5lite-c.pt'
    model = attempt_load(weights, map_location='cpu')
    stride = int(model.stride.max())
    imgsz = check_img_size(imgsz, s=stride)
    device = select_device('cpu')
    half = device.type != 'cpu'

    cudnn.benchmark = True  # set True to speed up constant image size inference
    dataset = LoadStreams(source, img_size=imgsz, stride=stride)

    names = model.module.names if hasattr(model, 'module') else model.names
    model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))

    findex1 = 0
    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        pred = model(img, augment=False)[0]
        pred = non_max_suppression(pred, conf_thres=0.45, iou_thres=0.5, classes=None, agnostic=False)

        findex2 = 0
        for i, det in enumerate(pred):  # detections per image
            if len(det):
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count

                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                findex3 = 0
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string
                    selectedval = names[int(c)]
                    print(time.strftime("%M:%S", time.localtime()),weights,findex1,findex2,findex3,selectedval)
                    findex3 = findex3 + 1
            findex2 = findex2 + 1
        findex1 = findex1 + 1

if __name__ == '__main__':
    detect('rtsp://example.com/streamName')