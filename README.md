---
title: CV Image Search
emoji: 🔍
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 🔍 Computer Vision Powered Image Search Engine

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C.svg)](https://pytorch.org/)
[![Ultralytics](https://img.shields.io/badge/YOLO-v11-yellow.svg)](https://github.com/ultralytics/ultralytics)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)

**Live Demo:** [View on Hugging Face Spaces](https://huggingface.co/spaces/Asadd22/cv-image-search)

An end-to-end Computer Vision Search Engine and MLOps deployment pipeline. This application allows users to semantically search through a dataset of images using Object Detection models. By leveraging **YOLOv11** for feature extraction and a decoupled search architecture, the engine achieves rapid retrieval times with complex boolean search logic.

## ✨ Key Features

* **Intelligent Search Logic:** Filter images using multiple object classes with complex `AND` / `OR` boolean conditions.
* **Granular Thresholds:** Specify exact count limits (e.g., "Find images with *exactly* 2 cars and at least 1 person").
* **Decoupled Architecture:** Heavy GPU-based object detection is performed offline during the "Indexing" phase, allowing the live search engine to run blazing-fast on lightweight CPU servers using generated JSON metadata.
* **Interactive UI:** Built with Streamlit, featuring dynamic CSS grids, custom bounding-box overlays via Pillow, and instant metadata inspection.
* **Automated CI/CD:** Fully automated deployment pipeline using GitHub Actions, automatically syncing code and Git LFS image assets to Hugging Face Docker containers upon every push.

## 🛠️ Technology Stack

* **Machine Learning:** PyTorch, Ultralytics YOLOv11
* **Frontend:** Streamlit, Custom CSS
* **Image Processing:** OpenCV (Headless), PIL (Pillow)
* **MLOps & Deployment:** Docker, GitHub Actions CI/CD, Git LFS, Hugging Face Spaces
* **Data Handling:** JSON, Pathlib

## 🚀 How to Run Locally

If you want to run this application on your own machine to process new images or test the GPU inference, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/Asad22Khan/CV-image_search_engine.git
cd CV-image_search_engine
```


### 2. Set Up the Virtual Environment (Conda Recommended)
It is highly recommended to use a Conda environment to manage PyTorch and CUDA dependencies cleanly.

```bash
conda create -n yolo_image_search python=3.12 -y
conda activate yolo_image_search
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```
The application will automatically open in your default web browser at http://localhost:8501

## 🖥️ Usage Guide

When you launch the application, you have three primary modes of operation:

1. **Test Application (Demo):** The default mode. Instantly loads the pre-indexed COCO-500 dataset so you can immediately test the search functionality without downloading any weights or images.
2. **Process New Images:** Point the engine to a local directory of raw images. The app will download the YOLOv11 weights, run inference across all images, and generate a new `metadata.json` schema. *(Requires GPU for optimal performance).*
3. **Load Existing Metadata:** Manually input the path to a previously generated JSON schema to load a custom dataset.

