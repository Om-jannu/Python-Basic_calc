# Python GUI program to

from tkinter import *


def add_numbers():
    res = int(e1.get()) + int(e2.get())
    label_text.set(res)

def sub_numbers():
    res = int(e1.get()) - int(e2.get())
    label_text.set(res)

def mul_numbers():
    res = int(e1.get()) * int(e2.get())
    label_text.set(res)

def div_numbers():
    res = int(e1.get()) % int(e2.get())
    label_text.set(res)

window = Tk()
label_text = StringVar();
Label(window, text="Enter First Number:").grid(row=0, sticky=W)
Label(window, text="Enter Second Number:").grid(row=1, sticky=W)
Label(window, text="Result:").grid(row=3, sticky=W)
result = Label(window, text="", textvariable=label_text).grid(row=3, column=1, sticky=W)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b = Button(window, text="add", command=add_numbers)
b.grid(row=0, column=2, padx=5, pady=5)

b = Button(window, text="sub", command=sub_numbers)
b.grid(row=1, column=2, padx=5, pady=5)

b = Button(window, text="mul", command=mul_numbers)
b.grid(row=2, column=2, padx=5, pady=5)

b = Button(window, text="div", command=div_numbers)
b.grid(row=3, column=2, padx=5, pady=5)

mainloop()