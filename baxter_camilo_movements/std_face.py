#!/usr/bin/env python

import rospy
import baxter_interface

import os
import cv2
import cv_bridge

from sensor_msgs.msg import (
    Image,
)

base = "src/baxter_camilo_movements/images/Standard_Face.png"

if not os.access(base, os.R_OK):
    print("No se pudo abrir la imagen 2")
    quit()

img = cv2.imread(base)
msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
pub.publish(msg)
rospy.sleep(1)