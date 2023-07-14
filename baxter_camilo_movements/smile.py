#!/usr/bin/env python

import rospy
import baxter_interface

import os
import cv2
import cv_bridge

from sensor_msgs.msg import (
    Image,
)

path = "src/baxter_camilo_movements/images/Happy_Face.png"

# Image formats are those supported by OpenCv - LoadImage()
if not os.access(path, os.R_OK):
    print("No se pudo abrir la imagen 1")
    quit()

img = cv2.imread(path)
msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
pub.publish(msg)
# Sleep to allow for image to be published.
rospy.sleep(1)