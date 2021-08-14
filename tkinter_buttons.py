# -*- coding: utf-8 -*-
"""
another way of handling button events by using the command attribute
function which is called with command - this does not need to be bind
and also this does not need to pass event as argument
"""
import tkinter as tk


def increase():
    value = int(label_value["text"])
    label_value["text"] = f"{value+1}"
    
    
def decrease():
    value = int(label_value["text"])
    label_value["text"] = f"{value-1}"


main_window = tk.Tk()
main_window.rowconfigure(0, minsize=50, weight=1)
main_window.columnconfigure([0,1,2], minsize=50, weight=1)

btn_decrease = tk.Button(master=main_window, text=" - ", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

label_value = tk.Label(master=main_window, text="0")
label_value.grid(row=0, column=1)

btn_increase = tk.Button(master=main_window, text=" + ", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")


main_window.mainloop()   
 