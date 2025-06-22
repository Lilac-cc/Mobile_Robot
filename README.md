# 移动机器人技术基础ROS作业

**配置**：Ubuntu 20.04  ROS noetic

## 两轮差动机器人
**/robot 文件夹**
**复用**：
1. 创建工作空间ws
2. 将该文件夹下代码下载至/src
3. 在该层级文件夹终端中运行catkin_make，编译工作空间
4. 可识别的机器人命名为“robot"
5. 需要的功能包主要有：ros_control、navigation

**可实现功能**：
1. gazebo中导入机器人模型：roslaunch robot gazebo.launch
2. 为机器人配置差动控制器，速度控制话题为/DiffDriveController/cmd_vel，在sim.launch启动文件中加载控制器，已集成gazebo和rviz的启动。
3. rqt可视化控制机器人运动，通过速度控制话题发布角速度、线速度命令，代码在sim.launch中已被注释。
4. 地图模型在/map文件夹下，有yaml配置文件和pgm二进制文件，相当于激光雷达建图完成。
5. 启动nav.launch文件可实现在地图中的全局路径规划和避障、轨迹跟踪，该launch文件集成了amcl节点（自适应定位）和move_base节点（驱动机器人模型），参数配置文件均在/config文件夹下，复用时可修改局部代价地图的膨胀系数。
6. 注意nav.launch文件仅发布话题节点，运行之前需要先运行sim.launch文件，加载机器人模型和控制器等。

## 轮滑机器人
**/roller_3rd 文件夹**
**复用**：
1. 创建工作空间ws
2. 将该文件夹下代码下载至/src
3. 在该层级文件夹终端中运行catkin_make，编译工作空间（注意其中包含python文件的编译）
4. 可识别的机器人命名为“roller_3rd"
5. 需要的功能包主要有：ros_control

**可实现功能**：
1. gazebo中导入机器人模型：roslaunch roller_3rd gazebo.launch
2. 为机器人12个关节分别配置速度控制器，在sim.launch启动文件中加载控制器，已集成gazebo和rviz的启动。
3. python文件为速度控制器发布速度命令，首先需运行sim.launch文件，后在新终端运行rosrun roller_3rd pubCommand.py，可实现速度指令的发布，目前代码为自转运动的尝试，未进行完整运动学建模。
