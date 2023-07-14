#!/usr/bin/env python

import rospy
import baxter_interface

left = baxter_interface.Limb('left')

e1 = left.joint_angle('left_e1')

delta = (left.joint_angle('left_e1') - 1.57) / (1.57 * 2) * (left.joint_angle('left_s1') / 0.5) 
pos = 1.57 - delta
left.move_to_joint_positions({'left_w1': pos})