#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
#rospy.init_node('Raise_Elbow_Left')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
left = baxter_interface.Limb('left')


pos = left.joint_angle('left_s1')

if pos <= -1.95:
	print("No puedo subir mas el brazo izquierdo")
else :
	delta = pos - 1.0
	if delta <= -1.95:
		delta = -2.0
	raise_left = {'left_s1': delta}

	left.move_to_joint_positions(raise_left)

#quit()