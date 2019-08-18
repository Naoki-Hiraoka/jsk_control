#!/usr/bin/env python

import rospy
import rosbag
from robot_calibration_msgs.msg import CaptureConfig

outname = "calibration_poses.bag"
outbag = rosbag.Bag(outname,"w")
try:
    topic = "calibration_joint_states"
    msg = CaptureConfig()
    msg.joint_states.name = ["RLEG_JOINT0", "RLEG_JOINT1","RLEG_JOINT2", "RLEG_JOINT3", "RLEG_JOINT4", "RLEG_JOINT5", "RLEG_JOINT6", "LLEG_JOINT0", "LLEG_JOINT1", "LLEG_JOINT2", "LLEG_JOINT3", "LLEG_JOINT4", "LLEG_JOINT5", "LLEG_JOINT6", "CHEST_JOINT0", "CHEST_JOINT1", "HEAD_JOINT0", "HEAD_JOINT1", "RARM_JOINT0", "RARM_JOINT0", "RARM_JOINT0", "RARM_JOINT0", "RARM_JOINT0", "RARM_JOINT0", "RARM_JOINT0", "RARM_JOINT0", "RARM_JOINT1", "RARM_JOINT2", "RARM_JOINT3", "RARM_JOINT4", "RARM_JOINT5", "RARM_JOINT6", "RARM_JOINT7", "LARM_JOINT0", "LARM_JOINT1", "LARM_JOINT2", "LARM_JOINT3", "LARM_JOINT4", "LARM_JOINT5", "LARM_JOINT6", "LARM_JOINT7"]
    t = rospy.Time()
    secs = 0

    #LARM_0000
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, -0.393004, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -2.08742, 0.255902, -1.27087, -0.377018, -1.44134, -0.114052, -0.77831, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0001
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.392547, -0.393004, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.13497, 0.159088, -0.685639, -1.34356, -1.37642, -0.632583, 1.102, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0002
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, -0.393004, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.962793, 0.32336, -0.47952, -1.65398, -1.03553, -0.217919, 0.894181, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0003
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, -0.393004, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.93347, 1.23218, -1.11789, -1.2903, -1.71478, -0.41231, -0.567245, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0004
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, -0.131204, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -2.2897, 0.227219, -1.59258, -0.764436, -1.84132, -0.400377, -1.38733, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0005
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, -0.131204, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.63762, 0.723421, -1.21202, -1.4132, -1.5045, -0.583356, -0.401969, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0006
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, -0.131204, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.896956, -0.137729, -0.700202, -1.49937, -0.680479, -0.501081, 0.932049, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0007
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, -0.131204, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.28722, -0.174533, -1.10353, -0.906383, -0.518896, -0.544516, 1.4298, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0008
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, -0.131204, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.37861, 0.246856, -1.10099, -0.686575, -1.24904, -0.220753, 0.146218, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0009
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.392547, -0.131204, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.15526, 0.807053, -0.912938, -1.30452, -1.24991, -0.499849, 0.177389, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0010
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, -0.131204, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, 0.430582, 1.31669, 0.688618, -2.2393, -0.947636, -0.893449, 0.356266, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0011
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, -0.131204, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.621, 1.21126, -0.537617, -1.63644, -1.27308, -0.606472, 0.594937, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0012
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.130595, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, 0.619567, 1.29979, 1.10617, -2.05113, -1.7881, -0.559361, -0.991338, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0013
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.130595, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, 0.736765, 1.19889, 0.3991, -2.29569, -1.21621, -0.834169, 0.725553, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0014
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.130595, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, 0.229775, 0.66617, -0.115095, -2.26524, -1.18863, -0.771006, 0.805528, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0015
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.130595, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, 0.060782, 0.327111, -0.304242, -2.05557, -1.12777, -0.308696, 0.792446, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0016
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.130595, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.304904, 0.169746, -0.24576, -1.79977, -0.862029, -0.739273, 1.22259, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0017
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.130595, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.626629, 1.05717, -0.561392, -2.1098, 0.547606, -0.480967, 1.41318, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0018
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.471616, 0.61928, -0.927041, -1.82467, -1.21298, -0.800909, 0.390651, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0019
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.51929, 0.636692, -1.56024, -1.42628, -1.31806, -1.02263, -0.799073, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0020
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.52785, -0.125537, -1.09453, -0.910063, -0.672212, 0.319086, 0.712986, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0021
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.04729, 0.553816, -1.27346, -1.01486, -1.50082, -0.295444, -0.2806, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0022
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.392547, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, 0.070364, 0.411039, -0.618595, -1.95241, -1.2546, -0.650381, 0.836969, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0023
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.392547, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -1.43311, 1.09693, -1.532, -1.42892, -1.85005, -0.067265, -0.455239, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0024
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.392547, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.158497, -0.110795, -0.61462, -1.66354, -0.852774, -0.574945, 1.33848, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0025
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, 0.490082, 0.404214, -0.330013, -2.0954, -1.60314, -0.724586, 0.985204, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0026
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.392394, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.097255, 0.067637, -0.409025, -1.20066, -1.33228, -0.151279, 1.227, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0027
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.130747, 0.654194, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.349049, 0.435595, -1.08836, -1.21472, -1.23682, -0.38409, 0.317196, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0028
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.392547, 0.654194, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, -0.121059, 0.801047, -0.918908, -1.50989, -1.23019, -0.421624, 0.3093, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #LARM_0029
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, 0.654346, 0.654194, 0.174533, -0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, 0.261799, 0.586632, 0.410333, -0.465496, -2.12325, -0.700211, -0.459314, 0.897238, -0.261799]
    msg.features = ["larm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0000
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, -0.393004, -1.19043, -0.469419, 0.481687, -1.14438, 1.08571, 0.190347, 0.920345, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0001
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, -0.393004, -1.84945, -1.07435, 1.1252, -1.78835, -0.624125, 0.55607, 1.41599, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0002
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.523903, -0.393004, -1.51038, -0.44527, 0.790897, -1.02125, 0.943601, 0.810565, 0.641055, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0003
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, -0.393004, -1.82571, -0.203578, 0.841043, -0.948812, 0.545115, 1.34638, 0.480874, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0004
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, -0.393004, -2.01251, -0.026119, 1.08615, -0.302681, 0.906806, 1.00539, -0.131669, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0005
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, -0.131204, -0.728497, -0.420804, 0.36028, -1.27567, 1.25022, 0.373353, 1.20532, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0006
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, -0.131204, -0.465659, -0.794003, 0.26907, -1.59478, 0.805473, 0.173658, 0.604485, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0007
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, -0.131204, -1.18523, -1.2306, 0.775788, -1.77386, -0.525336, 0.737966, 1.23084, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0008
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, -0.131204, -1.42076, -0.277928, 0.95862, -0.740435, 0.909663, 0.64774, 0.035063, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0009
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, -0.131204, -1.72533, -0.170846, 1.34699, -0.778929, 0.911805, 1.31636, 0.255137, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0010
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.130595, -1.06313, 0.108795, 1.03583, -0.480634, 0.864847, 0.475734, 0.981197, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0011
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.130595, -1.08037, -0.141565, 0.946782, -0.323066, 0.997656, -0.06209, -0.090422, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0012
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.130595, -1.22671, -0.451609, 1.20454, -1.04125, 1.22261, 0.881797, 0.086132, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0013
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, 0.392394, 0.114689, -0.690259, 0.42466, -1.33259, 0.808063, -0.086797, 0.384228, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0014
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, 0.392394, 0.252235, -0.85692, 0.246333, -1.78903, 0.470493, 0.474561, 0.621987, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0015
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, 0.392394, 0.047588, -1.01898, 0.215901, -1.96139, -0.311128, 0.861366, 1.15402, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0016
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.392394, -0.631172, -0.434432, 1.07156, -1.44708, 1.20059, 1.0939, 0.756912, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0017
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.392394, -0.849272, -0.647737, 1.06983, -1.12287, 1.21113, 0.412442, -0.342195, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0018
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.392394, -0.708832, 0.122678, 0.95915, -0.705307, 0.531485, 0.207524, 0.902156, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0019
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.392394, -0.776144, 0.116317, 0.767161, -0.96503, 0.166266, 0.644036, 1.29119, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0020
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.392394, -0.706399, -0.407891, 0.924301, -1.14607, 0.813249, 0.74024, 0.199062, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0021
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.392394, -0.80598, -0.299154, 1.23887, -0.57658, 1.41472, 0.124882, 0.446606, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0022
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.392394, -0.964066, -0.397541, 1.14182, -0.549822, 1.2401, 0.116606, -0.423536, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0023
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, 0.654194, 0.456031, -0.317991, 0.451837, -1.8544, 0.837053, 0.607875, 1.11288, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0024
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.785398, 0.654194, 0.182589, -0.345861, 0.638116, -1.06008, 1.03464, -0.134592, 0.750946, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0025
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.523903, 0.654194, 0.024618, -0.386889, 0.662114, -1.39831, 0.648112, 0.39708, 0.543244, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0026
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.523903, 0.654194, -1.05617, -0.783118, 1.53941, -1.45312, 0.982935, 1.40843, -0.363854, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0027
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.654194, -0.723311, -0.674854, 1.1843, -1.48193, 1.08912, 1.05306, -0.25099, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0028
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.654194, -1.00722, -0.492362, 1.31774, -1.43869, 0.239958, 1.58825, 0.453647, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

    #RARM_0029
    t = rospy.Time()
    t.secs = secs
    secs += 1
    msg.joint_states.position = [0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.453786, 0.872665, -0.418879, 0.0, 0.0, 0.0, 0.0, -0.262104, 0.654194, -0.285092, -0.101029, 0.641512, -1.30615, 0.29411, 0.887841, 0.850442, 0.261799, 0.174533, 0.174533, 0.0, -0.436332, 0.0, 0.0, -0.174533, -0.261799]
    msg.features = ["rarm_checkerboard_finder"]
    outbag.write(topic,msg,t)

finally:
    outbag.close()
