#!/usr/bin/env python

import rospy
import baxter_interface

left = baxter_interface.Limb('left')

pos = left.joint_angle('left_s0')

if pos <= -0.75:
	print("No puedo adelantar mas el hombro izquierdo")
else :
	delta = pos - 0.40
	if delta <= -0.75:
		delta = -0.8
	raise_left = {'left_s0': delta}

	left.move_to_joint_positions(raise_left)