# -*- coding: utf-8 -*-
"""
tkinter basics - geometry managers
learn about
pack()

Each window or Frame in the application can use only one Geometry Manager
Different frames can use different geometry managers
even if they are assigned to a frame with a different geometry manager

How pack works 
    - uses packing algorithm
packing algorithm :
    - computes a rectangular area which is wide (or tall) enough
    to hold the widget. Rest of the window is blank space
    - centers the widget in the window unless anchor is specified.

pack arguments 
 - fill= specfies which direction the widget should fill
 i.e. when window is resized how the widget will grow
 - side= specifies which side of the window the widgets will be placed
 by default placed at top or top most portion of the window
"""
import tkinter as tk

main_window = tk.Tk()

frame1 = tk.Frame(master=main_window, width=50, height=50, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=main_window, width=50, bg="green")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=main_window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

main_window.mainloop()