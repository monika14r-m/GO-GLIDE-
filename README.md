# GO-GLIDE

A smart mobility suitcase concept that combines computer vision, gesture recognition, and embedded systems to explore autonomous and contactless luggage navigation.

---

## Overview

GO-GLIDE is a robotics and computer vision project that aims to transform conventional luggage into an intelligent travel companion.

The proposed system uses hand gesture recognition for user interaction, autonomous following capabilities, and obstacle detection to assist travelers in navigating crowded environments such as airports, train stations, and campuses.

The project serves as an exploration of computer vision, embedded systems, robotics, and human-computer interaction.

---

## Proposed Features

| Feature             | Description                                         |
| ------------------- | --------------------------------------------------- |
| Gesture Recognition | Hand gesture detection for movement commands        |
| Follow Mode         | Autonomous tracking of the user                     |
| Obstacle Avoidance  | Detection and avoidance of nearby obstacles         |
| Contactless Control | Interaction without physical handles or controls    |
| Embedded Control    | Integration with microcontrollers and motor drivers |

---

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

---

## Planned Technology Stack

| Component            | Technologies                        |
| -------------------- | ----------------------------------- |
| Computer Vision      | OpenCV, MediaPipe                   |
| Embedded Control     | Raspberry Pi, Arduino               |
| Obstacle Detection   | Ultrasonic Sensors, Intel RealSense |
| Motor Driver         | L298N                               |
| Programming Language | Python                              |

---

## Development Roadmap

### Phase 1 — Computer Vision

* [ ] Hand detection pipeline
* [ ] Static gesture recognition
* [ ] Real-time gesture classification
* [ ] Command mapping

### Phase 2 — Embedded Systems

* [ ] Motor controller integration
* [ ] Raspberry Pi and Arduino communication
* [ ] Basic movement control

### Phase 3 — Autonomous Navigation

* [ ] Follow-me mode
* [ ] Obstacle detection
* [ ] Obstacle avoidance
* [ ] Path correction

### Phase 4 — System Integration

* [ ] Full prototype assembly
* [ ] Field testing
* [ ] Performance evaluation
* [ ] Reliability improvements

---

## Engineering Challenges

The project explores several technical challenges:

* Real-time computer vision processing
* Low-latency gesture recognition
* Autonomous navigation in crowded environments
* Sensor fusion for obstacle avoidance
* Power-efficient embedded computing
* Reliable motor control and path tracking

---

## Current Status

🚧 **Research & Architecture Phase**

Current work focuses on:

* System design
* Component selection
* Architecture planning
* Prototype feasibility analysis

Implementation has not yet begun.

---

## Future Enhancements

* Dynamic gesture customization
* Mobile companion application
* GPS-assisted navigation
* Voice command integration
* Multi-user recognition
* Indoor localization

---

## Contributing

This project is currently in the planning stage.

Suggestions related to robotics, embedded systems, computer vision, and autonomous navigation are welcome through issues and discussions.

---

## License

Licensed under the MIT License.

See the `LICENSE` file for additional information.

