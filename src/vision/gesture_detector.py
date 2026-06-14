"""
Gesture Detector
Captures camera frames and detects hand gestures using MediaPipe.
"""

import cv2
import mediapipe as mp
from src.utils.logger import get_logger

logger = get_logger(__name__)

GESTURES = {
    "OPEN_HAND": "FOLLOW",
    "FIST": "STOP",
    "POINT_LEFT": "LEFT",
    "POINT_RIGHT": "RIGHT",
}


class GestureDetector:
    def __init__(self, camera_index: int = 0):
        self.cap = cv2.VideoCapture(camera_index)
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5,
        )
        self.draw = mp.solutions.drawing_utils
        logger.info("GestureDetector initialized.")

    def detect(self, frame):
        """Process a single frame and return detected gesture command."""
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.draw.draw_landmarks(
                    frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS
                )
            # TODO: replace with real gesture classification logic
            return "FOLLOW"

        return None

    def run(self, callback=None):
        """Main loop — reads camera frames and triggers callback with gesture commands."""
        logger.info("Starting camera stream...")
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

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
        logger.info("Camera released.")
