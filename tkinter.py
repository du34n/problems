# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:26:43 2024

@author: duman
"""

import tkinter as tk


root = tk.Tk()

root.geometry('500x500')
root.title('concon')

label = tk.Label(root, text = 'DONDON', font=('Calibri',18))
label.pack(padx = 30, pady = 31)
textbox = tk.Text(root, font=('Arial',10), height = 5)
textbox.pack(padx= 100, pady = 100)
button = tk.Button(root, text = 'alma')
username = tk.Entry(root)
username.pack()
button.pack()

root.mainloop()