from smbus import SMBus
import time

class Ultrasonic:
    # Constructor
    def __init__(self, DEVICE_ADDR = 0x70, RANGE_COMMAND = 0x51,INITIATE_READ = 0xE1, I2CBUS = SMBus(1)):
        self.__DEVICE_ADDR = DEVICE_ADDR # Sensor I2C address
        self.__RANGE_COMMAND = RANGE_COMMAND # Range commond byte
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
        value = self.__I2CBUS.read_word_data(self.__DEVICE_ADDR, self.__INITIATE_READ) & 0xFFFF
        range = ((value >> 8) | (value & 0xFF)) 
        return range
            
    # Take a range reading and report last range value
    def take_range_reading(self):
        READING_INTERVAL = 0.100
        if (self.start_sensor() == True):
            time.sleep(READING_INTERVAL)
            return self.read_sensor()
            time.sleep(0.08)
        else:
            return print("Sensor did not start.")
            
            
            
            
            
        