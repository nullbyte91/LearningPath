# Ros - Robot Operating System

## 0.1 ROS Installation on Ubuntu 16.04 LTS

Follow the lecture, instructions are the same. But use the commands from this page instead : http://wiki.ros.org/kinetic/Installation/Ubuntu

## 1.0 Creating a catkin workspace

```bash
cd ~/Desktop/
mkdir catkin_ws/
cd catkin_ws/
mkdir src
catkin_make
```

Now, We can see that build and devel folder created by catkin_make. And, Can see CMakeLists.txt symbolic link too inside src folder.

### Setup ROS environment

```bash
cd devel
source setup.bash
```

or add it in .bashrc file,

```bash
vim ~/.bashrc
source /home/nullbyte/Desktop/catkin_ws/devel/setup.bash
```
