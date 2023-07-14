#!/usr/bin/env python

import rospy
import baxter_interface

left = baxter_interface.Limb('left')

aux = -1
s1 = left.joint_angle('left_s1')
e1 = left.joint_angle('left_e1')
delta = 0.5
deltae = 0.3
for i in range(5):
	left.move_to_joint_positions({'left_s1': s1 + delta*(aux*(i%2)), 'left_e1': e1 + deltae*(aux*(i%2))})