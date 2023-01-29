import tkinter as tk
from tkinter import ttk
from tkinter import font
from values import *
from PIL import ImageTk, Image
from PIL.Image import Resampling
from tkcalendar import DateEntry


class Page1(tk.Frame):
    def __init__(self, parent, controller, bg=None):
        tk.Frame.__init__(self, parent, bg=bg)
        im = Image.open('media/main_logo.png')
        im = im.resize((250, 250), Resampling.LANCZOS)
        img = ImageTk.PhotoImage(im)
        label = tk.Label(self, image=img, bg='white')
        label.image = img
        label.grid()
        # Pick Department Frame
        choose_dep_frame = tk.Frame(self, bg='#d9d9d9', highlightthickness=1, highlightbackground='grey')
        choose_dep_frame.grid(padx=130, pady=(10, 0), ipady=5/2)

        # canvas = tk.Canvas(choose_dep_frame, bg='#cfcfcf')
        # canvas.grid(ipady=5)

        # Labels
        font1 = font.Font(family = 'Arial', size=-18)

        name_so_label = ttk.Label(choose_dep_frame, text='Назва СО', font=font1)
        name_so_label.grid(row=0, column=0, pady=(33, 0), padx=18)
        departments_label = tk.Label(choose_dep_frame, text='Дільниця', bg='#d9d9d9')
        departments_label.grid(row=0, column=1)
        date_label = tk.Label(choose_dep_frame, text='Дата укладення', bg='#d9d9d9')
        date_label.grid(row=0, column=2)

        # Name Combobox
        name_so_combo = ttk.Combobox(choose_dep_frame, width=27)
        name_so_combo.grid(row=1, column=0, padx=10, pady=5)
        name_so_combo.bind("<<ComboboxSelected>>")

        # Department Combobox
        department_combo = ttk.Combobox(choose_dep_frame, value=[''], width=27)
        department_combo.grid(row=1, column=1, padx=10, pady=5)

        date = DateEntry(choose_dep_frame, width=13)
        date.grid(row=1, column=2, padx=10, pady=5)

        button_next = ttk.Button(self, text='Далі', width=8)
        button_next.grid(pady=5)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame()
        window.pack()

        self.frames = {}
        for F in (Page1,):
            frame = F(window, self, bg='white')
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Page1)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app['bg'] = 'white'
app.state('zoomed')
app.mainloop()
