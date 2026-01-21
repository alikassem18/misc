from tkinter import *

def addNum():
    first=int(one_entry.get())
    second=int(two_entry.get())
    result=first+second
    result_label.config(text=result)

w=Tk()
w.title("calc two numbers")

one=Label(w,text="your first number")
one_entry=Entry(w)

two=Label(w,text="your second number")
two_entry=Entry(w)

button=Button(w,text="add them",command=addNum)

result_label=Label(w,text="Result")

one.grid(row=0,column=0)
one_entry.grid(row=0,column=1)

two.grid(row=1,column=0)
two_entry.grid(row=1,column=1)

button.grid(row=2,column=0)

result_label.grid(row=3,column=0)