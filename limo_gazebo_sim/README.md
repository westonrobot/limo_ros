# limo_gazebo_sim

## About
This package contains the gazebo simulation worlds and launch configuration files needed to run a limo robot within a gazebo simulation.

## Environment
On top of the ROS installation, we will need additional packages to run the simulations successfully.

### Download and install required function package

​	Download and install ros-control function package, ros-control is the robot control middleware provided by ROS

```
sudo apt install ros-melodic-ros-control
```

​	Download and install ros-controllers function package, ros-controllers are the kinematics plug-in of common models provided by ROS

```
sudo apt install ros-melodic-ros-controllers
```

​	Download and install gazebo-ros function package, gazebo-ros is the communication interface between gazebo and ROS, and connect the ROS and Gazebo

```
sudo apt install ros-melodic-gazebo-ros
```

​	Download and install gazebo-ros-control function package, gazebo-ros-control is the communication standard controller between ROS and Gazebo

```
sudo apt install ros-melodic-gazebo-ros-control
```

​	Download and install joint-state-publisher-gui package.This package is used to visualize the joint control.

```
sudo apt install ros-melodic-joint-state-publisher-gui 
```

​	Download and install rqt-robot-steering plug-in, rqt_robot_steering is a ROS tool closely related to robot motion control, it can send the control command of robot linear motion and steering motion, and the robot motion can be easily controlled through the sliding bar

```
sudo apt install ros-melodic-rqt-robot-steering 
```

​	Download and install teleop-twist-keyboard function package, telop-twist-keyboard is keyboard control function package, the robot can be controlled to move forward, left, right and backward through "i", "j", "l",and "," on the keyboard

```
sudo apt install ros-melodic-teleop-twist-keyboard 
```

## Usage
### 1. Run the star file of limo model and visualize the urdf file in Rviz
```bash
roslaunch limo_description display_models.launch 
```

![img](image/rviz.png) 

### 2. Start the gazebo simulation environment of limo

The limo has 2 movement modes in the simulation, Ackerman and Four-wheel differential drive.

#### 1. Ackerman Movement Mode

```
roslaunch limo_gazebo_sim limo_ackerman.launch
```
### 2. Four-wheel Differential Steering Movement Mode

```
roslaunch limo_gazebo_sim limo_four_diff.launch 
```

### 3. Controlling the Limo in simulation
We have 2 ways to control the limo in simulation, using...
1. rqt_robot_steering movement control plug-in
2. publishing to /cmd_vel using teleop_twist_keyboard

#### 1. rqt_robot_steering movement control plug-in

​Start rqt_robot_steering movement control plug-in, the sliding bar can control the robot motion
```
rosrun rqt_robot_steering rqt_robot_steering
```

![img](image/limo_ackerman.png) 

#### 2. teleop_twist_keyboard
Control by keyboard, the robot can be controlled to move forward, left, right and backward through "i", "j", "l",and "," on the keyboard

```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py 
```

![img](image/limo_diff.png) 