import numpy as np

class TrajectoryPredictor:
    @staticmethod
    def predict_path(tracked_points, future_frames=15):
        if len(tracked_points) < 5:
            return []

        pts = np.array(tracked_points)
        x = pts[:, 0]
        y = pts[:, 1]

        poly_x = np.polyfit(range(len(x)), x, 1)
        poly_y = np.polyfit(range(len(y)), y, 2)

        future_pts = []
        for i in range(len(tracked_points), len(tracked_points) + future_frames):
            pred_x = int(np.polyval(poly_x, i))
            pred_y = int(np.polyval(poly_y, i))
            future_pts.append((pred_x, pred_y))

        return future_pts