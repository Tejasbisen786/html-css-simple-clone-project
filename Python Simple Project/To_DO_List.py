from tkinter import*
from tkinter import messagebox
def add():
    task=l2.get()
    if task:
        tasks_listbox.insert(END,task)
        l2.delete(0,END)
    else:
        messagebox.showwarning("Warning","Check Onces Again !! ")
def remove():
    taskremove=tasks_listbox.curselection()
    if taskremove:
        tasks_listbox.delete(taskremove)
    else:
        messagebox.showwarning("Warning","Check Onces Again !! ")
def update():
    taskremove=tasks_listbox.curselection()
    if taskremove:
        update=l2.get()
        if update:
            tasks_listbox.delete(taskremove)
            tasks_listbox.insert(taskremove,update)
            l2.delete(0,END)
        else:
            messagebox.showwarning("Warning","Check Onces Again !! ")
    else:
        def remove():
            tasks_listbox.delete(0,END)
r=Tk()
r.title("TodoList")
l1=Label(r,text="To-do-List",padx=40,pady=40,bg="#C4A484", font=("Helvetica",20))
l1.pack(fill=BOTH)
l2=Entry(r,font=("Helvetica",20))
l2.pack(fill=BOTH,padx=20,pady=20)
frame = Frame(r)
frame.pack(pady=10)
tasks_listbox=Listbox(
    frame,
    width=27,
    height=15,
    font="Helvetica",
    bd=2,
    activestyle = 'dotbox',
    fg="black",
)
tasks_listbox.pack(side=LEFT,fill=BOTH , padx=10)
button_frame=Frame(r)
button_frame.pack()
add=Button(
    button_frame,
    text="AddTask",
    bg='#C4A484',
    font='times',
    padx=20,
    pady=10,
    command=add,
)
add.pack(fill=BOTH, expand=True,side=LEFT)
delete=Button(
    button_frame,
    text="Delete",
    bg='#C4A484',
    font='times',
    padx=20,
    pady=10,
    command=remove,
)
delete.pack(fill=BOTH, expand=True,side=LEFT)
update=Button(
    button_frame,
    text="Update",
    bg='#C4A484',
    font='times',
    padx=20,
    pady=10,
    command=update,
)
update.pack(fill=BOTH,expand=True,side=BOTTOM)
r.maxsize(400,600)
r.minsize(400,600)
r.mainloop()