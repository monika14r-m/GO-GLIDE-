"""
Obstacle Detector
Placeholder for ultrasonic sensor or depth camera integration.
"""

from src.utils.logger import get_logger

logger = get_logger(__name__)

SAFE_DISTANCE_CM = 30


class ObstacleDetector:
    def __init__(self):
        # TODO: initialize sensor (GPIO for ultrasonic / RealSense SDK)
        logger.info("ObstacleDetector initialized (mock mode).")

    def get_distance(self) -> float:
        """Returns distance to nearest obstacle in cm. Mock returns safe value."""
        # TODO: replace with real sensor read
        return 100.0

    def is_obstacle_detected(self) -> bool:
        distance = self.get_distance()
        detected = distance < SAFE_DISTANCE_CM
        if detected:
            logger.warning(f"Obstacle detected at {distance:.1f} cm!")
        return detected
