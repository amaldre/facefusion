import cv2
import os
from pathlib import Path

def crop_center_4_3(frame):
    h, w, _ = frame.shape
    target_ratio = 4 / 3
    current_ratio = w / h

    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        x1 = (w - new_w) // 2
        frame_cropped = frame[:, x1:x1+new_w]
    else:
        new_h = int(w / target_ratio)
        y1 = (h - new_h) // 2
        frame_cropped = frame[y1:y1+new_h, :]
    return frame_cropped

def crop_videos_to_4_3(input_dir, output_dir):
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
            
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = cap.get(cv2.CAP_PROP_FPS)
            output_filename = f"{video_file.stem}.mp4"
            output_path = os.path.join(output_dir, output_filename)
            
            out = None
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame = crop_center_4_3(frame)
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                
                if out is None:
                    height, width, _ = frame.shape
                    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
                
                out.write(frame)
            
            cap.release()
            if out is not None:
                out.release()
                print(f"Resized video saved to {output_filename}")
            else:
                print(f"Error: No frames processed for {video_file.name}")
        except Exception as e:
            print(f"Error processing {video_file.name}: {str(e)}")
    print(f"Resizing completed. Videos saved to: {output_dir}")

if __name__ == "__main__":
    video_directory = os.path.expanduser("~/Desktop/shareid/target")
    output_directory = os.path.expanduser("~/Desktop/shareid/resized")
    if os.path.exists(video_directory):
        crop_videos_to_4_3(video_directory, output_directory)
    else:
        print("Directory not found")
