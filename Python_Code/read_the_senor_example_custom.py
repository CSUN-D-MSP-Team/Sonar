from ultrasonic import Ultrasonic
from smbus import SMBus
import time

# Sensor I2C addresses
DEVICE_ADDR   = 0x70  # Default I2C device address
RANGE_COMMAND = 0x51  # 81 in decimal
INITIATE_READ = 0xE1  # 225 in decimal

# I2C Bus
BUS = 1 # Default I2C bus for raspberry pi
I2CBUS = SMBus(BUS)

# Sleep Intervals
READING_INTERVAL = 0.100
COMMAND_INTERVAL = 0.080

# Main
if __name__ == '__main__':
    sonar = Ultrasonic(DEVICE_ADDR, RANGE_COMMAND, INITIATE_READ, I2CBUS) # Parameterized Constructor
    range = 0
    while(1):
        sonar.start_sensor()
        time.sleep(READING_INTERVAL)
        range = sonar.read_sensor() # Returns int
        print('Range: {} cm'.format(range))
        print('--------------------------')
        time.sleep(COMMAND_INTERVAL)

