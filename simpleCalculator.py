from tkinter import * 
def click(event):
    global sValue
    txt1 = event.widget.cget
    ("text")
    if (txt1 == "="):
        pass
        if txt1== "=":
            pass
        else:
            val1 = eval(screen1.get())
            sValue.set(val1)
            screen1.update()
    elif txt1 == "C":
        sValue.set("")
        screen1.update()
    else:
        sValue.set(sValue.get()+txt1)
root = Tk()
#GUI logic for simple calculator
root.title("Simple Calculator")
root.geometry("1200x800")
sValue = StringVar()
sValue.set("")
screen1 = Entry(root,textvariable=sValue,font="lucida 30").pack(fill=X,padx=10,pady=10)
#Frame 1 for adding buttons 9,8,7

f = Frame(root,bg="red")
# photo1 = PhotoImage                   #Add a photo to the GUI
# pLabel = Label(image=photo1).pack()

bt1 = Button(f,text="9",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="8",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="7",padx=6,pady=6 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="+",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1.bind(<Button-1>,click)
f.pack()
f = Frame(root,bg="red")
bt1 = Button(f,text="6",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="5",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="4",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="-",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1.bind(<Button-1>,click)
f.pack()
f = Frame(root,bg="red")
bt1 = Button(f,text="1",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="3",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="2",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1 = Button(f,text="=",padx=8,pady=8 ,font="lucida 16 bold").pack(side=LEFT , padx=12,pady=12)
bt1.bind(<Button-1>,click)
f.pack()

root.mainloop()