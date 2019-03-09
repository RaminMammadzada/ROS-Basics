#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3
from numpy import random as np

# Python program to get average of a list


def Average(lst):
    return sum(lst) / len(lst)


vel = Twist()


def callback(msgs):
    # print msgs  # This will print the whole Odometry message
    # print msg.header  # This will print the header section of the Odometry message
    # This will print the pose section of the Odometry message
    # m = msgs[1:3]

    last_range = 9999999999

    ranges = msgs.ranges
    middle_idx = len(ranges) // 2
    this_range = ranges[middle_idx]

    if range < 0.25:
        if this_range < last_range:
            if vel.linear.x > 0:
                vel.linear.x -= 0.02
            if vel.angular.z < 1:
                vel.angular.z += 0.02
        if this_range > last_range:
            if vel.linear.x < 1:
                vel.linear.x += 0.02
            if vel.angular.z > 0:
                vel.angular.z -= 0.02
    else:
        linear_x = np.rand()
        angular_z = np.rand()
        vel.linear = Vector3(linear_x, 0, 0)
        vel.angular = Vector3(0, 0, angular_z)


rospy.init_node('topics_quiz_node')

pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rate = rospy.Rate(2)


while not rospy.is_shutdown():

    pub.publish(vel)
    rate.sleep()
    # rospy.spin()
