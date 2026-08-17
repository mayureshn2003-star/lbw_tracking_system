import cv2

class PitchDetector:
    def __init__(self, stump_bbox):
        self.stump_bbox = stump_bbox

    def is_impact_inline(self, impact_x):
        x_min, _, x_max, _ = self.stump_bbox
        return x_min <= impact_x <= x_max