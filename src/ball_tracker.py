import cv2
import numpy as np
from ultralytics import YOLO

class BallTracker:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)
        self.kf = cv2.KalmanFilter(4, 2)
        self.kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
        self.kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
        self.kf.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03

    def track_frame(self, frame):
        results = self.model(frame, verbose=False)[0]
        ball_center = None

        for box in results.boxes:
            cls = int(box.cls[0])
            if cls == 32 and float(box.conf[0]) > 0.2:  # 32 = sports ball in COCO dataset
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                ball_center = np.array([[np.float32((x1 + x2) / 2)], [np.float32((y1 + y2) / 2)]])
                break

        self.kf.predict()
        if ball_center is not None:
            self.kf.correct(ball_center)
            
        state = self.kf.statePost
        return int(state[0][0]), int(state[1][0])