import cv2
import os

# Specify the path to the input video file
video_path = '1.MP4'

# Specify the folder to save the resized frames
output_folder = 'output'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the video file using OpenCV
video_capture = cv2.VideoCapture(video_path)

# Set the frame extraction rate (e.g., extract every nth frame)
frame_extraction_rate = 10  # Change this value as needed

# Define the desired width and height for resizing
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
        # Resize the frame to the desired dimensions
        resized_frame = cv2.resize(frame, (desired_width, desired_height))
        
        # Save the resized frame as an image
        output_file_path = os.path.join(output_folder, f'resized_frame_{extracted_frame_count}.jpg')
        cv2.imwrite(output_file_path, resized_frame)
        
        # Increment the extracted frame count
        extracted_frame_count += 1
    
    # Increment the frame number
    frame_number += 1

# Release the video capture object
video_capture.release()
