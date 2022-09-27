#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talk_to_me():
	pub = rospy.Publisher('talking_topic', Int32, queue_size=10) # publisher object
	rospy.init_node('publisher_node', anonymous=True) # initialize publisher node
	rate = rospy.Rate(1) # ros rate1
	rospy.loginfo("Ros sonar node now publishing.")
	while not rospy.is_shutdown():
		msg = "Hey - s%" % rospy.get_time()
		pub.publish(msg)
		rate.sleep()

if __name__ == "__main__":
	try:
		sonar_talker()
	except rospy.ROSInterruptException:
		pass
