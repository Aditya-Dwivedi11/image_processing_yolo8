# YOLOv8 Image Processing Project

This repository contains a Python-based object detection project using the YOLOv8 deep learning model. It includes source code, sample images, pretrained YOLOv8 weights, and instructions for setup and usage.

---

## 📁 Project Structure

├── start_yolo/ # Scripts and sample images for image detection
│ ├── yolo_1_pr.py # Main detection script on images
│ └── images/ # Sample images for testing
├── yolo-webcam/ # Scripts for real-time webcam detection
│ └── yolo_webcam_pr.py # Webcam detection script
├── yolo-weights/ # Pretrained YOLOv8 model weights (.pt files)
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules (excluding venv, etc.)
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher  
- Git  
- Virtual environment tool (optional but recommended)

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aditya-Dwivedi11/image_processing_yolo8.git
   cd image_processing_yolo8
Create and activate a virtual environment:

On Windows:

bash
Copy code
python -m venv venv
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
🎯 Usage
Run Object Detection on Sample Images
bash
Copy code
python start_yolo/yolo_1_pr.py
The script will process images in start_yolo/images/ and output detection results.

Run Real-time Object Detection from Webcam
bash
Copy code
python yolo-webcam/yolo_webcam_pr.py
⚠️ Notes
The pretrained YOLOv8 weights are located in the yolo-weights/ folder.

Some weight files are large (>50MB). For better version control, consider using Git Large File Storage (LFS).

The venv/ folder is excluded from the repository to keep it clean; recreate it locally using requirements.txt.

🤝 Contribution
Feel free to fork the repository and submit pull requests. Please open issues for bugs or feature requests.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

👤 Author
Aditya Dwivedi
GitHub: @Aditya-Dwivedi11

Thank you for checking out this project!
