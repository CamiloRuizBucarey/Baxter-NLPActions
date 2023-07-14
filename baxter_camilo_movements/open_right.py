#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
#rospy.init_node('Open_Arms')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
right = baxter_interface.Limb('right')
'''
left = baxter_interface.Limb('left')

open_left = {'left_s0': 0.5, 'left_s1': 0.00, 'left_w0': 0.00, 'left_w1': 0.00, 'left_w2': 0.00, 'left_e0': 0.00, 'left_e1': 0.00}
left.move_to_joint_positions(open_left)
'''
open_right = {'right_s0': -0.5, 'right_s1': 0.00, 'right_w0': 0.00, 'right_w1': 0.00, 'right_w2': 0.00, 'right_e0': 0.00,'right_e1': 0.00}
right.move_to_joint_positions(open_right)

#quit()