import subprocess
import os
import random

folder_path = "../../target"
extracted_path = "../../extracted_frames"
target_base_path = "../../resized"
output_base_path = "../../output"

crop_videos_to_4_3(folder_path, target_base_path)
extract_first_frames(target_base_path, extracted_path)

names = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for name in names:
    job_name = f"job_{name}"
    target_path = f"{target_base_path}/{name}.mp4"
    output_path = f"{output_base_path}/output_job_{name}.mp4"

    possible_names = [n for n in names if n != name]
    random_name = random.choice(possible_names)
    source_path = f"{extracted_path}/{random_name}.jpg"

    print(f"Creating job: {job_name}")
    print(f"Source Path:: {source_path}")
    try:
        subprocess.run(["python", "facefusion.py", "job-create", job_name], check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Failed to create job: {job_name}")
        continue

    print(f"Adding step to job: {job_name}, with source: {source_path}, target: {target_path}, output: {output_path}")

    try:
        subprocess.run([
            "python", "facefusion.py", "job-add-step", job_name,
            "-s", source_path,
            "-t", target_path,
            "-o", output_path
        ], check=True)
        print("\n")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to add step to job: {job_name}")
        print("\n")
        continue    

print("Submitting all jobs...")
subprocess.run(["python", "facefusion.py", "job-submit-all"], check=True)

print("Running all jobs...")
subprocess.run(["python", "facefusion.py", "job-run-all"], check=True)

print("All jobs completed.")
