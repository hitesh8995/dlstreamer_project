🚀 DL Streamer Scalability Analysis Project

This repository presents a scalability and performance analysis of Intel® DL Streamer for real-time video analytics.
The project demonstrates how deep learning–based inference pipelines perform when processing video streams using Intel’s optimized AI and media frameworks.

📌 Project Overview

Intel DL Streamer is a video analytics framework built on GStreamer, optimized for running deep learning inference efficiently using Intel® OpenVINO™.

This project focuses on:

Building DL Streamer pipelines

Running inference on video streams

Observing performance and scalability

Generating output videos and reports for analysis

🧠 Key Objectives

✅ Understand DL Streamer pipeline architecture

✅ Analyze scalability with video streams

✅ Evaluate inference performance

✅ Document results with video and reports

🛠️ Technologies Used

Intel® DL Streamer

Intel® OpenVINO™ Toolkit

GStreamer

Python

Deep Learning Models

Linux Environment

📂 Repository Structure

dlstreamer_project/
│
├── models/                     # Deep learning models
├── scripts/                    # Python scripts for pipeline execution
│
├── video.mp4                   # Input video
├── Output.mp4                  # Output video with inference
│
├── DL_Streamer_Report.docx     # Detailed project report
├── Dlstreamer_documentation.docx  # Project documentation
│
└── README.md                   # Project overview

⚙️ Prerequisites

Before running this project, ensure you have:

Linux OS (Ubuntu recommended)

Intel CPU / iGPU (preferred for optimization)

Installed:

Intel® OpenVINO™ Toolkit

Intel® DL Streamer

GStreamer

Python 3.x

🚀 How to Run the Project

Clone the repository

git clone https://github.com/hitesh8995/dlstreamer_project.git


Navigate to the project directory

cd dlstreamer_project


Run the pipeline script

python scripts/<script_name>.py


(Replace <script_name> with the actual script file name)

View the output

Processed video: Output.mp4

Reports: .docx files

📊 Results & Output

🎥 Processed Video Output with AI inference

📄 Detailed Report explaining:

Pipeline design

Performance behavior

Scalability observations

Practical conclusions

The results demonstrate how DL Streamer efficiently handles real-time video inference using optimized Intel hardware acceleration.

📈 Use Cases

Real-time video analytics

Object detection & classification

Edge AI deployments

Smart surveillance systems

Performance benchmarking of AI pipelines

📄 Documentation

DL_Streamer_Report.docx – Complete project analysis

Dlstreamer_documentation.doc – Technical explanation of DL Streamer setup and usage

👤 Author

Hitesh Choudhary
GitHub: https://github.com/hitesh8995

📜 License

This project is intended for educational and research purposes.
Feel free to use and modify it for learning and experimentation.
