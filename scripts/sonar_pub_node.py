#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from smbus2 import SMBus #I2C
from datetime import datetime #Date
import time #Delay

i2cAddr = 0x72 #Sensor i2c address

writeRangeCmd = 0x51 #Write range Command. 81 in decimal
initRead = 0xe1 #Initiate read. 225 in decimal

delay1 = 0.08 #80ms
delay2 = 0.10 #100ms

def sonar_talker():
	pub = rospy.Publisher('sonar_range_topic', Int32, queue_size=10) # publisher object
	rospy.init_node('sonar_publisher_node', anonymous=True) # initialize publisher node
	#rate1 = rospy.Rate(12) # ros rate1
	rate2 = rospy.Rate(10) # ros rate2
	rospy.loginfo("Ros sonar node now publishing.")
	while not rospy.is_shutdown():
	    try:
		i2cbus = SMBus(1)
		i2cbus.write_byte_data(i2cAddr, 0, writeRangeCmd) #Write the range command byte.
		rate1.sleep()
		rawData = i2cbus.read_word_data(i2cAddr, initRead) #Initiate a read at the sensor address. Word = 2bytes.
		rangeValue = (rawData >> 8) & 0xff #Right shift 8-bits. Mask with 0x00ff.
		rospy.loginfo(rangeValue)
		pub.publish(rangeValue)
		
	    except IOError as err:
		print(err)
	    rate2.sleep()

if __name__ == "__main__":
	try:
		sonar_talker()
	except rospy.ROSInterruptException:
		pass
