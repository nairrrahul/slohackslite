import tkinter as tk
import matplotlib.pyplot as plt
import sympy
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()

mp_list = []
sym_list = []
text_list = []
base_str = ""
mix, miy, mx, may = -10, -10, 10, 10

fig = plt.figure(figsize=(4, 3))
graph = fig.add_subplot(111)
plt.axis((mix, mx, miy, may))

xa0, ya0 = [mix*10, mx*10], [0, 0]
xa1, ya1 = [0, 0], [miy*10, may*10]

graph.plot(xa0, ya0, color='black')
graph.plot(xa1, ya1, color='black')

graph_canv = FigureCanvasTkAgg(fig, master=window)
graph_canv.draw()


def update_base():
    num_str = ""
    for i in text_list:
        num_str += i
    base_str = num_str
    y_eq.configure(text="y= " + base_str)


def up_eq(text_name):
    actual_error.configure(text="")
    text_list.append(text_name)
    if text_name == '^':
        mp_list.append('**')
    else:
        mp_list.append(text_name)
    update_base()


def add_num():
    try:
        float(num_e.get())
        actual_error.configure(text="")
        text_list.append(num_e.get())
        mp_list.append(num_e.get())
        num_e.delete(0, "end")
        update_base()
    except ValueError:
        actual_error.configure(text="Invalid Number")


def dc(choice):
    actual_error.configure(text="")
    global text_list, mp_list
    try:
        text_list.pop()
        mp_list.pop()
        if choice == 1:
            text_list = []
            mp_list = []
        update_base()
    except IndexError:
        actual_error.configure(text="Cannot Remove From \nEmpty Eq.")


def clear_function():
    plt.cla()
    graph.plot(xa0, ya0, color='black')
    graph.plot(xa1, ya1, color='black')
    graph_canv = FigureCanvasTkAgg(fig, master=window)
    graph_canv.draw()


def graph_function(list_func, min, max):
    try:
        b_s = ''
        good_list = ''
        for i in range(len(list_func)):
            b_s += list_func[i]
            good_list += text_list[i]
        x1 = np.array(range(int(min)*10-1, int(max)*10+2))
        x = x1/10
        x_0 = x.tolist()
        y = eval(b_s)
        y_0 = y.tolist()
        plt.axis((mix, mx, miy, may))
        graph.plot(x_0, y_0)
        eq_y.configure(text="y="+good_list)
        graph_canv.draw()
        graph_canv.get_tk_widget().grid(row=1, column=1, rowspan=4, columnspan=5)
    except SyntaxError:
        actual_error.configure(
            text="Check Equation. Don't Forget\na * sign for mult.")


def zoom_in():
    global mix, mx, miy, may
    mix, mx, miy, may = mix/2, mx/2, miy/2, may/2
    plt.cla()
    graph.plot(xa0, ya0, color='black')
    graph.plot(xa1, ya1, color='black')
    graph_function(mp_list, mix, mx)


def zoom_out():
    global mix, mx, miy, may
    mix, mx, miy, may = mix*2, mx*2, miy*2, may*2
    plt.cla()
    graph.plot(xa0, ya0, color='black')
    graph.plot(xa1, ya1, color='black')
    graph_function(mp_list, mix, mx)


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
con_zoom_in = tk.Button(text="Zoom In", command=zoom_in)
con_zoom_in.grid(row=2, column=6)
con_zoom_out = tk.Button(text="Zoom Out", command=zoom_out)
con_zoom_out.grid(row=3, column=6)
con_clear_graph = tk.Button(text="Clear Graph", command=clear_function)
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
dele = tk.Button(text="DEL", command=lambda: dc(0))
dele.grid(row=8, column=5)
clear = tk.Button(text="CLEAR", command=lambda: dc(1))
clear.grid(row=8, column=4)

err_h = tk.Label(text="Error Log", font=("Arial", 12), bg="#E0E0E0")
err_h.grid(row=5, column=6)
actual_error = tk.Label(text="", fg="red")
actual_error.grid(row=6, column=6)


y_eq = tk.Label(text="y= " + base_str, bg="#E0E0E0")
y_eq.grid(row=5, column=1, columnspan=4)
g_button = tk.Button(
    text="GRAPH", command=lambda: graph_function(mp_list, mix, mx))
g_button.grid(row=5, column=5)


graph_canv.get_tk_widget().grid(row=1, column=1, rowspan=4, columnspan=5)

window.mainloop()
