#!/usr/bin/env python

import rospy
import baxter_interface

right = baxter_interface.Limb('right')

pos = right.joint_angle('right_s0')

if pos >= 0.75:
	print("No puedo adelantar mas el hombro derecho")
else :
	delta = pos + 0.40
	if delta >= 0.75:
		delta = 0.8
	raise_right = {'right_s0': delta}
	right.move_to_joint_positions(raise_right)