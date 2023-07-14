#!/usr/bin/env python

import rospy
import baxter_interface

left = baxter_interface.Limb('left')

e1 = left.joint_angle('left_e1')
w1 = left.joint_angle('left_w1')

left.move_to_joint_positions({'left_e1': e1 + 0.7, 'left_w1': w1 - 1.5})
