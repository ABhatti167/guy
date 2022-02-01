from tkinter import *
from tkinter import filedialog

theroot = Tk()

e = Entry(theroot, width=35, borderwidth=3)


e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


quit = Button(theroot, text= "Exit", command = theroot.quit, padx=30,pady=20)



quit.grid(row=6,column=1)



def button_click(number):

    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))



def button_add():
    first = e.get()
    global f_num
    f_num =int(first)


    e.delete(0, END)



def button_equals():

    global second_num
    second_num = e.get()

    e.delete(0, END)

    e.insert(0, f_num + int(second_num))


def button_clear():
    e.delete(0, END)
    f_num = 0
    second_num = 0




button_1= Button(theroot, text="1", padx=40,pady=20,command=lambda: button_click(1))
button_2= Button(theroot, text="2", padx=40,pady=20,command=lambda: button_click(2))
button_3= Button(theroot, text="3", padx=40,pady=20,command=lambda: button_click(3))
button_4= Button(theroot, text="4", padx=40,pady=20,command=lambda: button_click(4))
button_5= Button(theroot, text="5", padx=40,pady=20,command=lambda: button_click(5))
button_6= Button(theroot, text="6", padx=40,pady=20,command=lambda: button_click(6))
button_7= Button(theroot, text="7", padx=40,pady=20,command=lambda: button_click(7))
button_8= Button(theroot, text="8", padx=40,pady=20,command=lambda: button_click(8))
button_9= Button(theroot, text="9", padx=40,pady=20,command=lambda: button_click(9))
button_0= Button(theroot, text="0", padx=40,pady=20,command=lambda: button_click(0))

button_equals= Button(theroot, text="=", padx=91,pady=20,command=button_equals)
button_add= Button(theroot, text="+", padx=39,pady=20,command=button_add)
button_clear= Button(theroot, text="Clear", padx=79,pady=20,command= button_clear)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_equals.grid(row=5, column=1,columnspan=2)
button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1,columnspan=2)






theroot.mainloop()