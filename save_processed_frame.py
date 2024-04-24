import cv2
import os
import numpy as np

# Specify the path to the input video file
video_path = '1.MP4'

# Specify the folder to save the processed frames
output_folder = 'output_4'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the video file using OpenCV
video_capture = cv2.VideoCapture(video_path)

# Set the frame extraction rate (e.g., extract every nth frame)
frame_extraction_rate = 10  # Change this value as needed

# Set the desired image format and quality settings
image_format = 'jpg'  # Choose 'jpg' or 'png' based on your needs
jpeg_quality = 95  # Quality setting for JPEG (1-100, where 100 is highest quality)

# Define the desired width and height for resizing (optional)
desired_width = 224
desired_height = 224

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
        # Resize the frame to the desired dimensions (optional)
        frame = cv2.resize(frame, (desired_width, desired_height))
        
        # Normalize the frame to the range [0, 1] (optional)
        frame = frame.astype(float) / 255.0
        
        # Convert the frame from BGR to RGB color space
        # First, convert the frame back to uint8 if it is in float format
        frame_uint8 = (frame * 255).astype(np.uint8)
        frame_rgb = cv2.cvtColor(frame_uint8, cv2.COLOR_BGR2RGB)
        
        # Save the processed frame as an image in the specified format and quality
        output_file_path = os.path.join(output_folder, f'processed_frame_{extracted_frame_count}.{image_format}')
        
        # Save the frame according to the chosen image format and quality
        if image_format == 'jpg':
            # Save as JPEG with specified quality
            cv2.imwrite(output_file_path, frame_rgb, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])
        elif image_format == 'png':
            # Save as PNG
            cv2.imwrite(output_file_path, frame_rgb)
        
        # Increment the extracted frame count
        extracted_frame_count += 1
    
    # Increment the frame number
    frame_number += 1

# Release the video capture object
video_capture.release()
