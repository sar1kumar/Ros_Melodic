#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

import sys

PI = 3.1415926535897

#Executing the pose_callback function whenever a message is received

def pose_callback(pose):
    if (current_angle<radian_angle):
        rospy.loginfo("Moving in a circle\n%f",current_angle)
        rate = rospy.Rate(4)
        rate.sleep()
    else:
        rospy.loginfo("Completed\n\npress ctrl+c to Kill the process") # Displaying completed Message After One revolution 
        rate = rospy.Rate(0.003)
        rate.sleep()
        sub.unregister()
        
def circle():
    #starting the node
    rospy.init_node('move_turtle',anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(4)
    vel_msg = Twist()
    global sub
    sub = rospy.Subscriber('/turtle1/pose',Pose,pose_callback)

    print("let the rotation begin")
    speed=36                           #degrees/sec
    angle=360
    
    angular_speed=speed*2*PI/360       #radians/sec
    global radian_angle
    radian_angle=angle*2*PI/360

    vel_msg.linear.x=1
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x=0
    vel_msg.angular.y=0
    vel_msg.angular.z=abs(angular_speed)

    t0=rospy.Time.now().to_sec()
    global current_angle
    current_angle =0

    while(current_angle<radian_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
    vel_msg.angular.z = 1.5
    vel_msg.linear.x=0
    velocity_publisher.publish(vel_msg)
    rospy.spin()
    rate.sleep()
if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
