"""Tests for ObstacleDetector"""

from src.navigation.obstacle_detector import ObstacleDetector


def test_mock_distance_is_safe():
    detector = ObstacleDetector()
    assert detector.get_distance() > 30


def test_no_obstacle_in_mock():
    detector = ObstacleDetector()
    assert detector.is_obstacle_detected() is False
