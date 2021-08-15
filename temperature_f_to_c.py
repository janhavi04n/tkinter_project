# -*- coding: utf-8 -*-
"""
enter temp in F and convert to C
"""
import tkinter as tk


def convert_fahrenheit_to_celsius():
    fahrenheit = ent_temp.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_c["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


main_window = tk.Tk()
main_window.title("Temperature Converter")

f_frame = tk.Frame(master=main_window)

ent_temp = tk.Entry(master=f_frame, width=10)
lbl_f = tk.Label(master=f_frame, text="\N{DEGREE FAHRENHEIT}")
ent_temp.grid(row=0, column=0, sticky="e")
lbl_f.grid(row=0, column=1, sticky="w")

btn_converter = tk.Button(master=main_window, text="\N{RIGHTWARDS BLACK ARROW}",
                          command=convert_fahrenheit_to_celsius)
lbl_c = tk.Label(master=main_window, text="\N{DEGREE CELSIUS}")

f_frame.grid(row=0, column=0, padx=10)
btn_converter.grid(row=0, column=1, pady=10)
lbl_c.grid(row=0, column=2, padx=10)

main_window.mainloop()