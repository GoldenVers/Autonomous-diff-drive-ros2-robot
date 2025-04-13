import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='articubot_one' #<--- CHANGE ME

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')



    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
    ])




#okay, so far what have we done?
# we have modified the code to run with gazebo classic instead of ignition and the reason is ignition is so bad, I had to work with the raw sdf files to add the plugins and the lidar plugin was very tiring to add, it was time consuming
# and I had to run into loops of debugging
#now that we are good to go, so far we are able to run it in gazebo and rviz2, then control it with the teleop_twist_keyboard package 
#the include tag in the robot.urdf.xacro file is not really working, it just takes the main core file and dont take the others. 
#I had to add the lidar plugins manually 
#the lidar work this way: you add the lidar joint in the core.xacro and then in the gazebo tag you have to add the sensor and the plugin things
#it was not working initially and this is due to some deprecation, <argument>~/out:=scan</argument> is replaced with <remapping>~/out:=scan</remapping>
 # <visualise> tag should be true and not false if you want to see the rays in gazebo
#thats it for gazebo, here is the commands steps
# 1. ros2 launch articubot_one launch_sim.launch.py
# 2. ros2 run teleop_twist_keyboard teleop_twist_keyboard 
# 3. ros2 run rviz2 

# 4. add the robot model and the laser scan
# 5. add the laser scan topic and the robot model
# 6. main frame is odom
