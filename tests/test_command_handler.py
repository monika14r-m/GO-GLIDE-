"""Tests for CommandHandler"""

import pytest
from src.control.command_handler import CommandHandler


def test_valid_command_executes():
    handler = CommandHandler()
    handler.execute("FOLLOW")
    assert handler.current_command == "FOLLOW"


def test_same_command_not_repeated():
    handler = CommandHandler()
    handler.execute("STOP")
    handler.execute("STOP")
    assert handler.current_command == "STOP"


def test_unknown_command_handled():
    handler = CommandHandler()
    handler.execute("SPIN")
    assert handler.current_command == "SPIN"
