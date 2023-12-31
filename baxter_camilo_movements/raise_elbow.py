#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
rospy.init_node('Raise_Elbow')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
right = baxter_interface.Limb('right')
left = baxter_interface.Limb('left')

flag = True

if flag:
	raise_left = {'left_s0': 0.30, 'left_s1': 0.00, 'left_e0': -1.80, 'left_e1': 1.00, 'left_w0': 1.0, 'left_w1': 0.00, 'left_w2': 0.00}
	left.move_to_joint_positions(raise_left)

else:
	raise_right = {'right_s0': -0.7, 'right_s1': 1.00, 'right_e0': 1.80,'right_e1': 1.00, 'right_w0': -1.0, 'right_w1': 0.00, 'right_w2': 0.00}
	right.move_to_joint_positions(raise_right)

quit()