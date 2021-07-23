import datetime
from tkinter import *
from PIL import ImageTk,Image  

ws = Tk()  
ws.title('Sleep Cycle')
ws.geometry('500x500')
canvas = Canvas(
        ws, 
        width = 500, 
        height = 500
        )  
canvas.pack(fill='both', expand = True)
img = ImageTk.PhotoImage(Image.open('bg.png'))  
canvas.create_image(
        10, 
        10, 
        anchor=NW, 
        image=img
        )
var = StringVar()
def function():
    now = datetime.datetime.strftime(datetime.datetime.now(), '%I:%M:%p')
    print("Hey there, it's", now)
    text = ""
    def sleep_calc(date_now):
        sleep = date_now + datetime.timedelta(minutes=90)
        wake = datetime.datetime.strftime(sleep, '%I:%M:%p')
        return wake
    print ("You should sleep now and set your alarm at:")
    date_now = datetime.datetime.now()
    date_now = date_now + datetime.timedelta(minutes=15)
    for i in range(0,6):
        print(sleep_calc(date_now))
        date_now = date_now + datetime.timedelta(minutes=90)
        var.set(text)
start = Button(command=function, text="Start")
start.place(y=220,x=230)
start = Button.pack
sleep_time = Label(textvariable=var)
sleep_time = Label.pack
ws.mainloop()