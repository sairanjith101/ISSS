import cv2

# Specify the path to the input video file
video_path = '1.MP4'

# Load the video file using OpenCV
video_capture = cv2.VideoCapture(video_path)

# Check if the video file was successfully loaded
if not video_capture.isOpened():
    print("Error: Could not open video file")
else:
    print(f"Video file loaded successfully: {video_path}")

    # Get video properties (optional)
    # For example, you can retrieve the frame width, height, and frame rate
    frame_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_rate = video_capture.get(cv2.CAP_PROP_FPS)

    print(f"Frame width: {frame_width}")
    print(f"Frame height: {frame_height}")
    print(f"Frame rate: {frame_rate}")

# Don't forget to release the video capture object when you're done
# This is important to free up system resources
video_capture.release()
