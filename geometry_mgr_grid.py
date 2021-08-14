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
# labels are added to each frame using the pack geometry 
# rowconfigure and columnconfigure - adjust how the widgets grow when the window
# is resized.
# row/columnconfigure take 3 parameters
# 1. index of the row/column grid (or list of indices)
# 2. weight = how the row/column responds to resizing of window wrt other 
#             rows or columns. Default is 0 i.e. no grow/shrink on resize
# 3. minsize = sets the min size for the row/column in pixels
for i in range(3):
    main_window.rowconfigure(i, weight=1, minsize=75)
    main_window.columnconfigure(i, weight=1, minsize=75)
    for j in range(3):
        frame = tk.Frame(master=main_window, relief=tk.RAISED,borderwidth=2)
        frame.grid(row=i, column=j,  padx=5, pady=5)
        # padx and pady: adds padding in x and y around the widget. 
        # padding is measured in pixels
        label = tk.Label(master=frame, text=f"({i},{j})", bg="yellow")
        label.pack(padx=5, pady=5)
        

main_window.mainloop()
