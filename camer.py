import cv2
import time
from datetime import datetime

cam = cv2.VideoCapture()
cam.open(2)
k=1000
while True:
#for i in range(10*k):
    result, image = cam.read()

    if result:
        now = datetime.now()
        fileName = "image-{}.png".format(now.strftime("%d_%H-%M-%S"))
      
        cv2.imwrite(fileName, image)
        print(f"captured: {fileName}")
    else:
        print("feil")
    time.sleep(10*60)

minutt = 60 #s
time.sleep(10)