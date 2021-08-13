# -*- coding: utf-8 -*-
"""
Geometry manager = grid
- splits the window into rows and columns
- widget is placed in the grid by passing the row and column index
- row and column indices are 0 based

padding = adds blank space around a widget
"""
import tkinter as tk

main_window = tk.Tk()

# create a 3x3 grid
# 2 geometry managers are used
# frames are added to the main window in the loop.
# This is done with the grid geometry manager specifying the row and column
# labels are added to each frame using the pack geometry manager
for i in range(3):
    for j in range(3):
        frame = tk.Frame(master=main_window, relief=tk.RAISED,borderwidth=2)
        frame.grid(row=i, column=j)
        # padx and pady: adds padding in x and y. padding is measured in pixels
        label = tk.Label(master=frame, text=f"({i},{j})", padx=5, pady=5)
        label.pack()

main_window.mainloop()