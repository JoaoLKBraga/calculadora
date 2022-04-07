import tkinter as tk
from math import *

def evaluate(event):
    try:
        entry.insert("end", " = " + str(eval(entry.get())))
    except:
        entry.delete("0","end")
        entry.insert("end","Syntax Error")
    

w = tk.Tk()
w.title = "caluculadora"
w.geometry("400x70")

tk.Label(w, text="DIGITE A EXPRESSÃO MATEMÁTICA").pack()

entry = tk.Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()

w.mainloop()