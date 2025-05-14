## 🧠 ROS2 Navigation & SLAM Simulation Project
This a journey of me following the tutorial of articulated robotics to create a mobile robot. this is here is a full ROS2-based mobile robot simulation project built with blood,sweat,tears, curiosity, and late-night bug hunting.

Note: please go to the latest branch for the latest code
Latest branch : nav2_and_slam

## 🛠️ Project Overview
This project simulates a differential drive robot in a Gazebo world using ROS2 (Humble). The aim is to develop a simulated robot that can:

Be controlled via teleoperation or mobile input.
Use SLAM to build maps of unknown environments.
Navigate using Nav2 stack and autonomously move to goal positions.
Simulate real-world robotics behavior through Gazebo + RViz2.
## 🚀 Features
✅ Differential drive simulation with ros2_control and gazebo_ros2_control
✅ SLAM using slam_toolbox
✅ Full integration with Nav2 stack
✅ Twist multiplexer (twist_mux) for command management
✅ Sensor TF broadcasting (camera, lidar, wheels, etc.)
✅ RViz2 visualization
✅ URDF and SDF modeling with a clean TF tree
✅ Organized launch files for modularity
## 📦 Tech Stack
Tech	Purpose
ROS2	Robotics Middleware Framework
Gazebo	Physics-based simulation environment
RViz2	3D visualization of robot state
ros2_control	Joint control and hardware abstraction
slam_toolbox	Online and offline SLAM
Nav2	Navigation stack for path planning
URDF/SDF	Robot modeling
## 📈 Project Journey
This project WAS NOT smooth, but it was worth every challenge.

## 👨‍🏫 Started by building a custom robot URDF.
🔧 Debugged endless issues with diff_drive_controller & wheel joints.
📊 Used view_frames to troubleshoot TF conflicts.
🧙‍♂️ The breakthrough came after tweaking robot inertial parameters and plugin tuning.
💡 Realized RViz2 glitching was due to duplicated odom TF—disabled it manually and voilà! 🎉
🔀 Branching out via Git for every phase.
🧭 SLAM started mapping magic after carefully configuring the sensors and slam_toolbox.
🧩 Learned to carefully manage twist_mux parameters and params.yaml structure.
🧹 Cleaned up launches and got Nav2 running with simulation time syncing.
🥳 Final Status
The robot is now successfully able to:

Map its environment in real time.
Navigate to a defined goal using Nav2.
Accept multiple input commands using a multiplexer.
Broadcast all necessary TFs without conflict.
And all of this... without physical hardware.
Powered by: Sweat, bugs, and robot dreams 🤖
## 📁 How to Run
Make sure to build the workspace and source the overlay before launching!

cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
