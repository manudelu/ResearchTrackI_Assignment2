# ResearchTrack_Assignment2
Research Track I - Assignment II :  Implementation of an Action Server that Moves a Robot in the Environment

Create and setup a Catkin Workspace
--------------------------------

It is the purpose of this assignment to develop a ROS package containing three ROS nodes that provide a way to interact with the environment presented in the assignment_2_2022 package.

The simulation requires the following steps for running:

- A ROS Noetic (ROS Noetic installation instructions)
- Run the ROS core by executing this command in terminal:

```bash
roscore
```

Create a catkin (ROS) Workspace. A catkin workspace is a directory in which you can create or modify existing catkin packages. We will label our catkin workspace `catkin_ws`. To create the catkin workspace, type the following commands in the Terminal:

```bash
mkdir catkin_ws/src
cd catkin_ws
catkin_make
```

This will allow us to create a new folder in the home directory called `catkin_ws` by using the `mkdir` command. Then we create a source `src` folder inside the catkin workspace folder. Once done, make sure to use the command `catkin_make` inside the `catkin_ws` folder in order to init the catkin workspace. If you view your current directory contents, you should now have the `devel` and `build` folders. Inside the `devel` folder there are now several `setup.*sh` files. Then, we will need to source the `setup.bash` file to overlay this workspace on top of your ROS environment. In order to do this, it is necessary to go back in our home directory with the `cd` command and then type:

```bash
source ~/catkin_ws/devel/setup.bash
```

Remember to add this source command to your `.bashrc` file under the source line of the global ROS installation. This is important in order to use your code with ROS functionalities. In order to open the `.bashrc` file type the following command:

```bash
gedit ~/.bashrc
```

- Move to the src folder of the workspace and then clone the package assignment_2_2022 which provides an implementation of an action server that moves a robot in the environment by implementing the bug0 algorithm:

```bash
git clone https://github.com/CarmineD8/assignment_2_2022
```

-Clone the package of my solution for this assignment:

```bash
git clone ---insert assignment---
```

- Then:

```bash
cd
cd catkin_ws
catkin_make
```

- Now, it is possible to run the whole project by running the launch file:

```bash
roslaunch rt1_2nd_assignment rt1_2nd_assignment.launch (da modificare)
```

