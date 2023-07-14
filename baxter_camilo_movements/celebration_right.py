#!/usr/bin/env python

import rospy
import baxter_interface

right = baxter_interface.Limb('right')

aux = -1
s1 = right.joint_angle('right_s1')
e1 = right.joint_angle('right_e1')
delta = 0.5
deltae = 0.3
for i in range(5):
	right.move_to_joint_positions({'right_s1': s1 + delta*(aux*(i%2)), 'right_e1': e1 + deltae*(aux*(i%2))})