import tkinter as tk
from tkinter import messagebox


def get_button(window,text,colour, command, fg = "white"):
    button = tk.Button(
        window,
        text=text,
        command= command,
        activebackground="black",
        activeforeground="white",
        fg=fg,
        bg=colour,
        height=1,
        width=20,
        font=("Helvetica bold",20)
        )

    return button

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0,column=0)
    return label

def get_text_label(window,text):
    label =tk.Label(window,text=text)
    label.config(font=("sans-serif",20), justify ="left")
    return label

def get_entry_text(window):
    inputtxt =tk.Text(window,
                      height = 1,
                      width = 15,
                      font=("Arial",30))
    return inputtxt

def msg_box(title, description):
    messagebox.showinfo(title,description)
