from tkinter import Label
from PIL import ImageTk, Image
from PIL.Image import Resampling
from tktooltip import ToolTip
import tkinter as tk


def tooltip_grid(self, msg, column=0, row=0, padx=0, pady=0):
    tooltip_img = Image.open('media/tooltip.png')
    tooltip_img = tooltip_img.resize((20, 20), Resampling.LANCZOS)
    tooltip_img = ImageTk.PhotoImage(tooltip_img)
    tooltip_label = Label(self, image=tooltip_img, bg='#C7E4FF')
    tooltip_label.image = tooltip_img
    tooltip_label.grid(column=column, row=row, sticky='e', padx=padx, pady=pady)
    ToolTip(tooltip_label, msg=msg)
