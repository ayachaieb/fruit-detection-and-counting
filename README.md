Fruit Detection and Counting

Overview

Fruit Detection and Counting is a project that leverages computer vision and deep learning to detect fruits in images or real-time video streams and count them accurately. The project includes a web-based interface to visualize the results and interact with the detection system.

Features

Real-time fruit detection using deep learning models (YOLO, Faster R-CNN, etc.).

Automatic counting of detected fruits in images or video streams.

User-friendly web interface to upload images/videos and view detection results.

Support for multiple fruit types with customizable datasets.

Live camera feed processing for real-time fruit counting.

Technologies Used

Deep Learning Models: YOLO/Faster R-CNN/SSD

Backend: Flask / FastAPI / Django

Frontend: React / Vue.js / HTML, CSS, JavaScript

Computer Vision: OpenCV, TensorFlow / PyTorch

Database (Optional): PostgreSQL / MongoDB (for storing results)

Installation

Prerequisites

Ensure you have the following installed:

Python 3.x

Pip / Conda

Virtual environment (optional but recommended)

Node.js (if using React for frontend)

Steps

Clone the repository:

git clone https://github.com/yourusername/fruit-detection-and-counting.git
cd fruit-detection-and-counting

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the backend server:

python app.py

Run the frontend (if applicable):

cd frontend
npm install
npm start

Access the web interface:
Open a browser and go to http://localhost:3000 (or the configured port).

Usage

Upload an image or video from the web interface.

View detected fruits and the count displayed on the screen.

 Save results for further analysis.

Dataset and Training

The model is trained on a dataset of fruit images.

Custom training can be performed using YOLOv8 / Faster R-CNN with a labeled dataset.

Use LabelImg for annotation.

Training script: train.py

Future Enhancements

Implement edge processing using Raspberry Pi / Jetson Nano.

Integrate with a database for result history.

Enhance UI/UX with real-time tracking and analytics.

Contributing

Contributions are welcome! Feel free to fork this repository, open issues, or submit pull requests.

License

This project is licensed under the MIT License.

Contact

For any inquiries or contributions, reach out via eya.chaieb@insat.ucar.tn
