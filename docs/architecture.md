# GO-GLIDE Architecture Notes

## System Components

- **Vision Layer** — OpenCV + MediaPipe for hand tracking and gesture classification
- **Control Layer** — Command interpreter that maps gestures to motor actions
- **Navigation Layer** — Obstacle detection and autonomous follow logic
- **Hardware Layer** — Arduino / Raspberry Pi motor driver integration

## Gesture Command Mapping

| Gesture     | Command |
|-------------|---------|
| Open Hand   | FOLLOW  |
| Fist        | STOP    |
| Point Left  | LEFT    |
| Point Right | RIGHT   |

## Hardware Notes

- Motor driver: L298N
- Microcontroller: Arduino Uno / Raspberry Pi 4
- Sensors: HC-SR04 ultrasonic (obstacle), Pi Camera / USB webcam (vision)
- Communication: USB Serial (pyserial)
