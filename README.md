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

- Create a ROS Workspace that will allow us to correctly organize and package our application. We start in our home directory and we type in the terminal:

```bash
mkdir catkin_ws/src
cd catkin_ws
catkin_make
```
This will allow us to create a new folder in the home directory called `catkin_ws` vy using the `mkdir` command. Then we create a source `src` folder inside the catkin workspace folder. Once done this, make sure to use the command `catkin_make` inside the `catkin_ws` folder in order to init the workspace. Now, you can see that inside the `src` folder there are new folders called `devel` and `build`

- Then, we will need to source the new `setup.bash` file inside the `devel` folder. In order to do this, it is necessary to go back in our home directory with the `cd` command and then type:

```bash
cd
source ~/catkin_ws/devel/setup.bash
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

