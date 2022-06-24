import serial
from time import sleep




class Uart():
    def __init__(self, port, baudrate, timeout=1.0):
        while True:
            try:
                self.ser = serial.Serial(
                    port,
                    baudrate,
                    timeout
                )
                print("Successfully connected to Serial.")
                sleep(0.5)
                self.ser.reset_input_buffer()
                print("Reset input buffer.")
                print("Start to receive from Arduino")
                break
            except serial.SerialException:
                print("Could not connect to Serial. Trying again.")
                sleep(1)

    def get_data(self):
        self.ser.reset_input_buffer() # Reset input buffer
        return self.ser.readline().decode('utf-8').rstrip()


    def get_inWaiting(self):
        #ser.reset_input_buffer()
        return self.ser.inWaiting()





class Arduino(Uart):
    def __init__(self):
        Uart.__init__(self,'/dev/ttyACM0',9600)
    
    def get_data_merge(self):
        if self.ser.in_waiting > 18:
            return Uart.get_data(self)

    def get_data_split(self):
        return self.get_data_merge().split('_')

    def get_data_humi(self):
        return self.get_data_split()[0]

    def get_data_temp(self):
        return self.get_data_split()[1]

    def get_data_lamp(self):
        return self.get_data_split()[2]
    
    def get_data_vol(self):
        return self.get_data_split()[3]

    def get_data_distance(self):
        return self.get_data_split()[4]





