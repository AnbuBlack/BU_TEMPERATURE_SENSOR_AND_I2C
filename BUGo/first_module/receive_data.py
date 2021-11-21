import serial
import time


class sensor:
    
    def __init__(self, port, b_rate):    
        self.t=0                        #temperature
        self.h=0                        #humidity
        self.w = False                  #PIR
        self.port =port                 #Arduino port
        self.b_rate = b_rate            #baudrate        
        
    def read_data(self):
        seri = serial.Serial(self.port, baudrate = self.b_rate, timeout = None)   #Read data at Arduino
        
        #read data from arduino
        while True:
            sensor=seri.readline().rstrip().decode()        #Decode received data from Arduino


            #Split sensor data
            self.w=sensor[:1]
            if self.w == '0':               #If detected trigger from PIR, change 'w' value 'Yes' to 'No or 'No' to 'Yes' 
                self.w = False
            elif self.w == '1':
                self.w = True
            print(self.w)
            self.h =sensor[1:4]
            print(self.h)
            self.t=sensor[4:]
            print(self.t)
            time.sleep(3)


if __name__ == "__main__":
    a = sensor("/dev/ttyACM0", 9600)

    a.read_data()
