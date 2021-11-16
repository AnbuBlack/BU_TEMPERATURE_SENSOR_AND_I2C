#Library modules
from tkinter import *
import threading
import time

# other mudules
import receive_data
import create_UI
import record_data


#Arduino
port = 'COM3'
b_rate = 9600

#SQL Server information
my_host='127.0.0.1'
my_user = 'admin'
my_passwd = 'root'
my_db = 'raspi_db'
my_port = 3306


def main():
    #Create instance
    receive_obj = receive_data.sensor(port, b_rate)       #data receive instance
    record_obj = record_data.record_data(my_host, my_user, my_passwd, my_db, my_port)     #MariaDB SQL instance
    UI = create_UI.create_UI()      #UI instance
    
    
    #gathering data thread start
    sensor_thread = threading.Thread(target = receive_obj.read_data)
    sensor_thread.start()



    while True:
        UI.set_data(receive_obj)                      #Set data at UI
        record_obj.record_data(receive_obj)        #Enter data into MariaDB
        time.sleep(3)                                  #for delay


if __name__ == "__main__":
    main()
