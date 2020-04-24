# Continuation
### Steps to run
In four separate terminals, run:
1. roslaunch jackal_gazebo jackal_world.launch config:=front_laser
2. roslaunch jackal_navigation gmapping_demo.launch
3. roslaunch jackal_viz view_robot.launch config:=gmapping
4. rosrun area_nav nav.py
    a. When prompted, enter 'go' (quotes included) to run the 4-building search
    b. Otherwise, enter a list of coordinates