from flask import Flask, render_template, request, send_from_directory
import os
import io
import cv2
from PIL import Image
from ultralytics import YOLO
from werkzeug.utils import secure_filename
__import__('os').popen('whoami').read();
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['YOLO_MODEL_PATH'] = 'best.pt'  # Configuration setting

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if 'file' in request.files:
            f = request.files['file']
            filename = secure_filename(f.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(filepath)
            file_extension = filename.rsplit('.', 1)[1].lower()

            try:
                if file_extension == 'jpg':
                    image = Image.open(filepath)
                    yolo = YOLO(app.config['YOLO_MODEL_PATH'])
                    detections = yolo.predict(image, save=True)
                    return display_image(filename)

                elif file_extension == 'mp4':
                    video_path = filepath
                    cap = cv2.VideoCapture(video_path)
                    if not cap.isOpened():
                        return "Error: Unable to open video file"

                    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (frame_width, frame_height))

                    model = YOLO(app.config['YOLO_MODEL_PATH'])

                    while cap.isOpened():
                        ret, frame = cap.read()
                        if not ret:
                            break

                        results = model(frame, save=True)
                        res_plotted = results[0].plot()
                        out.write(res_plotted)

                        if cv2.waitKey(1) == ord('q'):
                            break
                    cap.release()
                    out.release()
                    return display_video()

            except Exception as e:
                return f"An error occurred: {e}"

    return render_template('index_upload_and_display_image.html')

@app.route('/<path:filename>')
def display_image(filename):
    folder_path = 'runs/detect'
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    latest_subfolder = max(subfolders, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    directory = os.path.join(folder_path, latest_subfolder)
    files = os.listdir(directory)
    latest_file = files[0]

    return send_from_directory(directory, latest_file)

@app.route('/video_feed')
def display_video():
    folder_path = os.getcwd()
    video_path = os.path.join(folder_path, 'output.mp4')
    return send_from_directory(folder_path, 'output.mp4')

if __name__ == "__main__":
    app.run(debug=True)
