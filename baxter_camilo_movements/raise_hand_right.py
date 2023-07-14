#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
#rospy.init_node('Raise_Hand')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
right = baxter_interface.Limb('right')
#left = baxter_interface.Limb('left')

#flag = True
'''
if flag:
	#************ GIRAR BRAZO PARA ARRIBA ************
	pos = left.joint_angle('left_s1')
	moveto = -1.6 + pos
	left.move_to_joint_positions({'left_w0': moveto})

	#*********** GIRAR MUNHECA PARA ARRIBA ***********
	if abs(left.joint_angle('left_s1'))%1.57 < 0.05 or (1.57 - abs(left.joint_angle('left_e1')%1.57) < 0.05):
		left.move_to_joint_positions({'left_w1': 1.57})

	delta = (left.joint_angle('left_e1') - 1.57) / (1.57 * 2) * (left.joint_angle('left_s1') / 0.5) 
	pos = 1.57 - delta
	#print("w1 se mueve a: " + str(pos))
	left.move_to_joint_positions({'left_w1': pos})
	#*************************************************

else:
'''
#************ GIRAR BRAZO PARA ARRIBA ************
pos = right.joint_angle('right_s1')
moveto = 1.6 - pos
#right.move_to_joint_positions({'right_w0': moveto})

#*********** GIRAR MUNHECA PARA ARRIBA ***********
if abs(right.joint_angle('right_e0')) >= 2.7:
	delta = (right.joint_angle('right_e1') - 1.57) / (1.57 * 2) * (right.joint_angle('right_s1') / 0.5) 
	movedelta = 1.57 - delta
	right.move_to_joint_positions({'right_w0': 0.0, 'right_w1': 0.6})
else:
	delta = (right.joint_angle('right_e1') - 1.57) / (1.57 * 2) * (right.joint_angle('right_s1') / 0.5) 
	movedelta = 1.57 - delta
	#print("w1 se mueve a: " + str(pos))
	right.move_to_joint_positions({'right_w0': moveto, 'right_w1': movedelta})
'''
#*************************************************

while 1:
	pos = right.joint_angle('right_s1')
	e1 = right.joint_angle('right_e1')
	moveto = 1.6 - pos
	delta = (right.joint_angle('right_e1') - 1.57) / (1.57 * 2) * (right.joint_angle('right_s1') / 0.5) 
	movedelta = 1.57 - delta
	right.move_to_joint_positions({'right_w0': moveto, 'right_w1': movedelta})
	if (pos >= right.joint_angle('right_s1') - 0.05 and pos <= right.joint_angle('right_s1') + 0.05 ) and (e1 >= right.joint_angle('right_e1') - 0.05 and e1 <= right.joint_angle('right_e1') + 0.05):		break
'''
#quit()