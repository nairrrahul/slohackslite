import tkinter as tk
import matplotlib.pyplot as plt
import sympy
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()

fig = plt.figure(figsize=(4, 3))
graph = fig.add_subplot(111)

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


err_h = tk.Label(text="Error Log")
err_h.grid(row=5, column=6, rowspan=4)


window.mainloop()
