# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:03:48 2024

@author: gencyetenek
"""

import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.listuple = ("a","b","c","d")  
        self.window = tk.Tk()

        self.label = tk.Label(self.window, text = "CONCON", font=('Calibri',20))
        self.label.pack(padx = 20, pady=20)
        self.elements = tk.StringVar()
        self.listbox = tk.Listbox(self.window,width=50,height=5,listvariable=self.elements)
        self.elements.set(self.listuple)
        self.listbox.pack(pady=50)
        self.textbox = tk.Text(self.window, font=('Calibri',15),height=5)
        self.textbox.bind("<KeyPress>",self.shortcut)
        self.textbox.pack(pady= 30, padx=30)
        self.checkState = tk.IntVar()     
        self.check = tk.Checkbutton(self.window, text="check this", font=('Calibri',15),variable=self.checkState)
        self.check.pack()
        self.button = tk.Button(self.window,text = "whoami",font=('Calibri',15), command=self.showMessage)
        self.button.pack(pady=20)
        self.window.mainloop()
    def showMessage(self):
        if(self.checkState.get() == 1):
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message",message=self.textbox.get("1.0",tk.END))
    def shortcut(self,event):
        if((event.state == 4) & (event.keysym == "Return")):
            self.showMessage()
        print(event)


MyGUI()