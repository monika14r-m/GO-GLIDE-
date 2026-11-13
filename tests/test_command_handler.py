"""Tests for CommandHandler."""

from src.control.command_handler import CommandHandler


def test_valid_command_executes():
    handler = CommandHandler()
    calls = []
    handler._mock_motor_action = calls.append

    assert handler.execute("FOLLOW") is True
    assert handler.current_command == "FOLLOW"
    assert calls == ["FOLLOW"]


def test_same_command_not_repeated():
    handler = CommandHandler()
    calls = []
    handler._mock_motor_action = calls.append

    assert handler.execute("STOP") is True
    assert handler.execute("STOP") is False
    assert handler.current_command == "STOP"
    assert calls == ["STOP"]


def test_unknown_command_is_rejected_without_motor_action():
    handler = CommandHandler()
    calls = []
    handler._mock_motor_action = calls.append

    assert handler.execute("SPIN") is False
    assert handler.current_command is None
    assert calls == []


def test_non_string_command_is_rejected_without_changing_active_command():
    handler = CommandHandler()
    calls = []
    handler._mock_motor_action = calls.append
    assert handler.execute("FOLLOW") is True

    assert handler.execute(None) is False
    assert handler.current_command == "FOLLOW"
    assert calls == ["FOLLOW"]
