# GO-GLIDE

A smart mobility suitcase concept that combines computer vision, gesture recognition, and embedded systems to explore autonomous and contactless luggage navigation.

## Overview

GO-GLIDE is a robotics and computer vision project that aims to transform conventional luggage into an intelligent travel companion.

The proposed system uses hand gesture recognition for user interaction, autonomous following capabilities, and obstacle detection to assist travelers in navigating crowded environments such as airports, train stations, and campuses.

## Current gesture behavior

The camera pipeline currently recognizes two deliberately limited commands:

- **Open palm → FOLLOW**
- **Fist → STOP**

A command must be observed in three consecutive frames before it is emitted. If the hand becomes missing or ambiguous for three consecutive frames while FOLLOW is active, the detector emits STOP. Exiting the camera loop also emits a final STOP when FOLLOW is active.

Point-left and point-right gestures are not implemented yet and are ignored rather than guessed.

**Hardware safety:** motor actions are still mocked in `CommandHandler`; this repository is not ready to drive a physical suitcase. The gesture thresholds and stop behavior must be validated with the intended camera, lighting, hand orientations, and hardware before any motor driver is connected.

## Features

| Feature | Description |
| --- | --- |
| Gesture recognition | Open-palm follow and fist stop commands with frame stabilization |
| Follow mode | Command interface prepared for user-follow behavior |
| Obstacle detection | Placeholder for ultrasonic or depth-sensor integration |
| Contactless control | Gesture-based command input |
| Embedded control | Motor-driver integration planned; current motor actions are mocked |

## System architecture

```text
Camera Input
     │
     ▼
MediaPipe Hand Landmarks
     │
     ▼
Open-Palm / Fist Classifier
     │
     ▼
Three-Frame Stabilizer
     │
     ├── FOLLOW
     └── STOP (also on sustained hand loss)
             │
             ▼
      Command Handler
      (motor actions mocked)
```

## Project structure

```text
GO-GLIDE/
├── src/
│   ├── vision/             # Camera input and gesture classification
│   ├── control/            # Command interpretation and motor actions
│   ├── navigation/         # Obstacle detection and avoidance
│   └── utils/              # Shared helpers and logging
├── config/                 # Configuration files
├── docs/                   # Architecture notes and research
├── tests/                  # Unit tests
├── requirements.txt
└── main.py
```

## Getting started

Requires Python 3.9+.

```bash
git clone https://github.com/monika14r-m/GO-GLIDE-.git
cd GO-GLIDE-
pip install -r requirements.txt
python main.py
```

A camera accessible to OpenCV is required to run the live detector. Press `q` to exit the camera window.

## Run tests

Install the test runner and execute the unit suite:

```bash
python -m pip install pytest
python -m pytest -q
```

The gesture classifier tests use synthetic landmarks and do not require a camera or MediaPipe runtime.

## Planned work

- Point-left and point-right gesture classification
- Real motor-driver integration with hardware interlocks
- Real ultrasonic/depth sensor input and obstacle-stop behavior
- Follow-me tracking and field validation

## Engineering challenges

- Real-time computer vision processing
- Low-latency gesture recognition
- Autonomous navigation in crowded environments
- Sensor fusion for obstacle avoidance
- Power-efficient embedded computing

## Contributing

Suggestions related to robotics, embedded systems, computer vision, and autonomous navigation are welcome through issues and discussions.

## License

MIT License. See [LICENSE](LICENSE) for details.
