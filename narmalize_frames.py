import cv2
import numpy as np
import os

# Specify the path to the input video file
video_path = '1.MP4'

# Specify the folder to save the normalized frames
output_folder = 'output_1'

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
        # Normalize the frame to the range [0, 1]
        normalized_frame = frame.astype(np.float32) / 255.0
        
        # Convert the frame back to uint8 for saving as an image
        # For downstream tasks such as neural network input, you might not need to convert back to uint8
        normalized_frame_uint8 = (normalized_frame * 255).astype(np.uint8)
        
        # Save the normalized frame as an image
        output_file_path = os.path.join(output_folder, f'normalized_frame_{extracted_frame_count}.jpg')
        cv2.imwrite(output_file_path, normalized_frame_uint8)
        
        # Increment the extracted frame count
        extracted_frame_count += 1
    
    # Increment the frame number
    frame_number += 1

# Release the video capture object
video_capture.release()
