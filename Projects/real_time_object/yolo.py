from ultralytics import YOLO
import cv2
import math

cap = cv2.VideoCapture("video/C1073.MP4")
cap.set(3, 640)
cap.set(4, 480)

# model = YOLO("yolov8n.pt")
model = YOLO("best/best.pt")

className = ["needle"]

if(cap.isOpened() == False):
    print("Error! video not open")

# Set desired output size
output_width = 480  # Set your desired width
output_height = 480 # Set your desired height

# Set the desired frame rate
desired_frame_rate = 13  # Change this to your desired frame rate

# Change the frame rate of the video capture
cap.set(cv2.CAP_PROP_FPS, desired_frame_rate)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (output_width, output_height))  # Resize frame
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

            # # class name
            # cls = int(box.cls[0])
            # print("Class name -->", className[cls])
            # Assuming 'needle' is the only class in the list
            print("Class name -->", className[0])            


            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, className[0], org, font, fontScale, color, thickness)


    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



