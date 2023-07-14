#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
#rospy.init_node('Raise_Hand')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
left = baxter_interface.Limb('left')


#************ GIRAR BRAZO PARA ARRIBA ************
pos = left.joint_angle('left_s1')
moveto = -1.6 + pos
#left.move_to_joint_positions({'left_w0': moveto})


#*********** GIRAR MUNHECA PARA ARRIBA ***********

#if abs(left.joint_angle('left_s1'))%1.57 < 0.05 or (1.57 - abs(left.joint_angle('left_e1')%1.57) < 0.05):
if abs(left.joint_angle('left_e0')) >= 2.7:
	delta = (left.joint_angle('left_e1') - 1.57) / (1.57 * 2) * (left.joint_angle('left_s1') / 0.5) 
	movedelta = 1.57 - delta
	left.move_to_joint_positions({'left_w0': 0.0, 'left_w1': 0.6})
else:
	delta = (left.joint_angle('left_e1') - 1.57) / (1.57 * 2) * (left.joint_angle('left_s1') / 0.5) 
	movedelta = 1.57 - delta
	#print("w1 se mueve a: " + str(pos))
	left.move_to_joint_positions({'left_w0': moveto, 'left_w1': movedelta})

#*************************************************
'''
while 1:
	pos = left.joint_angle('left_s1')
	e1 = left.joint_angle('left_e1')
	moveto = -1.6 + pos
	delta = (left.joint_angle('left_e1') - 1.57) / (1.57 * 2) * (left.joint_angle('left_s1') / 0.5) 
	movedelta = 1.57 - delta
	left.move_to_joint_positions({'left_w0': moveto, 'left_w1': movedelta})
	if (pos >= left.joint_angle('left_s1') - 0.05 and pos <= left.joint_angle('left_s1') + 0.05 ) and (e1 >= left.joint_angle('left_e1') - 0.05 and e1 <= left.joint_angle('left_e1') + 0.05):
		break		# condicion de salida -> ha dejado de moverse
'''
#quit()