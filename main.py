"""
GO-GLIDE — Entry Point
Gesture-Controlled Smart Suitcase
"""

from src.vision.gesture_detector import GestureDetector
from src.control.command_handler import CommandHandler
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("GO-GLIDE system starting...")

    detector = GestureDetector()
    handler = CommandHandler()

    try:
        detector.run(callback=handler.execute)
    except KeyboardInterrupt:
        logger.info("Shutting down GO-GLIDE.")
    finally:
        detector.release()


if __name__ == "__main__":
    main()
