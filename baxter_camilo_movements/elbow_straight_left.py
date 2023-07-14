#!/usr/bin/env python

import rospy
import baxter_interface

left = baxter_interface.Limb('left')

#print(left.joint_angle('left_e0'))
left.move_to_joint_positions({'left_e0': -3.0})