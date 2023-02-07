import os

from PIL import ImageTk
from PIL import Image
import tkinter as tk


def next_button(ob, frame, command, padx=0, pady=0):
    ob.loadimage = Image.open('media/button_next.png')
    ob.img = ob.loadimage.resize((105, 35))
    ob.img = ImageTk.PhotoImage(ob.img)
    ob.roundedbutton = tk.Button(frame, image=ob.img, command=command, bg='white', border=0,
                                 activebackground='white')
    ob.roundedbutton.pack(padx=padx, pady=pady)


def back_button(ob, frame, command, padx=0, pady=0):
    ob.loadimage_b = Image.open('media/back_b.png')
    ob.img_b = ob.loadimage_b.resize((105, 35))
    ob.img_b = ImageTk.PhotoImage(ob.img_b)
    ob.roundedbutton_b = tk.Button(frame, image=ob.img_b, command=command, bg='white', border=0,
                                 activebackground='white')
    ob.roundedbutton.pack(padx=padx, pady=pady)
