# -*- coding: utf-8 -*-
"""
some more practice on how widgets are placed in a grid geometry manager
"""
import tkinter as tk

# sticky is a kw parameter in grid
# sticky sets the location of the widget inside the grid.
# by default widgets are placed in center of a grid cell
# sticky is set as compass points i.e. n, s, e, w, ne, nw, se, sw

main_window = tk.Tk()
main_window.columnconfigure(0, minsize=250)
main_window.rowconfigure([0,1,2], minsize=100)

label_y = tk.Label(text="label1")
label_y.grid(row=0, column=0, sticky="ne")

label_b = tk.Label(text="label2")
label_b.grid(row=1, column=0, sticky="sw")

# when a widget is positioned with sticky the widget size will be only 
# as much as the text or any component within the widget
# it will not fill up the entire grid cell
# to make a widget fill up the entire grid cell
# sticky should be set to "ew" - to fill only horizontally
# "ns" - to fill only vertically
# "nsew" - to fill the entire grid cell
label_frame = tk.Frame(master=main_window, relief=tk.RAISED, borderwidth=1)
label_frame.grid(row=2, column=0, sticky="nsew")
label_frame.columnconfigure([0,1,2,3], minsize=50)
label_frame.rowconfigure(0, minsize=100)

label_0 = tk.Label(master=label_frame, text="0", bg="black", fg="white")
label_0.grid(row=0, column=0)
label_1 = tk.Label(master=label_frame, text="1", bg="black", fg="white")
label_1.grid(row=0, column=1, sticky="ew")
label_2 = tk.Label(master=label_frame, text="2", bg="black", fg="white")
label_2.grid(row=0, column=2, sticky="ns")
label_3 = tk.Label(master=label_frame, text="3", bg="black", fg="white")
label_3.grid(row=0, column=3, sticky="nsew")

main_window.mainloop()
