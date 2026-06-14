"""
Command Handler
Receives gesture commands and routes them to the appropriate motor actions.
"""

from src.utils.logger import get_logger

logger = get_logger(__name__)

COMMAND_MAP = {
    "FOLLOW": "Activating follow mode",
    "STOP": "Halting all motors",
    "LEFT": "Turning left",
    "RIGHT": "Turning right",
}


class CommandHandler:
    def __init__(self):
        self.current_command = None
        logger.info("CommandHandler ready.")

    def execute(self, command: str):
        """Execute a command received from the gesture detector."""
        if command == self.current_command:
            return  # Avoid re-executing the same command repeatedly

        self.current_command = command
        message = COMMAND_MAP.get(command, f"Unknown command: {command}")
        logger.info(f"[CMD] {command} → {message}")

        # TODO: replace with actual motor control calls
        self._mock_motor_action(command)

    def _mock_motor_action(self, command: str):
        """Placeholder for motor driver integration."""
        print(f"[MOTOR] Executing: {command}")
