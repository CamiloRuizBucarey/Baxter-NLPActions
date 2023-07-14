#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
#rospy.init_node('Shake_Hand')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
left = baxter_interface.Limb('left')


current_pos = left.joint_angle('left_w0')
mov_angle = 0.4
for i in range(3):
	delta = (pow(-1, i) * mov_angle)
	command = {'left_w0': current_pos + delta}
	left.move_to_joint_positions(command, timeout = 1.2)
left.move_to_joint_positions({'left_w0': current_pos})

#quit()