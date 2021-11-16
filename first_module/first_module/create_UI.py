import  time
import cv2 as cv
import tkinter as Tk
from PIL import Image, ImageTk


#video size
video_width = 600
video_height =480

class create_UI:
    def __init__(self):
        #Create UI
        self.UI = Tk.Tk()
        self.UI.geometry("1020x600")
        self.UI.resizable(False, False)

        # Sensor data labeling
        temp = Tk.Label(self.UI, text = "Temperature")
        temp.place(x=700,y=50)
        humi = Tk.Label(self.UI, text = "Humidity")
        humi.place(x=700,y=80)
        wave = Tk.Label(self.UI, text = "Ultrasonic wave")
        wave.place(x=700,y=110)
        
        # Sensor data value labeling
        self.var_temp = Tk.StringVar()
        self.var_humi = Tk.StringVar()
        self.var_wave = Tk.StringVar()
        self.var_temp.set("Temperature")
        self.var_humi.set("Humidity")
        self.var_wave.set("Ultrasonic wave")

        val_temp = Tk.Label(self.UI, textvariable = self.var_temp)
        val_humi = Tk.Label(self.UI, textvariable = self.var_humi)
        val_wave = Tk.Label(self.UI, textvariable = self.var_wave)
        val_temp.place(x=800,y=50)
        val_humi.place(x=800,y=80)
        val_wave.place(x=800,y=110)

        #Video labeling
        self.cap = cv.VideoCapture(0)
        self.font = cv.FONT_HERSHEY_SIMPLEX 
        self.face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') #Face detect
        self.body_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')            #Body detect
        stream_L = Tk.Label(self.UI, text = "STREAMING")
        stream_L.grid(row = 0, column = 0)

        stream_frm = Tk.Frame(self.UI, bg = 'white', width = video_width, height = video_height)
        stream_frm.grid(row = 1, column = 0)

        self.video_lbl = Tk.Label(stream_frm)
        self.video_lbl.grid()
        self.video_play()
    
    #update data values
    def set_data(self, object):
        self.var_temp.set(object.t)
        self.var_humi.set(object.h)
        self.var_wave.set(object.w)
        self.UI.update()
        
    #play video on UI
    def video_play(self):
        ret, frame = self.cap.read()
        if not ret:
            self.cap.release()
            return
        #frame = cv.flip(frame, 0) #뒤집기
        frame = cv.resize(frame, dsize=(600,480), interpolation=cv.INTER_AREA)
        face = self.face_cascade.detectMultiScale(frame,1.8,1,0,(30,30))
        body = self.body_cascade.detectMultiScale(frame,1.8,1,0,(30,30))
        #print("Number of body, face detected: " + str(len(body)) + ',' + str(len(face)))
        for (x,y,w,h) in body:
            cv.rectangle(frame, (x,y),(x+w+10,y+h+10),(255,0,0),3,4,0) #물체표시 사각형
            cv.putText(frame,'Detected human',(x-5,y-5),self.font,0.9,(255,255,0),2) #물체표시 글

        if len(body) == 0:
            for (x,y,w,h) in face:
                cv.rectangle(frame, (x,y),(x+w+10,y+h+10),(255,0,0),3,4,0) #물체표시 사각형
                cv.putText(frame,'Detected human',(x-5,y-5),self.font,0.9,(255,255,0),2) #물체표시 
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.video_lbl.imgtk = imgtk
        self.video_lbl.configure(image=imgtk)
        self.video_lbl.after(10,self.video_play)
      

if __name__ == '__main__':
    UI = create_UI()     
