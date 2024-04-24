import cv2
import os

# Specify the path to the input video file
video_path = '1.MP4'

# Specify the folder to save the extracted frames
output_folder = 'path_to_output_folder'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

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
        # Save the current frame as an image
        # Specify the file path for the output image
        output_file_path = os.path.join(output_folder, f'frame_{extracted_frame_count}.jpg')
        
        # Save the frame as a JPEG image
        cv2.imwrite(output_file_path, frame)
        
        # Increment the extracted frame count
        extracted_frame_count += 1
    
    # Increment the frame number
    frame_number += 1

# Release the video capture object
video_capture.release()
