#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
#rospy.init_node('Raise_Elbow_Right')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
right = baxter_interface.Limb('right')

pos = right.joint_angle('right_s1')

if pos <= -1.95:
	print("No puedo subir mas el brazo derecho")
else :
	delta = pos - 1.0
	if delta <= -1.95:
		delta = -2.0
	raise_right = {'right_s1': delta}

	right.move_to_joint_positions(raise_right)


#quit()