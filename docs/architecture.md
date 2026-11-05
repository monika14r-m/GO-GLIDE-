# GO-GLIDE Architecture Notes

## System components

- **Vision layer** — OpenCV + MediaPipe for hand tracking and gesture classification.
- **Control layer** — Command interpreter that maps stable gesture commands to motor actions.
- **Navigation layer** — Obstacle detection and autonomous follow logic (currently placeholders).
- **Hardware layer** — Arduino / Raspberry Pi motor-driver integration (not connected yet).

## Implemented gesture behavior

| Pose | Command | Status |
| --- | --- | --- |
| Open palm | FOLLOW | Implemented; requires three consecutive frames |
| Fist | STOP | Implemented; requires three consecutive frames |
| Point left | LEFT | Not implemented; ignored |
| Point right | RIGHT | Not implemented; ignored |

The classifier compares the wrist-to-fingertip distance with the corresponding wrist-to-PIP-joint distance for the four non-thumb fingers. Mixed or uncertain poses are ignored. The stabilizer requires three consecutive matching frames before changing commands. If no confident pose is available for three frames while FOLLOW is active, it emits STOP. Leaving the camera loop also emits a final STOP when FOLLOW is active.

## Hardware safety status

`CommandHandler` still uses mock motor actions. The project must not be treated as ready for physical movement. Before connecting a motor driver, validate the classifier under the intended camera positions, lighting, hand orientations, and occlusion conditions, then add independent hardware emergency-stop and obstacle interlocks.

## Hardware notes

- Motor driver: L298N (planned)
- Microcontroller: Arduino Uno / Raspberry Pi 4 (planned)
- Sensors: HC-SR04 ultrasonic (planned)
- Camera: Pi Camera / USB webcam
- Communication: USB Serial (pyserial, planned)
