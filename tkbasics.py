import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)
# this is a access to a protected method.
# tkinter._test()

# this also creates a window
gui_window = tkinter.Tk()
# set the title
gui_window.title("Hello Python World")
# set the width height left and top offsets
# sets w = 640 h = 480, position 50 pixels from left of screen and 100 pixels from top
# if offset values have minus sign then offset is from right and bottom of screen
gui_window.geometry("640x480+50+100")
# this method is important as it will display the window.
gui_window.mainloop()
