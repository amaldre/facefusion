import cv2
import os
from pathlib import Path

def extract_first_frames(input_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)
    
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.m4v'}
    
    input_path = Path(input_dir)
    video_files = [f for f in input_path.iterdir() 
                   if f.is_file() and f.suffix.lower() in video_extensions]
    
    print(f"Found {len(video_files)} video files")
    
    for video_file in video_files:
        try:
            cap = cv2.VideoCapture(str(video_file))
            
            if not cap.isOpened():
                print(f"Error: Could not open video {video_file.name}")
                continue
            
            ret, frame = cap.read()
            
            if ret:
                output_filename = f"{video_file.stem}.jpg"
                output_path = os.path.join(output_dir, output_filename)
                cv2.imwrite(output_path, frame)
                print(f"Extracted first frame from {video_file.name} -> {output_filename}")
            else:
                print(f"Error: Could not read first frame from {video_file.name}")
            
            cap.release()
            
        except Exception as e:
            print(f"Error processing {video_file.name}: {str(e)}")
    
    print(f"Frame extraction completed. Frames saved to: {output_dir}")

if __name__ == "__main__":
    video_directory = os.path.expanduser("../../resized")
    extract_path = os.path.expanduser("../../extracted_frames")
    
    if os.path.exists(video_directory):
        extract_first_frames(video_directory, extract_path)
    else:
        print("Directory not found!")
