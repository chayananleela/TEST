from tkinter import *
import tkinter as tk
from tkinter.constants import COMMAND
import tkinter.font as tkFont
import time as tm
from datetime import datetime

print("arm")

class App:

    def __init__(self, root):
        #setting title
        root.title("คัดกรองบุคคลผ่าน เข้า-ออก")
        #setting window size
        width=1280
        height=720
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        #root.configure(background='#FFFF33')
        root.resizable(width=False, height=False)

        img = PhotoImage(file='bg_screen FramePict-2.png')
        w = img.width()
        h = img.height()
        cv = Canvas(width=w, height=h)
        cv.create_image(1, 2, anchor=NW, image=img)
        cv.image = img
        cv.place(x=1, y=1)

        current_datetime = tm.strftime('%m/%d/%Y')
        lb_clock = tk.Label(root, font='Mitr 18', fg='#484747', background='#d6b7d7', text=current_datetime)
        lb_clock.place(x=40, y=40, width=150, height=30)
        #clock_label.grid(row=0,column=0)

        lb_clock2 = Label(font='Mitr 18', fg='#484747', background='#d6b7d7')
        lb_clock2.place(x=185, y=40, width=120, height=30)

        def datetm():
            global curtime
            curtime = datetime.now().time()
            ftime = curtime.strftime('%H:%M:%S')
            lb_clock2.config(text=ftime)
            lb_clock2.after(1000, datetm)  # ให้เรียกฟังก์ชันตัวมันเองทุก 1 วินาที
        datetm()

        put_img=tk.Entry(root) #พื้นที่ใส่รูป
        put_img["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=28)
        put_img["font"] = ft
        put_img["fg"] = "#333333"
        put_img["justify"] = "center"
        put_img["text"] = "Photo"
        put_img.place(x=72,y=168,width=352,height=470)

        rank = tk.Label(root)
        ft = tkFont.Font(family='Mitr', size=20)
        rank["bg"] = "#d6b7d7"
        rank["font"] = ft
        rank["fg"] = "#000000"
        rank["justify"] = "left"
        rank["text"] = "คำนำหน้า"
        rank.place(x=467, y=210, width=140, height=30)

        input_rank = tk.Entry(root) #ช่องคำนำหน้า
        input_rank["bg"] = "#ffffff"
        input_rank["borderwidth"] = "2px"
        ft = tkFont.Font(family='Mitr', size=20)
        input_rank["font"] = ft
        input_rank["fg"] = "#000000"
        input_rank["justify"] = "center"
        input_rank["text"] = "คำนำหน้า"
        input_rank.place(x=600, y=203, width=165, height=42)

        name=tk.Label(root)
        ft = tkFont.Font(family='Mitr', size=20)
        name["bg"] = "#d6b7d7"
        name["font"] = ft
        name["fg"] = "#000000"
        name["justify"] = "center"
        name["text"] = "ชื่อ"
        name.place(x=765, y=210,width=62,height=30)

        input_name = tk.Entry(root) #ช่องชื่อ
        input_name["bg"] = "#ffffff"
        input_name["borderwidth"] = "2px"
        ft = tkFont.Font(family='Mitr', size=20)
        input_name["font"] = ft
        input_name["fg"] = "#000000"
        input_name["justify"] = "center"
        input_name["text"] = "ชื่อ"
        input_name.place(x=825, y=203, width=374, height=42)

        occu1=tk.Label(root)
        ft = tkFont.Font(family='Mitr', size=20)
        occu1["bg"] = "#d6b7d7"
        occu1["font"] = ft
        occu1["fg"] = "#000000"
        occu1["justify"] = "left"
        occu1["text"] = "สกุล"
        occu1.place(x=490, y=270,width=145,height=30)

        input_last = tk.Entry(root) #ช่องสกุล
        input_last["bg"] = "#ffffff"
        input_last["borderwidth"] = "2px"
        ft = tkFont.Font(family='Mitr', size=20)
        input_last["font"] = ft
        input_last["fg"] = "#000000"
        input_last["justify"] = "center"
        input_last["text"] = "สกุล"
        input_last.place(x=600, y=264, width=600, height=42)

        occu=tk.Label(root)
        ft = tkFont.Font(family='Mitr', size=20)
        occu["bg"] = "#d6b7d7"
        occu["font"] = ft
        occu["fg"] = "#000000"
        occu["justify"] = "right"
        occu["text"] = "ตำแหน่ง"
        occu.place(x=477,y=332,width=130,height=30)

        input_occu = tk.Entry(root) #ช่องตำแหน่ง
        input_occu["bg"] = "#ffffff"
        input_occu["borderwidth"] = "2px"
        ft = tkFont.Font(family='Mitr', size=20)
        input_occu["font"] = ft
        input_occu["fg"] = "#000000"
        input_occu["justify"] = "center"
        input_occu["text"] = "ตำแหน่ง"
        input_occu.place(x=600, y=325, width=600, height=42)

        depart = tk.Label(root)
        ft = tkFont.Font(family='Mitr', size=20)
        depart["bg"] = "#d6b7d7"
        depart["font"] = ft
        depart["fg"] = "#000000"
        depart["justify"] = "center"
        depart["text"] = "กรม"
        depart.place(x=540,y=393, width=50, height=30)

        input_depart = tk.Entry(root) #ช่องกรม
        input_depart["bg"] = "#ffffff"
        input_depart["borderwidth"] = "2px"
        ft = tkFont.Font(family='Mitr', size=20)
        input_depart["font"] = ft
        input_depart["fg"] = "#000000"
        input_depart["justify"] = "center"
        input_depart["text"] = "กรม"
        input_depart.place(x=600, y=386, width=600, height=42)

        depart2 = tk.Label(root)
        ft = tkFont.Font(family='Mitr', size=20)
        depart2["bg"] = "#d6b7d7"
        depart2["font"] = ft
        depart2["fg"] = "#000000"
        depart2["justify"] = "center"
        depart2["text"] = "กอง"
        depart2.place(x=539,y=454, width=50, height=30)

        input_depart2 = tk.Entry(root) #ช่องกอง
        input_depart2["bg"] = "#ffffff"
        input_depart2["borderwidth"] = "2px"
        ft = tkFont.Font(family='Mitr', size=20)
        input_depart2["font"] = ft
        input_depart2["fg"] = "#000000"
        input_depart2["justify"] = "center"
        input_depart2["text"] = "กอง"
        input_depart2.place(x=600, y=447, width=600, height=42)

        """img2 = PhotoImage(file='bt_access_02.png')
        w = img2.width()
        h = img2.height()
        cv = Canvas(width=w, height=h, bd=0)
        cv.create_image(1, 2, anchor=NW, image=img2)
        cv.image = img2
        #cv["bg"]="#FFFF33"
        cv.place(x=480, y=550)

        img3 = PhotoImage(file='bt_denied_02.png')
        w = img3.width()
        h = img3.height()
        cv = Canvas(width=w, height=h, bd=0)
        cv.create_image(1, 2, anchor=NW, image=img3)
        cv.image = img3
        #cv["bg"] = "#FFFF33"
        cv.place(x=855, y=550)"""

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


