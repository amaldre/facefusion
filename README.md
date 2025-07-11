# FaceFusion

This repository a fork of [FaceFusion](https://github.com/facefusion/facefusion).

> 🔗 Original project: [https://github.com/facefusion/facefusion](https://github.com/facefusion/facefusion)

The idea of this fork is to be able to create jobs and face swaps based on only videos from a specified folder

---

# HOW TO RUN IT

## Create the conda env

`conda create --name facefusion python=3.12 pip=25.0`

`conda activate facefusion`

## Install accelerator

### LINUX

`conda install nvidia/label/cuda-12.9.1::cuda-runtime nvidia/label/cudnn-9.10.0::cudnn`

### WINDOWS

`conda install nvidia/label/cuda-12.9.1::cuda-runtime nvidia/label/cudnn-9.10.0::cudnn`

## Clone the repo

`git clone git@github.com:amaldre/facefusion.git`

`cd facefusion`

## Install application

`python install.py --onnxruntime cuda`

## Reload the env

`conda deactivate`

`conda activate facefusion`

## Prepare video folder

Put the video folder under the name `target`, and change the path to all folders to where you want your folder to be in [here](job_creation.py)

## Launch job creation

`python job_creation.py`

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
