from tkinter import*
root=Tk()
root.geometry("644x900")
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 35 bold",bg="green",fg="white")
screen.pack(fill=X,padx=20,pady=20,ipady=8,ipadx=8)
root.title("Soumya's Calculator")
f1=Frame(root,bg="green")
b1=Button(f1,bg="orange",fg="white",text="C", font=("lucida 30 bold"),padx=32,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="%", font=("lucida 30 bold"),padx=29,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="/", font=("lucida 30 bold"),padx=40,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="green")
b1=Button(f1,bg="orange",fg="white",text="7", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="8", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="9", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="green")
b1=Button(f1,bg="orange",fg="white",text="4", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="5", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="6", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="green")
b1=Button(f1,bg="orange",fg="white",text="1", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="2", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="3", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="green")
b1=Button(f1,bg="orange",fg="white",text=".", font=("lucida 30 bold"),padx=41,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="0", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="+", font=("lucida 30 bold"),padx=34.3,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="green")
b1=Button(f1,bg="orange",fg="white",text="-", font=("lucida 30 bold"),padx=40.5,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="*", font=("lucida 30 bold"),padx=36,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
b1=Button(f1,bg="orange",fg="white",text="=", font=("lucida 30 bold"),padx=35,pady=4)
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()
root.mainloop()