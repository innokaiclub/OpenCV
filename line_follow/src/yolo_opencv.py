#!/usr/bin/env python

import cv2, cv_bridge, numpy
import numpy as np
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

weight_path = "/home/zimbot/innokai_opencv_ws/src/line_follow/model/yolov3-tiny.weights"
names_path = "/home/zimbot/innokai_opencv_ws/src/line_follow/model/coco.names"
cfg_path = "/home/zimbot/innokai_opencv_ws/src/line_follow/model/yolov3-tiny.cfg"

# Darw a rectangle surrounding the object and its class name
def draw_pred(img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    label = str(classes[class_id])

    color = COLORS[class_id]

    cv2.rectangle(img, (int(x),int(y)), (int(x_plus_w),int(y_plus_h)), color, 2)

    cv2.putText(img, label, (int(x)-10,int(y)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def image_callback(msg):
    image = bridge.imgmsg_to_cv2(msg,'bgr8')
    image=cv2.resize(image, (640, 640))


    blob = cv2.dnn.blobFromImage(image, 1.0/255.0, (640,640), [0,0,0], True, crop=False)
    Width = image.shape[1]
    Height = image.shape[0]
    net.setInput(blob)

    outs = net.forward(getOutputsNames(net))

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4




    for out in outs:
        #print(out.shape)
        for detection in out:
        #each detection  has the form like this [center_x center_y width height obj_score class_1_score class_2_score ..]
            scores = detection[5:]#classes scores starts from index 5
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and classes[class_id] == 'person':
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
                distance = abs(h-y)
                mid =(h+y)/2
                if mid>643:
                    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0.2
                elif mid<637:
                    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -0.2
                else:
                    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
                if distance<400:
                    twist.linear.x = 0.2; twist.linear.y = 0; twist.linear.z = 0
                else:
                    twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
                cmd_vel_pub.publish(twist)


    # apply non-maximum suppression algorithm on the bounding boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    for i in indices:

        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        draw_pred(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))

    # Put efficiency information.
    t, _ = net.getPerfProfile()
    label = 'Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())
    cv2.putText(image, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, .6, (255, 0, 0))

    cv2.imshow("window_title", image)
    cv2.waitKey(10)

# Get names of output layers, output for YOLOv3 is ['yolo_16', 'yolo_23']
def getOutputsNames(net):
    layersNames = net.getLayerNames()
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]



# Load names classes
classes = None
with open(names_path, 'r') as f:
    classes = [line.strip() for line in f.readlines()]
print(classes)

#Generate color for each class randomly
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

# Define network from configuration file and load the weights from the given weights file
net = cv2.dnn.readNet(weight_path,cfg_path)

# Define video capture for default cam
rospy.init_node('yolo')

rospy.sleep(3)
bridge = cv_bridge.CvBridge()
twist = Twist()
image_sub = rospy.Subscriber('/usb_cam/image_raw',Image, image_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel',Twist, queue_size=1)
rospy.spin()
