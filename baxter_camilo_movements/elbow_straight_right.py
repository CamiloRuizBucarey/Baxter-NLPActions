#!/usr/bin/env python

import rospy
import baxter_interface

right = baxter_interface.Limb('right')

#print(right.joint_angle('right_e0'))
right.move_to_joint_positions({'right_e0': 3.0})