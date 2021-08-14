# -*- coding: utf-8 -*-
"""
understanding geometry managers
assignment - create a address entry form
"""
import tkinter as tk

address_window = tk.Tk()
address_window.title("Address Entry Form")

label_names = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:"
]

form_frame = tk.Frame(master=address_window)
form_frame.pack(fill=tk.BOTH)

for idx, label_nm in enumerate(label_names):
    form_label = tk.Label(master=form_frame, text=label_nm)
    form_label.grid(row=idx, column=0, sticky="e")
    form_text = tk.Entry(master=form_frame)
    form_text.grid(row=idx, column=1, sticky="nsew")
    
btn_frame = tk.Frame(master=address_window)
btn_frame.pack(fill=tk.X, padx=5, pady=5)

btn_submit = tk.Button(master=btn_frame, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, pady=10)

btn_clear = tk.Button(master=btn_frame, text="Clear")
btn_clear.pack(side=tk.RIGHT, padx=10)


address_window.mainloop()
