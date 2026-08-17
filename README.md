# Automated Real-Time Umpiring & LBW Tracking System

A Computer Vision and Machine Learning pipeline designed to track a cricket ball in real-time, fit a parabolic trajectory, and evaluate automated Leg Before Wicket (LBW) decisions based on ICC rules.

## Features
- **Ball Detection & Tracking:** Leverages YOLOv8 combined with a 2D Kalman Filter for frame-by-frame object tracking and state prediction.
- **Trajectory Projection:** Fits a parabolic curve ($y = ax^2 + bx + c$) to model future ball movement towards the stumps.
- **LBW Decision Engine:** Automates three-stage evaluation (Pitching Line, Impact Line, and Projected Wicket Hit).

## Project Structure
```text
lbw_tracking_system/
│
├── data/
│   └── videos/          # Input test clips
│
├── src/
│   ├── __init__.py
│   ├── ball_tracker.py   # YOLOv8 + Kalman Filter integration
│   ├── pitch_detector.py # Pitch & Stump boundary region calculations
│   ├── trajectory_3d.py  # Parabolic curve prediction algorithm
│   └── lbw_rules.py      # Automated decision rules logic
│
├── main.py              # Main pipeline orchestrator
└── README.md