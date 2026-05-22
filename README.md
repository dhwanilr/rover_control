## Overview

'rover_control' is a ROS2 based rover control system that implements a modular pipeline using multiple nodes, including the following nodes:

- Sensor Node (data collection)
- Perception Node (processing sensor data)
- Decision Node (nagivation logic)
- Motor Node (movement control)
- Launch file to start the full system

The system is designed as a simple pipeline where sensor data flows through collection -> perception -> decision -> motor control.

## System Architecture
Each node communicates through ROS2 topics

---

## Nodes

### 1. Sensor Node
- Publishes raw sensor data
- Topic: `/scan`

### 2. Perception Node
- Subscribes to `/scan`
- Processes data (basic filtering / interpretation)
- Publishes `/obstacle_info`

### 3. Decision Node
- Subscribes to `/obstacle_info`
- Determines rover action (e.g., forward, left, right, stop)
- Publishes `/cmd_vel`

### 4. Motor Node
- Subscribes to `/cmd_vel`
- Converts decisions into motor commands
- Outputs final actuator commands

---

## Launch File

A launch file is provided to start all nodes:

```bash
ros2 launch rover_control rover.launch.py
```

## Build Instructions

### 1. Clone Workspace
```
cd ~/ros2_ws/src
```
```
git clone https://github.com/dhwanilr/rover_control.git
```
Or download zip and extract in your ROS2 workspace folder

### 2. Build Workspace
```
cd ~/ros2_ws/src
```
```
colcon build
```

### 3. Source Setup
```
source install/setup.bash
```

### 4. Run rover_control
```
ros2 launch rover_control rover.launch.py
```
