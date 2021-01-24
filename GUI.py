import tkinter as tk
import matplotlib.pyplot as plt
import sympy
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()

fig = plt.figure(figsize=(4, 3))
graph = fig.add_subplot(111)

mp_list = []
sym_list = []
text_list = []
base_str = ""


def update_base():
    num_str = ""
    for i in text_list:
        num_str += i
    base_str = num_str
    y_eq.configure(text="y= " + base_str)


def up_eq(text_name):
    text_list.append(text_name)
    update_base()


def add_num():
    try:
        float(num_e.get())
        actual_error.configure(text="")
        text_list.append(num_e.get())
        num_e.delete(0, "end")
        update_base()
    except ValueError:
        actual_error.configure(text="Invalid Number")


title = tk.Label(text="PyGrapher", font=("Consolas", 20))
title.grid(row=0, column=0, columnspan=7)

eq_h = tk.Label(text="Equation", font=("Arial", 12), bg="#E0E0E0")
eq_h.grid(row=1, column=0)
eq_y = tk.Label(text="y=")
eq_y.grid(row=2, column=0)
eq_deriv = tk.Button(text="Graph Deriv.")
eq_int = tk.Button(text="Graph Anti-Deriv")
eq_deriv.grid(row=3, column=0)
eq_int.grid(row=4, column=0)

num_h = tk.Label(text="Insert Number", font=("Arial", 12), bg="#E0E0E0")
num_e = tk.Entry(width=7)
num_b = tk.Button(text="Enter Number", command=add_num)
num_h.grid(row=6, column=0)
num_e.grid(row=7, column=0)
num_b.grid(row=8, column=0)

con_h = tk.Label(text="Controls", font=("Arial", 12), bg="#E0E0E0")
con_h.grid(row=1, column=6)
con_zoom_in = tk.Button(text="Zoom In")
con_zoom_in.grid(row=2, column=6)
con_zoom_out = tk.Button(text="Zoom Out")
con_zoom_out.grid(row=3, column=6)
con_clear_graph = tk.Button(text="Clear Graph")
con_clear_graph.grid(row=4, column=6)

x = tk.Button(text="x", command=lambda: up_eq(x['text']))
x.grid(row=6, column=1)
exponent = tk.Button(text="^", command=lambda: up_eq(exponent['text']))
exponent.grid(row=7, column=1)
sin = tk.Button(text="sin", command=lambda: up_eq(sin['text']))
sin.grid(row=8, column=1)
plus = tk.Button(text="+", command=lambda: up_eq(plus['text']))
plus.grid(row=6, column=2)
e = tk.Button(text="e^", command=lambda: up_eq(e['text']))
e.grid(row=7, column=2)
cos = tk.Button(text="cos", command=lambda: up_eq(cos['text']))
cos.grid(row=8, column=2)
neg = tk.Button(text="-", command=lambda: up_eq(neg['text']))
neg.grid(row=6, column=3)
div = tk.Button(text="/", command=lambda: up_eq(div['text']))
div.grid(row=6, column=4)
mult = tk.Button(text="*", command=lambda: up_eq(mult['text']))
mult.grid(row=6, column=5)
ln = tk.Button(text="ln", command=lambda: up_eq(ln['text']))
ln.grid(row=7, column=3)
par_open = tk.Button(text="(", command=lambda: up_eq(par_open['text']))
par_open.grid(row=7, column=4)
par_close = tk.Button(text=")", command=lambda: up_eq(par_close['text']))
par_close.grid(row=7, column=5)
tan = tk.Button(text="tan", command=lambda: up_eq(tan['text']))
tan.grid(row=8, column=3)
dele = tk.Button(text="DEL")
dele.grid(row=8, column=5)
clear = tk.Button(text="CLEAR")
clear.grid(row=8, column=4)

err_h = tk.Label(text="Error Log", font=("Arial", 12), bg="#E0E0E0")
err_h.grid(row=5, column=6)
actual_error = tk.Label(text="", fg="red")
actual_error.grid(row=6, column=6)


y_eq = tk.Label(text="y= " + base_str, bg="#E0E0E0")
y_eq.grid(row=5, column=1, columnspan=4)
g_button = tk.Button(text="GRAPH", pady=5)
g_button.grid(row=5, column=5)

window.mainloop()
