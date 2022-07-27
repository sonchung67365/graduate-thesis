from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
#import cv2
import PIL.Image, PIL.ImageTk
from time import sleep
from threading import Thread
# import RPi.GPIO as GPIO
# import l298
# import uart
import numpy as np
#import ctr_con_XLA as xla
import time
import os.path
#Setup xử lý ảnh -------------
    
#Khoang mau nhan dien diem re
min_mau = np.array([3, 20, 20])#khoang mau  hsv min
max_mau = np.array([27, 225, 225])#khoang mau  hsv max

speed=0

#Bien dem tg
pTime = 0

fps=0

i=int(0)

data_tach='0_0_0_0_0_0'
    
font1 = ('Helvetica', 20,"bold")
font2 = ("Helvetica", 15,"bold")
font3 = ("Helvetica", 11,"bold")
a=520
b=100
# Setups ---------------------

def toc_do_dong_co(var):
    global speed
    speed = int(var)

window = Tk()
window.title("Tkinter GUI")

try :
    #frame = cv2.imread('/home/pi/Desktop/Thanh_code/Data/frame.jpg')
    (canvas_h, canvas_w, _) = frame.shape
except :
    exit()
canvas = Canvas(window, width = canvas_w, height= canvas_h*5 )



label_tocdo=tk.Label(window,text="Tốc độ động cơ :",font=font2).place(x=a,y=b+290)
var=DoubleVar()
scale_tocdodongco= tk.Scale(window,variable=var,command=toc_do_dong_co,orient=HORIZONTAL,length=150).place(x=a+170,y=b+270)

label_doam1 = tk.Label(window,text="Độ ẩm :", font=font2).place(x=a,y=b)
label_nhietdo1 = tk.Label(window,text="Nhiệt độ :", font=font2).place(x=a,y=b+60)
label_trangthaiden1 = tk.Label(window,text="Trạng thái đèn :", font=font2).place(x=a+200,y=b)
label_checkhang = tk.Label(window,text="Hàng :", font=font2).place(x=a+200,y=b-60)
label_pin1 = tk.Label(window,text="Pin :", font=font2).place(x=a+220,y=b+60)
label_canhbaokhoangcach1 = tk.Label(window,text="Cảnh báo khoảng cách :", font=font2).place(x=a,y=b+120)
label_fps = tk.Label(window,text="FPS GUI :",font=font2).place(x=140,y=b+280)

#nhiet_do2
lab_nhietdo2=tk.Label(window,text="0",width=8,bg='light yellow',font=font2)
lab_nhietdo2.place(x=a+100,y=b+60)
#do am2
label_doam2 = tk.Label(window,text = "1",width=8,bg='light yellow',font=font2)
label_doam2.place(x=a+90,y=b)
#trang thai den2
label_trangthaiden2 = tk.Label(window,text="2" ,width=8,bg='light yellow',font=font2)
label_trangthaiden2.place(x=a+360,y=b)
#checkhang2
label_checkhang2 = tk.Label(window,text="2" ,width=8,bg='light yellow',font=font2)
label_checkhang2.place(x=a+300,y=b-60)
#pin2
label_pin2 = tk.Label(window,text="3" ,width=8,bg='light yellow',font=font2)
label_pin2.place(x=a+280,y=b+60)
#khoang cach2
label_canhbaokhoangcach2 = tk.Label(window,text='4',width=8,bg='light yellow',font=font2)
label_canhbaokhoangcach2.place(x=a+270,y=b+120)
#fps2
label_fps2 = tk.Label(window,text='',width=8,bg='light yellow',font=font2)
label_fps2.place(x=240,y=b+280)


v=tk.IntVar()

tk.Label(window, text="Các trạng thái hoạt động :",font=font2).place(x=a,y=b+180)
tk.Radiobutton(window, text="Dò line",variable=v,value=1,font=font2).place(x=a+250,y=b+180)
tk.Radiobutton(window, text="Điều khiển bằng tay",variable=v, value=2,font=font2).place(x=a+250,y=b+210)
tk.Radiobutton(window, text="Khóa",variable=v, value=3,font=font2).place(x=a+250,y=b+240)

def update_frame():
    global canvas, photo, bw, count, speed, pTime, fps, i, data_tach, frame
    
    i = i + 1
    
    #frame = cv2.imread('/home/pi/Desktop/Thanh_code/Data/frame.jpg')
    
    while (type(frame) is not np.ndarray):       

        #frame = cv2.imread('/home/pi/Desktop/Thanh_code/Data/frame.jpg')
    
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Ressize
    frame = cv2.resize(frame, dsize=None, fx=0.75, fy=0.75)
    # Convert hanh image TK
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # Show
    (h, w, _) = frame.shape
    if h < 350:
        canvas.place(x= 10,y= 100)
    else:
        canvas.place(x= 10,y= 10) 
    canvas.create_image(0,0, image = photo, anchor=tk.NW)
            
    if i==1 :data_tach = uart.doc()

    label_doam2.config(text=data_tach[0] +' %')
    lab_nhietdo2.config(text=data_tach[1]+ ' °C')
    if data_tach[2]=='1' : den2='Bật'
    else : den2='Tắt'
    label_trangthaiden2.config(text=den2)
    label_pin2.config(text=data_tach[3]+' V')
    label_canhbaokhoangcach2.config(text=data_tach[4]+ ' cm')
    if data_tach[5]=='1' : cohang2='Có hàng'
    else : cohang2='Không có'
    label_checkhang2.config(text=cohang2)
    label_fps2.config(text = int(fps))
    with open('/home/pi/Desktop/Thanh_code/Data/data_gui.txt', 'w') as wf:
        wf.write(str(speed)+'_'+data_tach[5])
    if i==6 :
        i=0
        #Hien thi so khung hinh tren giay
        cTime = time.time()
        fps = 6 / (cTime - pTime)
        pTime = cTime
        
    window.after(1,update_frame)
 
update_frame()

window.geometry('1000x440')
window.mainloop()


