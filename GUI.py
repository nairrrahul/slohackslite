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

title = tk.Label(text="PyGrapher", font=("Consolas", 20))
title.grid(row=0, column=0, columnspan=7)

eq_h = tk.Label(text="Equation")
eq_h.grid(row=1, column=0)
eq_y = tk.Label(text="y=")
eq_y.grid(row=2, column=0)
eq_deriv = tk.Button(text="Graph Deriv.")
eq_int = tk.Button(text="Graph Anti-Deriv")
eq_deriv.grid(row=3, column=0)
eq_int.grid(row=4, column=0)

num_h = tk.Label(text="Insert Number")
num_e = tk.Entry()
num_b = tk.Button(text="Enter Number")
num_h.grid(row=6, column=0)
num_e.grid(row=7, column=0)
num_b.grid(row=8, column=0)

con_h = tk.Label(text="Controls")
con_h.grid(row=1, column=6)

con_zoom_in = tk.Button(text="Zoom In")
con_zoom_in.grid(row=2, column=6)

con_zoom_out = tk.Button(text="Zoom Out")
con_zoom_out.grid(row=3, column=6)

con_clear_graph = tk.Button(text="Clear Graph")
con_clear_graph.grid(row=4, column=6)

x = tk.Button(text="X")
x.grid(row=6, column=1)

exponent = tk.Button(text="^")
exponent.grid(row=7, column=1)

sin = tk.Button(text="Sin")
sin.grid(row=8, column=1)

plus = tk.Button(text="+")
plus.grid(row=6, column=2)

e = tk.Button(text="e^")
e.grid(row=7, column=2)

cos = tk.Button(text="cos")
cos.grid(row=8, column=2)

neg = tk.Button(text="-")
neg.grid(row=6, column=3)

div = tk.Button(text="/")
div.grid(row=6, column=4)

mult = tk.Button(text="*")
mult.grid(row=6, column=5)

ln = tk.Button(text="ln")
ln.grid(row=7, column=3)

par_open = tk.Button(text="(")
par_open.grid(row=7, column=4)

par_close = tk.Button(text=")")
par_close.grid(row=7, column=5)

tan = tk.Button(text="tan")
tan.grid(row=8, column=3)

dele = tk.Button(text="DEL")
dele.grid(row=8, column=5)

clear = tk.Button(text="Clear")
clear.grid(row=8, column=4)

err_h = tk.Label(text="Error Log")
err_h.grid(row=5, column=6, rowspan=4)


window.mainloop()
