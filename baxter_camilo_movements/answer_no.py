#!/usr/bin/env python

import rospy
import baxter_interface

import os
import cv2
import cv_bridge

from sensor_msgs.msg import (
    Image,
)

# Inicializa el "nodo" ROS y lo registra "with the Master"
rospy.init_node('Answer_No')

head = baxter_interface.Head()

base = "src/baxter_camilo_movements/images/Standard_Face.png"
path = "src/baxter_camilo_movements/images/Angry_Face.png"

if not os.access(path, os.R_OK):
    print("No se pudo abrir la imagen")
    quit()

img = cv2.imread(path)
msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
pub.publish(msg)
# Sleep to allow for image to be published.
rospy.sleep(1)

angles = [-0.5, 0.5]
for i in range(4):
	head.set_pan(angles[i%2], speed = 0.1)


head.set_pan(0.0, speed=0.2, timeout=0.5)

if not os.access(path, os.R_OK):
    print("No se pudo abrir la imagen")
    quit()

img = cv2.imread(base)
msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
pub.publish(msg)
rospy.sleep(1)

quit()