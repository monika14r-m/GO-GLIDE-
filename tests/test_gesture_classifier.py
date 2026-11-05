"""Tests for safe hand-pose classification and command stabilization."""

from src.vision.gesture_classifier import GestureStabilizer, classify_gesture


def make_hand(tip_y):
    points = [(0.5, 0.9) for _ in range(21)]
    for pip_index, tip_index, x in (
        (6, 8, 0.35),
        (10, 12, 0.45),
        (14, 16, 0.55),
        (18, 20, 0.65),
    ):
        points[pip_index] = (x, 0.6)
        points[tip_index] = (x, tip_y)
    return points


def test_open_palm_maps_to_follow():
    assert classify_gesture(make_hand(0.3)) == "FOLLOW"


def test_fist_maps_to_stop():
    assert classify_gesture(make_hand(0.8)) == "STOP"


def test_ambiguous_pose_is_ignored():
    assert classify_gesture(make_hand(0.58)) is None


def test_invalid_landmarks_are_ignored():
    assert classify_gesture([]) is None
    assert classify_gesture(None) is None
    invalid = make_hand(0.3)
    invalid[8] = (float("nan"), 0.3)
    assert classify_gesture(invalid) is None


def test_command_requires_consecutive_stable_frames():
    stabilizer = GestureStabilizer(stable_frames=3)
    assert stabilizer.update("FOLLOW") is None
    assert stabilizer.update("FOLLOW") is None
    assert stabilizer.update("FOLLOW") == "FOLLOW"
    assert stabilizer.update("FOLLOW") is None


def test_losing_hand_after_follow_emits_stop():
    stabilizer = GestureStabilizer(stable_frames=3)
    for _ in range(3):
        stabilizer.update("FOLLOW")
    assert stabilizer.update(None) is None
    assert stabilizer.update(None) is None
    assert stabilizer.update(None) == "STOP"
    assert stabilizer.stop() is None


def test_ambiguous_frames_do_not_confirm_new_command():
    stabilizer = GestureStabilizer(stable_frames=3)
    assert stabilizer.update("FOLLOW") is None
    assert stabilizer.update(None) is None
    assert stabilizer.update("FOLLOW") is None
    assert stabilizer.update("FOLLOW") is None
    assert stabilizer.update("FOLLOW") == "FOLLOW"


def test_shutdown_emits_stop_only_when_following():
    stabilizer = GestureStabilizer()
    assert stabilizer.stop() is None
    for _ in range(3):
        stabilizer.update("FOLLOW")
    assert stabilizer.stop() == "STOP"


def test_unsupported_direction_gesture_is_not_forwarded():
    stabilizer = GestureStabilizer(stable_frames=1)
    assert stabilizer.update("LEFT") is None


def test_stable_frame_count_must_be_positive_integer():
    for value in (0, -1, True, 1.5):
        try:
            GestureStabilizer(stable_frames=value)
        except ValueError:
            continue
        raise AssertionError(f"Expected ValueError for {value!r}")
