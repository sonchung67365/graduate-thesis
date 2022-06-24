import serial
from time import sleep




class Uart():
    def __init__(self):
        while True:
            try:
                self.ser = serial.Serial(
                    port='/dev/ttyACM0',
                    baudrate=9600,
                    timeout=1.0
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
        Uart.__init__(self)
    
    def get_data_merge(self):
        while self.ser.in_waiting < 20:
            return Uart.get_data(self)

    def get_data_split(self):
        data = self.ser.readline().decode('utf-8').rstrip()
        while len(data) < 20:
            data = self.ser.readline().decode('utf-8').rstrip()
        self.ser.reset_input_buffer()
        return data





