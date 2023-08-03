'''
T Kinter is python GUI library
Label,Button,Entry,Radio ,CheckButton ,Combo Box ,NoteBook , SpinBox ,Menu Bar , Scrolled Text

import tkinter
top = tk.Tk()
#code is written here
top.mainloop()
'''
import tkinter as tk

# window = tk.Tk()
# window.title("GUI")
# label = tk.Label(window,text="Hello World!").pack()
# window.mainloop()

# from tkinter import messagebox
# import Tkmessagebox
# top = tk.Tk()
# def helloCallBack():
#     TkmessageBox.showinfo("Hello Python ", "Hello world")
# B = tk.Button(top,text="Hello",command=helloCallBack)
# B.pack()
# top.mainloop()
'''
from tkinter import messagebox
from tkinter import *
gui = Tk()
gui.title("Welcome to the Python GUI")
w = 400
h = 400
gui.geometry(f"{w}x{h}")
gui.minsize(w,h)
gui.maxsize(600,600)
label = tk.Label(gui,text="Hello World!").pack()
gui.mainloop()
'''
'''
from tkinter import *
root = Tk()
root.geometry("500x500")
btn1 = Button(root,text="Hello World!").pack(side=RIGHT)
btn2 = Button(root,text="Hello World!").pack(side=LEFT)
btn3 = Button(root,text="Hello World!").pack(side=BOTTOM)
btn4 = Button(root,text="Hello World!").pack(side=TOP)
root.mainloop()
'''
'''
from tkinter import *
parent = Tk()
parent.title("Students")
parent.geometry("700x500")
name = Label(parent,text="Name: ")
name.grid(row=0,column=0,pady=10,padx=5)
e1 = Entry(parent)
e1.grid(row=0,column=1)
regno = Label(parent,text = "Regd NO: ")
regno.grid(row=1,column=0,padx=5,pady=10)
e2 = Entry(parent)
e2.grid(row=1,column=1)
btn = Button(parent,text="Submit")
btn.grid(row=3,column=1)
parent.mainloop()
'''
