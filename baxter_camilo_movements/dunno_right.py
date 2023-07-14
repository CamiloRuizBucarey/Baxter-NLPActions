#!/usr/bin/env python

import rospy
import baxter_interface

right = baxter_interface.Limb('right')

e1 = right.joint_angle('right_e1')
w1 = right.joint_angle('right_w1')

right.move_to_joint_positions({'right_e1': e1 + 0.7, 'right_w1': w1 - 1.5})