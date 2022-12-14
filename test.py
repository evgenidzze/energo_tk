import tkinter as tk
from tkinter import ttk
from tkinter import *

from PIL import ImageTk, Image
from PIL.Image import Resampling

from values import get_names, db


class Page1(tk.Frame):
    so_names_lst = get_names()
    saved_name = ''
    saved_dep = ''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')

        def pick_dep(e):
            """Create dependent list of departments"""
            departments_lst = []
            val = name_so_combo.get()
            for name in db():
                if val in name:
                    departments_lst.append(name[0])
            department_combo.config(value=departments_lst)
            return departments_lst

        def save_name_dep():
            saved_name = name_so_combo.get()
            saved_dep = department_combo.get()
            controller.show_frame(Page2)
            print(saved_dep, saved_name)

        # Pick Department Frame
        choose_dep_frame = LabelFrame(self, text='Оберіть дільницю', bg='white', font=('Arial', 12))
        choose_dep_frame.grid(padx=180, pady=(160, 0), ipady=5)

        # Labels
        name_so_label = Label(choose_dep_frame, text='Назва СО', bg='white')
        name_so_label.grid(row=0, column=0, pady=5)
        departments_label = Label(choose_dep_frame, text='Дільниця', bg='white')
        departments_label.grid(row=0, column=1)

        # Name Combobox
        name_so_combo = ttk.Combobox(choose_dep_frame, values=Page1.so_names_lst)
        name_so_combo.grid(row=1, column=0, padx=10, pady=5)
        name_so_combo.bind("<<ComboboxSelected>>", pick_dep)

        # Department Combobox
        department_combo = ttk.Combobox(choose_dep_frame, value=[''])
        department_combo.grid(row=1, column=1, padx=10, pady=5)

        button_next = tk.Button(self, bd=1, text='Далі', width=8, command=save_name_dep)
        button_next.grid(pady=5)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        scheme_frame = LabelFrame(self, text='Оберіть схему', font=('Arial', 12))
        scheme_frame.pack(fill=BOTH, pady=10)

        canvas = Canvas(scheme_frame, width=700, height=400)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = Scrollbar(scheme_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        sec_frame = Frame(canvas, bg='white')
        canvas.create_window((0, 0), window=sec_frame, anchor='nw')

        def on_mouse_wheel(event):
            """Mouse wheel"""
            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        im = Image.open('scheme1.png')
        im = im.resize((110, 170), Resampling.LANCZOS)
        image = ImageTk.PhotoImage(im)

        # schemes list
        column = 0
        row = 0
        value = 0
        for i in range(15):
            if column == 5:
                row += 1
                column = 0
            choice = tk.Radiobutton(sec_frame, indicatoron=0,
                                    variable=1,
                                    image=image,
                                    value=value)
            choice.image = image
            choice.grid(row=row, column=column, padx=10, pady=10)
            column += 1
            value += 1

        button_next = Button(self, text='Далі', width=8, command=lambda: controller.show_frame(Page3))
        button_next.pack(side=RIGHT, padx=15)

        button_back = Button(self, text='Назад', width=8, command=lambda: controller.show_frame(Page1))
        button_back.pack(side=LEFT, padx=15)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        object_info = LabelFrame(self, text="Технічна інформація об'єкта", font=('Arial', 12))
        object_info.pack(pady=(10, 0))

        canv_2 = Canvas(object_info, bg='white', width=700, height=400)
        canv_2.pack(ipady=8)

        Label(canv_2, text='Номер ТП', bg='white').grid(sticky='s')
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        Label(canv_2, text='Потужність', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        Label(canv_2, text='Щитова(ЗКО, ВРЩ)', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        #
        Label(canv_2, text='Ступінь напруги ТРЕЕ', bg='white').grid(column=1, row=0, sticky='s')
        ttk.Combobox(canv_2).grid(column=1, row=1, padx=10, pady=5)
        Label(canv_2, text='Тип лічильника', bg='white').grid(column=1, row=2)
        ttk.Entry(canv_2).grid(column=1, row=3, padx=10, pady=5)
        Label(canv_2, text='Початкові показники', bg='white').grid(column=1, row=4)
        ttk.Entry(canv_2).grid(column=1, row=5, padx=10, pady=5)
        #
        Label(canv_2, text='Струм', bg='white').grid(column=2, row=0, sticky='s')
        ttk.Entry(canv_2).grid(column=2, row=1, padx=10, pady=5)
        Label(canv_2, text='Серійний номер лічильника', bg='white').grid(column=2, row=2)
        ttk.Entry(canv_2).grid(column=2, row=3, padx=10, pady=5)
        Label(canv_2, text='Номінал лічильника', bg='white').grid(column=2, row=4)
        ttk.Entry(canv_2).grid(column=2, row=5, padx=10, pady=5)
        #
        Label(canv_2, text='Категорія надійності\nструмоприймачів', bg='white').grid(column=3, row=0, pady=(5, 0))
        ttk.Combobox(canv_2).grid(column=3, row=1, padx=10, pady=5)
        Label(canv_2, text='Квартал та рік повірки', bg='white').grid(column=3, row=2)
        ttk.Entry(canv_2).grid(column=3, row=3, padx=10, pady=5)
        Label(canv_2, text='Режим роботи', bg='white').grid(column=3, row=4)
        ttk.Entry(canv_2).grid(column=3, row=5, padx=10, pady=5)
        #
        Canvas(canv_2, bg='grey', height=1, width=600, highlightbackground='white').grid(columnspan=4, pady=10)
        #
        Label(canv_2, text='Номер опори', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        Label(canv_2, text='Номер лінії', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        Label(canv_2, text='Активний опір лінії', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        #
        Label(canv_2, text='Номер фідера', bg='white').grid(column=1, row=7)
        ttk.Entry(canv_2).grid(column=1, row=8, padx=10, pady=5)
        Label(canv_2, text='Тип лінії', bg='white').grid(column=1, row=9)
        ttk.Entry(canv_2).grid(column=1, row=10, padx=10, pady=5)
        Label(canv_2, text='Реактивний опір лінії', bg='white').grid(column=1, row=11)
        ttk.Entry(canv_2).grid(column=1, row=12, padx=10, pady=5)
        #
        Label(canv_2, text='Назва підстанції', bg='white').grid(column=2, row=7)
        ttk.Entry(canv_2).grid(column=2, row=8, padx=10, pady=5)
        Label(canv_2, text='Марка лінії', bg='white').grid(column=2, row=9)
        ttk.Entry(canv_2).grid(column=2, row=10, padx=10, pady=5)
        Label(canv_2, text='Кількість проводів Х Переріз лінії', bg='white').grid(column=2, row=11)
        ttk.Entry(canv_2).grid(column=2, row=12, padx=10, pady=5)

        button_next = Button(self, text='Назад', width=8, command=lambda: controller.show_frame(Page2))
        button_next.pack(side=LEFT, padx=15, anchor='n', pady=10)

        button_next = tk.Button(self, text='Далі', width=8, command=lambda: controller.show_frame(Page4))
        button_next.pack(side=RIGHT, padx=15, anchor='n', pady=10)


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        object_info = LabelFrame(self, text="Технічна інформація об'єкта", font=('Arial', 12))
        object_info.pack(pady=(10, 0))

        canv_2 = Canvas(object_info, bg='white', width=700, height=400)
        canv_2.pack(ipady=8)

        Label(canv_2, text="Вид об'єкта", bg='white').grid(sticky='s')
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        Label(canv_2, text='ЕІС-код', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        Label(canv_2, text='П.І.Б. споживача', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        Label(canv_2, text='Повна назва споживача', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)
        Label(canv_2, text='Скорочена повна назва споживача', bg='white').grid()
        ttk.Entry(canv_2).grid(padx=10, pady=5)

        Label(canv_2, text='Документ, за яким\nспоживач здійснює діяльність', bg='white').grid(column=1, row=0,
                                                                                               sticky='s')
        ttk.Combobox(canv_2).grid(column=1, row=1, padx=10, pady=5)
        Label(canv_2, text='Номер договору', bg='white').grid(column=1, row=2)
        ttk.Entry(canv_2).grid(column=1, row=3, padx=10, pady=5)
        Label(canv_2, text="Фактична адреса об'єкту", bg='white').grid(column=1, row=4)
        ttk.Entry(canv_2).grid(column=1, row=5, padx=10, pady=5)
        Label(canv_2, text='Індекс, Юридична адреса', bg='white').grid(column=1, row=6)
        ttk.Combobox(canv_2).grid(column=1, row=7, padx=10, pady=5)
        Label(canv_2, text='Індекс,\nАдреса для документообігу', bg='white').grid(column=1, row=8)
        ttk.Entry(canv_2).grid(column=1, row=9, padx=10, pady=5)

        button_next = Button(self, text='Назад', width=8, command=lambda: controller.show_frame(Page3))
        button_next.pack(side=LEFT, padx=15, anchor='n', pady=10)

        button_next = tk.Button(self, text='На головну', command=lambda: controller.show_frame(Page1))
        button_next.pack(side=RIGHT, padx=15, anchor='n', pady=10)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)
        window.pack()
        self.frames = {}
        for F in (Page1, Page2, Page3, Page4):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Page1)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.geometry("750x500")
app.configure()
app.mainloop()
