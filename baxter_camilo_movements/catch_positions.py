#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
rospy.init_node('Catch_Positions')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
right = baxter_interface.Limb('right')
left = baxter_interface.Limb('left')

articulaciones = ['s0', 'e0', 'w0', 'w2', 's1', 'e1', 'w1']
for i in articulaciones:
	continue
	command = 'left_'+i
	current_pos = left.joint_angle(command)
	rad = str(current_pos)
	current_pos = str(current_pos * 57.256)
	print(command+" "+current_pos+" grados")
	print(command+" "+rad+" radianes")
for i in articulaciones:
	command = 'right_'+i
	current_pos = right.joint_angle(command)
	current_pos = str(current_pos)
	print(command+" "+current_pos)

quit()