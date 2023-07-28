from tkinter import*
import time
import sys
from time import strftime
def clock():
    current_time =time.strftime("%H : %M : %S")
    digital.config(text=current_time)
    digital.after(100,clock)
r=Tk()
r.geometry("500x200")
r.title("Digital_Clock")
digital=Label(r,font=("times",45,"bold"),bg="Red",fg="white")
digital.grid(row=2,column=2,pady=25,padx=100)
clock()
sec=Label(r,text="hours      minutes      seconds",font=("times", 20 ,"bold"),bg="Red",fg="white")
sec.grid(row=3,column=2)
r['bg']="Red"
r.mainloop()