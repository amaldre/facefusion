# FaceFusion

This repository a fork of [FaceFusion](https://github.com/facefusion/facefusion).

> 🔗 Original project: [https://github.com/facefusion/facefusion](https://github.com/facefusion/facefusion)

The idea of this fork is to be able to create jobs and face swaps based on only videos from a specified folder

---

# Changes applied

## Video size

Created a file to resize the video to a format accepted by FaceFusion : `resize_video.py`

---

## Frame extraction

Created a file to extract the first frame for a video : `extract_frames.py`

---

## Job pipeline

Created a file to perform a job pipeline : `job_creation.py`

- Perform a swap with a random first frame for a video
- Apply face and frame enhancement
- Do this for all files from the folder
