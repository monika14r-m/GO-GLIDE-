"""Pure-Python gesture classification and command stabilization."""

from math import hypot, isfinite
from typing import Optional, Sequence

# MediaPipe hand landmark indices: (tip, PIP joint) for index through pinky.
_FINGER_JOINTS = ((8, 6), (12, 10), (16, 14), (20, 18))
_EXTENSION_RATIO = 1.12
_CURL_RATIO = 0.92
_SUPPORTED_COMMANDS = {"FOLLOW", "STOP"}


def _point_xy(point):
    """Read normalized x/y coordinates from a MediaPipe point or an (x, y) pair."""
    try:
        if hasattr(point, "x") and hasattr(point, "y"):
            x, y = float(point.x), float(point.y)
        else:
            x, y = float(point[0]), float(point[1])
    except (TypeError, ValueError, IndexError, KeyError, AttributeError):
        return None
    if not isfinite(x) or not isfinite(y):
        return None
    return x, y


def classify_gesture(landmarks: Sequence) -> Optional[str]:
    """Return FOLLOW for an open palm, STOP for a fist, or None if ambiguous.

    Finger extension is estimated by comparing each fingertip's distance from
    the wrist with its PIP joint's distance. Mixed/uncertain poses are ignored.
    """
    if landmarks is None or len(landmarks) < 21:
        return None

    points = [_point_xy(point) for point in landmarks[:21]]
    if any(point is None for point in points):
        return None

    wrist_x, wrist_y = points[0]
    extended = []
    for tip_index, pip_index in _FINGER_JOINTS:
        tip_x, tip_y = points[tip_index]
        pip_x, pip_y = points[pip_index]
        tip_distance = hypot(tip_x - wrist_x, tip_y - wrist_y)
        pip_distance = hypot(pip_x - wrist_x, pip_y - wrist_y)
        if pip_distance <= 1e-6:
            return None
        if tip_distance >= pip_distance * _EXTENSION_RATIO:
            extended.append(True)
        elif tip_distance <= pip_distance * _CURL_RATIO:
            extended.append(False)
        else:
            return None

    if all(extended):
        return "FOLLOW"
    if not any(extended):
        return "STOP"
    return None


class GestureStabilizer:
    """Require consecutive frames before changing commands; stop after hand loss."""

    def __init__(self, stable_frames: int = 3):
        if isinstance(stable_frames, bool) or not isinstance(stable_frames, int) or stable_frames < 1:
            raise ValueError("stable_frames must be a positive integer")
        self.stable_frames = stable_frames
        self.current_command = None
        self._candidate = None
        self._candidate_count = 0
        self._missing_count = 0

    def update(self, candidate: Optional[str]) -> Optional[str]:
        """Return a command only when a new pose is stable or FOLLOW is lost."""
        if not isinstance(candidate, str) or candidate not in _SUPPORTED_COMMANDS:
            candidate = None

        if candidate is None:
            self._candidate = None
            self._candidate_count = 0
            self._missing_count += 1
            if self.current_command == "FOLLOW" and self._missing_count >= self.stable_frames:
                self.current_command = "STOP"
                self._missing_count = 0
                return "STOP"
            return None

        self._missing_count = 0
        if candidate == self.current_command:
            self._candidate = None
            self._candidate_count = 0
            return None

        if candidate != self._candidate:
            self._candidate = candidate
            self._candidate_count = 1
        else:
            self._candidate_count += 1

        if self._candidate_count >= self.stable_frames:
            self.current_command = candidate
            self._candidate = None
            self._candidate_count = 0
            return candidate
        return None

    def stop(self) -> Optional[str]:
        """Request a final STOP when the active command was FOLLOW."""
        if self.current_command != "FOLLOW":
            return None
        self.current_command = "STOP"
        self._candidate = None
        self._candidate_count = 0
        self._missing_count = 0
        return "STOP"
