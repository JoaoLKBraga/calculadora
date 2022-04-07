import tkinter as tk
from math import *

def evaluate(event):
    try:
        entry.insert('end', ' = '+str(eval(entry.get())))
    except:
        entry.delete('0','end')
        entry.insert('end','Syntax Error')    

w = tk.Tk()
w.title('calculadora')
w.geometry('300x70')

tk.Label(w, text='DIGITE A EXPRESSÃO MATEMÁTICA').pack()

entry = tk.Entry(w,width=30)
entry.bind('<Return>', evaluate)
entry.pack()

w.mainloop()