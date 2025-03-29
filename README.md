
# 🍎 Fruit Detection and Counting

## 📌 Project Overview
This project focuses on detecting and counting fruits using computer vision and deep learning. A web interface is provided to visualize the detection results in real time, making it accessible for users to monitor and analyze fruit data efficiently.

## 🏗 Features
- **Real-time Fruit Detection**: Uses a trained deep learning model to identify different fruits.
- **Accurate Counting**: The system detects and counts the number of fruits in an image or video feed.
- **Web Interface**: A user-friendly dashboard displays the results interactively.
- **Performance Logging**: Stores detection results for further analysis.

## ⚙️ Technologies Used
- **Programming Language**: Python
- **Deep Learning Framework**: TensorFlow / PyTorch
- **Object Detection Model**: YOLO 
- **Backend**: Flask 
- **Frontend**: HTML, CSS, JavaScript, Bootstrap

## 🚀 Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/ayachaieb/fruit-detection-and-counting.git
   cd fruit-detection-and-counting
   ```

2. **Create a Virtual Environment **
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download or Train the Model**
   - If using a pre-trained model, download it and place it in the `models/` directory.
   - To train your own model, follow the instructions in `train_model.ipynb`.

5. **Run the Web App**
   ```bash
   python app.py
   ```
   Access the interface at `http://127.0.0.1:5000/` in your browser.

## 🖼 Sample Usage
- Upload an image or enable live camera mode.
- The system detects and counts fruits in the frame.
- Results are displayed on the web dashboard with bounding boxes.


## 🛠 Future Improvements
- Support for more fruit types.
- Mobile app integration.
- Cloud-based storage for detection results.
- Optimized model for better real-time performance.

## 📜 License
This project is licensed under the MIT License.

## 📩 Contact
For any inquiries or contributions, feel free to reach out at `eya.chaieb@insat.tn`.

