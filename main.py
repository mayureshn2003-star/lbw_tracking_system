import cv2
import numpy as np
from src.ball_tracker import BallTracker
from src.trajectory_3d import TrajectoryPredictor
from src.lbw_rules import LBWRuleEngine

def run_pipeline(video_path):
    cap = cv2.VideoCapture(video_path)
    tracker = BallTracker()
    tracked_points = []
    
    stumps_bbox = (500, 300, 600, 500) 

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cx, cy = tracker.track_frame(frame)
        if cx > 0 and cy > 0:
            tracked_points.append((cx, cy))

        for i in range(1, len(tracked_points)):
            cv2.line(frame, tracked_points[i - 1], tracked_points[i], (0, 255, 0), 2)

        if len(tracked_points) > 5:
            future_path = TrajectoryPredictor.predict_path(tracked_points[-10:])
            for pt in future_path:
                cv2.circle(frame, pt, 4, (0, 0, 255), -1)

        cv2.rectangle(frame, (stumps_bbox[0], stumps_bbox[1]), (stumps_bbox[2], stumps_bbox[3]), (255, 0, 0), 2)

        cv2.imshow("Automated LBW System", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    verdict = LBWRuleEngine.evaluate(pitching_inline=True, impact_inline=True, projected_hits_wickets=True)
    print("\n=============================")
    print("      FINAL LBW DECISION     ")
    print("=============================")
    for rule, outcome in verdict.items():
        print(f"{rule}: {outcome}")

if __name__ == "__main__":
    run_pipeline("data/videos/sample.mp4")