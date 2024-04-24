import cv2
import os

# Specify the path to the input video file
video_path = '1.MP4'

# Specify the folder to save the converted frames
output_folder_rgb = 'output_rgb'
output_folder_gray = 'output_gray'

# Create the output folders if they don't exist
os.makedirs(output_folder_rgb, exist_ok=True)
os.makedirs(output_folder_gray, exist_ok=True)

# Load the video file using OpenCV
video_capture = cv2.VideoCapture(video_path)

# Set the frame extraction rate (e.g., extract every nth frame)
frame_extraction_rate = 10  # Change this value as needed

frame_number = 0
extracted_frame_count = 0

# Iterate through the video frames
while True:
    # Read the next frame from the video
    ret, frame = video_capture.read()
    
    # Check if the frame was read successfully
    if not ret:
        # End of video or an error occurred
        break

    # Extract frames based on the frame extraction rate
    if frame_number % frame_extraction_rate == 0:
        # Convert the frame from BGR to RGB color space
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Convert the frame to grayscale color space
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Save the RGB frame as an image
        output_file_path_rgb = os.path.join(output_folder_rgb, f'rgb_frame_{extracted_frame_count}.jpg')
        cv2.imwrite(output_file_path_rgb, frame_rgb)
        
        # Save the grayscale frame as an image
        output_file_path_gray = os.path.join(output_folder_gray, f'gray_frame_{extracted_frame_count}.jpg')
        cv2.imwrite(output_file_path_gray, frame_gray)
        
        # Increment the extracted frame count
        extracted_frame_count += 1
    
    # Increment the frame number
    frame_number += 1

# Release the video capture object
video_capture.release()
