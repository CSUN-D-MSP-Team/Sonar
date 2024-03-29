#----------------------------------------
#Engineer: Michael Granberry
#Project: ARCS Smart Pallet
#Device: Ultrasonic Sensor
#Model: I2C MaxSonar EZ Series - MB1212
#Program: ROS Publisher Node for Sonar-0x72
#Last Modified Date: Oct 23, 2022
#----------------------------------------

#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from sonar import Sonar

def sonar_talker():
	pub = rospy.Publisher('sonar0x72_range_topic', Int32, queue_size=10) # publisher object
	rospy.init_node('sonar0x72_publisher_node', anonymous=True) # initialize publisher node
	rate = rospy.Rate(10) # ros rate
	rospy.loginfo("Ros sonar node now publishing.")
	s = Sonar(0x72)
	while not rospy.is_shutdown():
		rangeValue = s.read_range()
		rospy.loginfo(rangeValue)
		pub.publish(rangeValue)
		rate.sleep()

if __name__ == "__main__":
	try:
		sonar_talker()
	except rospy.ROSInterruptException:
		pass
