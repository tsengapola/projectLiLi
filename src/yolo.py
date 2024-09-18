from ultralytics import YOLO
import cv2
import math 
import time
import subprocess
import os

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

person_time = time.time()
spoon_time = time.time()
eat_time = time.time()
fsm = "screen_on"
person_center = [0,0]
spoon_center = [0,0]

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])
            if(classNames[cls]=="person"):
                person_time = time.time()
                person_center[0] = (x1+x2)/2
                person_center[1] = (y1+y2)/2
            if(classNames[cls]=="spoon"):
                spoon_time = time.time()
                spoon_center[0] = (x1+x2)/2
                spoon_center[1] = (y1+y2)/2
                
            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
    	
        dx = person_center[0] - spoon_center[0]
        dy = person_center[1] - spoon_center[1]
        if(math.sqrt(dx*dx + dy*dy)<300):
            eat_time = time.time()
    	    
    if(fsm=="screen_on" and time.time() - eat_time > 10.0):
        turn_off_keyboard_cmd = "xinput --disable " + str(os.environ['keyboard_id'])
        keyboard_status = subprocess.check_output(turn_off_keyboard_cmd, shell=True)
        monitor_status = subprocess.check_output("xset -display $DISPLAY dpms force off", shell=True)
        fsm = "screen_off"
    elif(fsm == "screen_off"):
        if(time.time() - eat_time < 0.2):
            monitor_status = subprocess.check_output("xset -display $DISPLAY dpms force on", shell=True)
            turn_on_keyboard_cmd = "xinput --enable " + str(os.environ['keyboard_id'])
            keyboard_status = subprocess.check_output(turn_on_keyboard_cmd, shell=True)
            fsm = "screen_on"
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break
        
turn_on_keyboard_cmd = "xinput --enable " + str(os.environ['keyboard_id'])
keyboard_status = subprocess.check_output(turn_on_keyboard_cmd, shell=True)
cap.release()
cv2.destroyAllWindows()
