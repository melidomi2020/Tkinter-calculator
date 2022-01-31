from tkinter import *

root=Tk()
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
root.title("simple calculator")


def add(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    return
def clear():
    e.delete(0,END)

button_1=Button(root,text="1",command =lambda: add(1))
button_2=Button(root,text="2",command =lambda: add(2))
button_3=Button(root,text="3",command =lambda: add(3))
button_4=Button(root,text="4",command =lambda: add(4))
button_5=Button(root,text="5",command =lambda: add(5))
button_6=Button(root,text="6",command =lambda: add(6))
button_7=Button(root,text="7",command =lambda: add(7))
button_8=Button(root,text="8",command =lambda: add(8))
button_9=Button(root,text="9",command =lambda: add(9))
button_equal=Button(root,text="=",command =add)
button_clear=Button(root,text="clear",command =clear)
button_add=Button(root,text="+",command =add)
button_0=Button(root,text="0",command =lambda: add(0))
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_equal.grid(row=5,column=0)
button_clear.grid(row=5,column=1)
button_add.grid(row=5,column=2)
root.mainloop()