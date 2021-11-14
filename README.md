# Sonar

### read_the_senor_example_default.py
* Reads a range reading from default I2C bus and device address.
```python
from MaxSonar import Ultrasonic

# Main
if __name__ == '__main__':
    sonar = Ultrasonic() # Default Constructor
    range = 0
    while(1):
        range = sonar.take_range_reading() # Returns int
        print('Range: {} cm'.format(range))
        print('--------------------------')

```
### read_the_senor_example_custom.py
* Reads a range reading from a user defined I2C bus and device address.
```python

from MaxSonar import Ultrasonic
from smbus import SMBus
import time

# Sensor I2C addresses
DEVICE_ADDR   = 0x70  # Default I2C device address: 0x70 = 112 in decimal
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

```

### MaxSonar.py Class
```python
from smbus import SMBus
import time

class Ultrasonic:
    # Constructor
    def __init__(self, DEVICE_ADDR = 0x70, RANGE_COMMAND = 0x51,INITIATE_READ = 0xE1, I2CBUS = SMBus(1)):
        self.__DEVICE_ADDR = DEVICE_ADDR # Sensor I2C address
        self.__RANGE_COMMAND = RANGE_COMMAND # Range command byte
        self.__INITIATE_READ = INITIATE_READ # Initiate a read at the sensor address
        self.__I2CBUS = I2CBUS # I2C Bus
    
    # Take a range reading
    def start_sensor(self):
        try:
            self.__I2CBUS.write_byte(self.__DEVICE_ADDR, self.__RANGE_COMMAND)
            return True
        except IOError as e:
            print("IOError: {0}".format(e))
            return False
        
    # Report the last range value
    def read_sensor(self):
        try:
            val = self.__I2CBUS.read_word_data(self.__DEVICE_ADDR, self.__INITIATE_READ)
            range = ((val >> 8) & 0xff | (val & 0xff))
            return range
        except IOError as e:
            print("IOError: {0}".format(e)) 
            
    # Take a range reading and report last range value
    def take_range_reading(self):
        READING_INTERVAL = 0.100
        if (self.start_sensor() == True):
            time.sleep(READING_INTERVAL)
            return self.read_sensor()
        else:
            return print("Sensor did not start.")
```




