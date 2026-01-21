from tkinter import *

def addNum():
    F = int(E1.get())
    S = int(E2.get())
    Result = F + S
    L3.config(text = Result)

win = Tk()
win.title('calc two numbers')

L1 = Label(win, text = 'your first number')
L1.grid(row = 0, column = 0)
E1 = Entry(win)
E1.grid(row = 0, column = 1)

L2 = Label(win, text = 'your second number')
L2.grid(row = 1, column = 0)
E2 = Entry(win)
E2.grid(row = 1, column = 1)

B1 = Button(win, text = 'add them', command = addNum)
B1.grid(row = 2, column = 0)

L3 = Label(win, text = 'Result')
L3.grid(row = 3, column = 0)

mainloop()