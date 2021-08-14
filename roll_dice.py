# -*- coding: utf-8 -*-
"""
roll the dice - button click mimic the roll of dice - any number b/w 1 and 6
buttons event practice
"""
import tkinter as tk
import random as r


def roll_dice():
    value = r.randint(1, 6)
    lbl_value["text"] = f"{value}"

main_window = tk.Tk()

lbl_value = tk.Label(master=main_window, text=" ")
lbl_value.pack()

btn_dice = tk.Button(master=main_window, text="Roll the Dice", command=roll_dice)
btn_dice.pack(fill=tk.BOTH)

main_window.mainloop()
