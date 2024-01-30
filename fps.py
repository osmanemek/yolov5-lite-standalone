import cv2

def getframes(path,ip):
    sourcecap = cv2.VideoCapture(path)
    frame_count = int(sourcecap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(sourcecap.get(cv2.CAP_PROP_FPS))

    print ("result:",ip,frame_count,fps)

getframes('rtsp://admin:e6500e126cd3f9c206b56c22f65d2ce2d166d282@192.168.31.164:88/videoMain','164_main')
getframes('rtsp://admin:e6500e126cd3f9c206b56c22f65d2ce2d166d282@192.168.31.164:88/videoSub','164_sub')

getframes('rtsp://admin:49c82606c26f775fa304665aafacb95a6655103f@192.168.31.235:88/videoMain','235_main')
getframes('rtsp://admin:49c82606c26f775fa304665aafacb95a6655103f@192.168.31.235:88/videoSub','235_sub')

getframes('rtsp://admin:77836c8c77ea34a62c3fbd63e0b488f6d9670e15@192.168.31.144:88/videoMain','144_main')
getframes('rtsp://admin:77836c8c77ea34a62c3fbd63e0b488f6d9670e15@192.168.31.144:88/videoSub','144_sub')

"""
result: 164_main    -2570587947308599       25
result: 164_sub     -4611686018427387904    45000

result: 235_main    -4611686018427387904    45000
result: 235_sub     -4611686018427387904    45000

result: 144_main    -2562047788015215       25
result: 144_sub     -1127301026726695       11
"""