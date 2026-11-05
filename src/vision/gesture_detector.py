"""
Gesture Detector
Captures camera frames and classifies stable hand poses using MediaPipe.
"""

import cv2
import mediapipe as mp

from src.vision.gesture_classifier import GestureStabilizer, classify_gesture
from src.utils.logger import get_logger

logger = get_logger(__name__)


class GestureDetector:
    def __init__(self, camera_index: int = 0, stable_frames: int = 3):
        self.cap = cv2.VideoCapture(camera_index)
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5,
        )
        self.draw = mp.solutions.drawing_utils
        self.stabilizer = GestureStabilizer(stable_frames=stable_frames)
        logger.info("GestureDetector initialized.")

    def detect(self, frame):
        """Return a debounced FOLLOW/STOP command, or None for uncertain poses."""
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        candidate = None

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.draw.draw_landmarks(
                    frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS
                )
            candidate = classify_gesture(results.multi_hand_landmarks[0].landmark)

        return self.stabilizer.update(candidate)

    def run(self, callback=None):
        """Read camera frames and emit only stable commands."""
        logger.info("Starting camera stream...")
        try:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    logger.warning("Failed to read frame.")
                    break

                command = self.detect(frame)
                if command and callback:
                    callback(command)

                cv2.imshow("GO-GLIDE | Gesture View", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            # Never leave a previously active follow command latched on shutdown.
            stop_command = self.stabilizer.stop()
            if stop_command and callback:
                callback(stop_command)

    def release(self):
        self.cap.release()
        self.hands.close()
        cv2.destroyAllWindows()
        logger.info("Camera released.")
