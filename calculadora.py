import tkinter as tk
from math import *

def evaluate(event):
    try:
        display_text.set(str(eval(entry.get())))
    except:
        if (str(entry.get()) == ""):
            display_text.set('0')
        else:
            display_text.set('Syntax Error')

w = tk.Tk()
w.title('calculadora')
w.geometry('300x100')

text = tk.Label(w, text='DIGITE A EXPRESSÃO MATEMÁTICA')
text.pack(fill='x', padx=5, pady=5)

entry = tk.Entry(w,width=30)
entry.bind('<Return>', evaluate)
entry.pack(fill='x')

display_text = tk.StringVar(value=0)
display = tk.Label(w, textvariable=display_text)
display.pack(side='right')

equal = tk.Label(w,text='=')
equal.pack(side='right')

w.mainloop()