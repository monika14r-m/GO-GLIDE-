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
        """Execute a supported command received from the gesture detector."""
        if not isinstance(command, str) or command not in COMMAND_MAP:
            logger.warning("[CMD] Ignoring unsupported command: %r", command)
            return False
        if command == self.current_command:
            return False  # Avoid re-executing the same command repeatedly

        self.current_command = command
        message = COMMAND_MAP[command]
        logger.info("[CMD] %s → %s", command, message)

        # TODO: replace with actual motor control calls
        self._mock_motor_action(command)
        return True

    def _mock_motor_action(self, command: str):
        """Placeholder for motor driver integration."""
        print(f"[MOTOR] Executing: {command}")
