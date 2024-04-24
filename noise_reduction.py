import cv2
import os

# Specify the path to the input video file
video_path = '1.MP4'

# Specify the folder to save the noise-reduced frames
output_folder = 'output_2'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the video file using OpenCV
video_capture = cv2.VideoCapture(video_path)

# Set the frame extraction rate (e.g., extract every nth frame)
frame_extraction_rate = 10  # Change this value as needed

# Define the kernel size for Gaussian blur and median filtering
gaussian_kernel_size = (5, 5)  # Gaussian blur kernel size
median_kernel_size = 3  # Median filter kernel size

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
        # Apply Gaussian blur to reduce noise
        gaussian_blurred_frame = cv2.GaussianBlur(frame, gaussian_kernel_size, 0)
        
        # Apply median filtering to reduce noise (you can use either Gaussian blur or median filtering)
        median_filtered_frame = cv2.medianBlur(gaussian_blurred_frame, median_kernel_size)
        
        # Save the noise-reduced frame as an image
        output_file_path = os.path.join(output_folder, f'noise_reduced_frame_{extracted_frame_count}.jpg')
        cv2.imwrite(output_file_path, median_filtered_frame)
        
        # Increment the extracted frame count
        extracted_frame_count += 1
    
    # Increment the frame number
    frame_number += 1

# Release the video capture object
video_capture.release()
