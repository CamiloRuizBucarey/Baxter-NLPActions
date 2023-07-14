#!/usr/bin/env python

import rospy
import baxter_interface

right = baxter_interface.Limb('right')

delta = (right.joint_angle('right_e1') - 1.57) / (1.57 * 2) * (right.joint_angle('right_s1') / 0.5) 
pos = 1.57 - delta
right.move_to_joint_positions({'right_w1': pos})