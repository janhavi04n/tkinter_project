import tkinter as tk

#print(tkinter.TkVersion)
#print(tkinter.TclVersion)
# this is a access to a protected method.
# tkinter._test()

# this also creates a window
gui_window = tk.Tk()
# set the title
# gui_window.title("Python rocks!!")
# set the width height left and top offsets
# sets w = 640 h = 480, position 50 pixels from left of screen and 100 pixels from top
# if offset values have minus sign then offset is from right and bottom of screen
# gui_window.geometry("100x100+50+100")

# create a label
# , fg="red", bg="black"
# lable = tkinter.Label(text="Python rocks!!")
# pack is one of the ways to add the widget to a window
# pack will resize the window small as the widget size
# doesnt work if the .geometry is called 
#lable.pack()

border_effects = {
    "raised" : tk.RAISED,
    "sunken" : tk.SUNKEN,
    "groove" : tk.GROOVE,
    "ridge"  : tk.RIDGE,
    "flat"   : tk.FLAT
}

for relief_nm, relief_type in border_effects.items():
    frame = tk.Frame(master=gui_window, relief=relief_type, borderwidth=5)
    frame.pack(side=tk.LEFT)
    lable = tk.Label(master=frame, text=relief_nm)
    lable.pack()


frm_entries = tk.Frame(master=gui_window, relief=tk.RAISED, borderwidth=5)
frm_entries.pack(side=tk.BOTTOM)
ent_names = tk.Entry(master=frm_entries)
ent_names.pack()
ent_names.insert(0, "Python is good!")

# this method is important as it will display the window. and wait till
# the window is closed
gui_window.mainloop()
