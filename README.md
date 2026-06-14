# GO-GLIDE

A smart mobility suitcase concept that combines computer vision, gesture recognition, and embedded systems to explore autonomous and contactless luggage navigation.

## Overview

GO-GLIDE is a robotics and computer vision project that aims to transform conventional luggage into an intelligent travel companion.

The proposed system uses hand gesture recognition for user interaction, autonomous following capabilities, and obstacle detection to assist travelers in navigating crowded environments such as airports, train stations, and campuses.

## Proposed Features

| Feature             | Description                                         |
| ------------------- | --------------------------------------------------- |
| Gesture Recognition | Hand gesture detection for movement commands        |
| Follow Mode         | Autonomous tracking of the user                     |
| Obstacle Avoidance  | Detection and avoidance of nearby obstacles         |
| Contactless Control | Interaction without physical handles or controls    |
| Embedded Control    | Integration with microcontrollers and motor drivers |

## System Architecture

```text
Camera Input
     │
     ▼
Hand Gesture Recognition
 (MediaPipe / OpenCV)
     │
     ▼
Command Interpreter
     │
     ├── Follow Mode
     ├── Stop
     └── Direction Commands
             │
             ▼
 Motor Controller
(Arduino / Raspberry Pi)
             │
             ▼
 Obstacle Detection Layer
(Ultrasonic / Depth Sensors)
             │
             ▼
      Suitcase Motion
```

## Project Structure

```
GO-GLIDE/
├── src/
│   ├── vision/             # Camera input, gesture recognition
│   ├── control/            # Motor control and command execution
│   ├── navigation/         # Follow mode, obstacle avoidance
│   └── utils/              # Shared helpers and logging
├── hardware/               # Arduino sketches and wiring diagrams
├── tests/                  # Unit and integration tests
├── docs/                   # Architecture notes and research
├── config/                 # Configuration files
├── requirements.txt
└── main.py
```

## Getting Started

**Requires Python 3.9+**

```bash
git clone https://github.com/monika14r-m/GO-GLIDE.git
cd GO-GLIDE
pip install -r requirements.txt
python main.py
```

## Planned Technology Stack

| Component            | Technologies                        |
| -------------------- | ----------------------------------- |
| Computer Vision      | OpenCV, MediaPipe                   |
| Embedded Control     | Raspberry Pi, Arduino               |
| Obstacle Detection   | Ultrasonic Sensors, Intel RealSense |
| Motor Driver         | L298N                               |
| Programming Language | Python                              |

## Development Roadmap

### Phase 1 — Computer Vision
- [ ] Hand detection pipeline
- [ ] Static gesture recognition
- [ ] Real-time gesture classification
- [ ] Command mapping

### Phase 2 — Embedded Systems
- [ ] Motor controller integration
- [ ] Raspberry Pi and Arduino communication
- [ ] Basic movement control

### Phase 3 — Autonomous Navigation
- [ ] Follow-me mode
- [ ] Obstacle detection and avoidance
- [ ] Path correction

### Phase 4 — System Integration
- [ ] Full prototype assembly
- [ ] Field testing
- [ ] Performance evaluation

## Engineering Challenges

- Real-time computer vision processing
- Low-latency gesture recognition
- Autonomous navigation in crowded environments
- Sensor fusion for obstacle avoidance
- Power-efficient embedded computing

## Current Status

🚧 **Research & Architecture Phase** — implementation starting now.

## Contributing

Suggestions related to robotics, embedded systems, computer vision, and autonomous navigation are welcome through issues and discussions.

## License

MIT License. See [LICENSE](LICENSE) for details.
