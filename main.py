import cv2

video_path = '1.MP4'

video_capture = cv2.VideoCapture(video_path)

if not video_capture.isOpened():
    print("Error. video could not open it.")

while video_capture.isOpened():
    ret, frame = video_capture.read()

    if not ret:
        break

    cv2.imshow('Video Frame', frame)

    cv2.waitKey(1)

video_capture.release()

cv2.destroyAllWindows()