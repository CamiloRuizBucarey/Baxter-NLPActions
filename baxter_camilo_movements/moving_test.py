#!/usr/bin/env python

import rospy
import baxter_interface

# Inicializa el "nodo" ROS y lo registra "with the Master"
rospy.init_node('Moving_Test')

# Crear instancias de la clase Limb(miembro/extremidad) de baxter_interface
left = baxter_interface.Limb('left')
right = baxter_interface.Limb('right')


#Crea estructuras con la "posicion de descanso" de los brazos del baxter
rest_left = {'left_s0': -0.08, 'left_s1': -1.00, 'left_w0': 0.67, 'left_w1': 1.03, 'left_w2': -0.50, 'left_e0': -1.18, 'left_e1': 1.94}
rest_right = {'right_s0': 0.08, 'right_s1': -1.00, 'right_w0': -0.67, 'right_w1': 1.03, 'right_w2': 0.50, 'right_e0': 1.18,'right_e1': 1.94}


# Mueve los brazos a la posicion de descanso
left.move_to_joint_positions(rest_left)
right.move_to_joint_positions(rest_right)

test_left = {'left_s0': 0.70, 'left_s1': 1.00, 'left_e0': -1.80, 'left_e1': 1.00, 'left_w0': 1.0, 'left_w1': 1.50, 'left_w2': 0.00}
test_right = {'right_s0': -0.5, 'right_s1': 0.00, 'right_w0': -0.67, 'right_w1': 0.53, 'right_w2': 0.50, 'right_e0': 0.50,'right_e1': 0.00}
#left.move_to_joint_positions(test_left)
#right.move_to_joint_positions(test_right)

#left.move_to_joint_positions({'left_w1': 1.41})


#**************** APUNTA BRAZO AL CIELO *************************
#pos = left.joint_angle('left_s1')
#moveto = -1.6 + pos

#left.move_to_joint_positions({'left_w0': moveto})

#****************************************************************





comando = {'left_e0': -3.00}
com = {'left_e1': 1.00}
#left.move_to_joint_positions(comando)
#left.move_to_joint_positions(com)

# Imagino que cierra el programa y termina la ejecucion del movimiento
quit()