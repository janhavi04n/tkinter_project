# -*- coding: utf-8 -*-
"""
Learn about events and event handlers
To handle events
1. functions called handlers are defined. the logic to be executed when 
the event occurs is defined in these handlers
2. the event handler (keypress, button_click etc) has to be bind to the event
.bind() takes at least 2 args
1. the event to be handled in the format <event_nm>
2. the handler - i.e. name of the function to handle the event
the event handler is bind to the widget
when the event handler is called the event object is passed to the 
event handler function
"""
import tkinter as tk

main_window = tk.Tk()
label_0 = tk.Label(master=main_window, text="Event Handlers Demo", bg="yellow")
label_0.pack()
btn_0 = tk.Button(master=main_window, text="Click Me")
btn_0.pack()


def handle_keypress(event):
    print(event.char)
    
    
def handle_btnclick(event):
    print('Button clicked')


# bind Keypress event to handle_keypress handler
main_window.bind("<Key>", handle_keypress)
# bind right click to handle events for left button click
main_window.bind("<Button-1>", handle_btnclick)

main_window.mainloop()
