

if abs(right.joint_angle('right_s1'))%1.57 < 0.05 or (1.57 - abs(right.joint_angle('right_e1')%1.57) < 0.05):
	right.move_to_joint_positions({'right_w1': 1.57})

delta = (right.joint_angle('right_e1') - 1.57) / (1.57 * 2) * (right.joint_angle('right_s1') / 0.5) 
pos = 1.57 - delta
#print("w1 se mueve a: " + str(pos))
right.move_to_joint_positions({'right_w1': pos})