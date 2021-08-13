# -*- coding: utf-8 -*-
"""
geometry manager - place()

place - places widgets in the window based on the x,y co ordinates
for the top left corner of the window
use to control the precise location of the widget in the window
any x,y argument to place is the number of pixels from the top left 
corner of the window
drawbacks of place:
    - not responsive: window resize has no effect on the widgets
    - difficult to manage: as exact x,y is needed and if application
    has lot of widgets
"""
import tkinter as tk

main_window = tk.Tk()
frame = tk.Frame(master=main_window, width=200, height=100)
frame.pack()

red_label = tk.Label(master=frame, text="I am at (0,0)", bg="red")
red_label.place(x=0, y=0)

yellow_label = tk.Label(master=main_window, text="I am at (75,75)", bg="yellow")
yellow_label.place(x=75, y=75)

main_window.mainloop()