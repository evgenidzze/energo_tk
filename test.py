import tkinter as tk
from tkinter import ttk
from tkinter import *
from change_docx import dictionary
from PIL import ImageTk, Image
from PIL.Image import Resampling
from change_docx import replace_data
from values import *


class Page1(tk.Frame):
    so_names_lst = get_so()  # {so_name: (id, address, №, date), ...}
    departments_dict = get_departments()
    saved_name = ''
    saved_dep = ''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def pick_dep(e):
            """Create dependent list of departments"""
            departments_lst = []
            val = name_so_combo.get()
            for name in Page1.departments_dict:
                if Page1.so_names_lst[val][0] in Page1.departments_dict[name]:
                    departments_lst.append(name)
            department_combo.config(value=departments_lst)
            return departments_lst

        def save_name_dep():
            dictionary['(ю0.1)'] = name_so_combo.get()[4:-1]
            dictionary['(ю0.2)'] = Page1.departments_dict[department_combo.get()][1]
            controller.show_frame(Page2)
            print(dictionary['(ю0.2)'], dictionary['(ю0.1)'])

        # Pick Department Frame
        choose_dep_frame = LabelFrame(self, text='Оберіть дільницю', font=('Arial', 12))
        choose_dep_frame.grid(padx=180, pady=(160, 0))

        canvas = Canvas(choose_dep_frame, bg='white')
        canvas.grid(ipady=5)

        # Labels
        name_so_label = Label(canvas, text='Назва СО', bg='white')
        name_so_label.grid(row=0, column=0, pady=5)
        departments_label = Label(canvas, text='Дільниця', bg='white')
        departments_label.grid(row=0, column=1)

        # Name Combobox
        name_so_combo = ttk.Combobox(canvas, values=list(Page1.so_names_lst))
        name_so_combo.grid(row=1, column=0, padx=10, pady=5)
        name_so_combo.bind("<<ComboboxSelected>>", pick_dep)

        # Department Combobox
        department_combo = ttk.Combobox(canvas, value=[''])
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

        im = Image.open('media/scheme1.png')
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
            choice = tk.Radiobutton(sec_frame, indicatoron=0, variable=1, image=image, value=value)
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
        tp_num = ttk.Entry(canv_2)
        tp_num.grid(padx=10, pady=5)
        Label(canv_2, text='Потужність', bg='white').grid()
        power = ttk.Entry(canv_2)
        power.grid(padx=10, pady=5)
        Label(canv_2, text='Щитова(ЗКО, ВРЩ)', bg='white').grid()
        zko_vrs = ttk.Entry(canv_2)
        zko_vrs.grid(padx=10, pady=5)
        #
        Label(canv_2, text='Ступінь напруги ТРЕЕ', bg='white').grid(column=1, row=0, sticky='s')
        tree = ttk.Combobox(canv_2, values=('0,22кВ', '0,38кВ'))
        tree.grid(column=1, row=1, padx=10, pady=5)
        Label(canv_2, text='Тип лічильника', bg='white').grid(column=1, row=2)
        type_l = ttk.Entry(canv_2)
        type_l.grid(column=1, row=3, padx=10, pady=5)
        Label(canv_2, text='Початкові показники', bg='white').grid(column=1, row=4)
        indicators = ttk.Entry(canv_2)
        indicators.grid(column=1, row=5, padx=10, pady=5)
        #
        Label(canv_2, text='Струм', bg='white').grid(column=2, row=0, sticky='s')
        stream = ttk.Entry(canv_2)
        stream.grid(column=2, row=1, padx=10, pady=5)
        Label(canv_2, text='Серійний номер лічильника', bg='white').grid(column=2, row=2)
        serial_num = ttk.Entry(canv_2)
        serial_num.grid(column=2, row=3, padx=10, pady=5)
        Label(canv_2, text='Номінал лічильника', bg='white').grid(column=2, row=4)
        par = ttk.Entry(canv_2)
        par.grid(column=2, row=5, padx=10, pady=5)
        #
        Label(canv_2, text='Категорія надійності\nструмоприймачів', bg='white').grid(column=3, row=0, pady=(5, 0))
        category = ttk.Combobox(canv_2, values=('I', 'II', 'III'))
        category.grid(column=3, row=1, padx=10, pady=5)
        Label(canv_2, text='Квартал та рік повірки', bg='white').grid(column=3, row=2)
        cvartal = ttk.Entry(canv_2)
        cvartal.grid(column=3, row=3, padx=10, pady=5)
        Label(canv_2, text='Режим роботи', bg='white').grid(column=3, row=4)
        rezhym = ttk.Entry(canv_2)
        rezhym.grid(column=3, row=5, padx=10, pady=5)
        #
        Canvas(canv_2, bg='grey', height=1, width=600, highlightbackground='white').grid(columnspan=4, pady=10)
        #
        Label(canv_2, text='Номер опори', bg='white').grid()
        num_opory = ttk.Entry(canv_2)
        num_opory.grid(padx=10, pady=5)
        Label(canv_2, text='Номер лінії', bg='white').grid()
        line_num = ttk.Entry(canv_2)
        line_num.grid(padx=10, pady=5)
        Label(canv_2, text='Активний опір лінії', bg='white').grid()
        active_opir = ttk.Entry(canv_2)
        active_opir.grid(padx=10, pady=5)
        #
        Label(canv_2, text='Номер фідера', bg='white').grid(column=1, row=7)
        fider_num = ttk.Entry(canv_2)
        fider_num.grid(column=1, row=8, padx=10, pady=5)
        Label(canv_2, text='Тип лінії', bg='white').grid(column=1, row=9)
        line_type = ttk.Entry(canv_2)
        line_type.grid(column=1, row=10, padx=10, pady=5)
        Label(canv_2, text='Реактивний опір лінії', bg='white').grid(column=1, row=11)
        reactive_opir = ttk.Entry(canv_2)
        reactive_opir.grid(column=1, row=12, padx=10, pady=5)
        #
        Label(canv_2, text='Назва підстанції', bg='white').grid(column=2, row=7)
        substation_name = ttk.Entry(canv_2)
        substation_name.grid(column=2, row=8, padx=10, pady=5)
        Label(canv_2, text='Марка лінії', bg='white').grid(column=2, row=9)
        line_mark = ttk.Entry(canv_2)
        line_mark.grid(column=2, row=10, padx=10, pady=5)
        Label(canv_2, text='Кількість проводів Х Переріз лінії', bg='white').grid(column=2, row=11)
        wire_count = ttk.Entry(canv_2)
        wire_count.grid(column=2, row=12, padx=10, pady=5)

        button_next = Button(self, text='Назад', width=8, command=lambda: controller.show_frame(Page2))
        button_next.pack(side=LEFT, padx=15, anchor='n', pady=(42, 0))

        button_next = tk.Button(self, text='Далі', width=8, command=lambda: controller.show_frame(Page4))
        button_next.pack(side=RIGHT, padx=15, anchor='n', pady=(42, 0))


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def save_data():
            dictionary['ю1'] = full_name.get()
            dictionary['ю0'] = type_obj.get()
            dictionary['ю1.1'] = doc_activity.get()
            dictionary['ю2'] = eis_code.get()
            dictionary['ю3'] = object_address.get()
            dictionary['ю4'] = consumer_name.get()
            if not (abbreviated_name.get()):
                dictionary['ю4.1'] = consumer_name.get()
            else:
                dictionary['ю4.1'] = abbreviated_name.get()
            if legal_address == 'Співпадає з адресою для документообігу':
                dictionary['ю5'] = doc_flow.get()
                dictionary['ю5.1'] = doc_flow.get()
            else:
                dictionary['ю5'] = legal_address.get()
                dictionary['ю5.1'] = legal_address.get()
            dictionary['ю6'] = doc_flow.get()
            dictionary['ю6.1'] = doc_flow.get()
            replace_data()

        object_info = LabelFrame(self, text="Технічна інформація об'єкта", font=('Arial', 12))
        object_info.pack(pady=(10, 0))

        canv_2 = Canvas(object_info, bg='white', width=700, height=400)
        canv_2.pack(ipady=8)

        Label(canv_2, text="Вид об'єкта", bg='white').grid(sticky='s')
        type_obj = ttk.Entry(canv_2)
        type_obj.grid(padx=10, pady=5)
        Label(canv_2, text='ЕІС-код', bg='white').grid()
        eis_code = ttk.Entry(canv_2)
        eis_code.grid(padx=10, pady=5)
        Label(canv_2, text='П.І.Б. споживача', bg='white').grid()
        consumer_name = ttk.Entry(canv_2)
        consumer_name.grid(padx=10, pady=5)
        Label(canv_2, text='Повна назва споживача', bg='white').grid()
        full_name = ttk.Entry(canv_2)
        full_name.grid(padx=10, pady=5)
        Label(canv_2, text='Скорочена повна назва споживача', bg='white').grid(padx=5)
        abbreviated_name = ttk.Entry(canv_2)
        abbreviated_name.grid(padx=10, pady=5)
        Label(canv_2, text='Документ, за яким\nспоживач здійснює діяльність', bg='white').grid(column=1, row=0,
                                                                                               pady=(5, 0))
        doc_activity = ttk.Entry(canv_2)
        doc_activity.grid(column=1, row=1, padx=10, pady=5)
        Label(canv_2, text='Номер договору', bg='white').grid(column=1, row=2)
        contract_num = ttk.Entry(canv_2)
        contract_num.grid(column=1, row=3, padx=10, pady=5)
        Label(canv_2, text="Фактична адреса об'єкту", bg='white').grid(column=1, row=4)
        object_address = ttk.Entry(canv_2)
        object_address.grid(column=1, row=5, padx=10, pady=5)
        Label(canv_2, text='Індекс, Юридична адреса', bg='white').grid(column=1, row=6)
        legal_address = ttk.Combobox(canv_2, values=['Співпадає з адресою для документообігу'], width=35)
        legal_address.grid(column=1, row=7, padx=10, pady=5)
        Label(canv_2, text='Індекс,\nАдреса для документообігу', bg='white').grid(column=1, row=8)
        doc_flow = ttk.Entry(canv_2, width=35)
        doc_flow.grid(column=1, row=9, padx=10, pady=5)

        button_next = Button(self, text='Назад', width=8, command=lambda: controller.show_frame(Page3))
        button_next.pack(side=LEFT, padx=15, anchor='n', pady=(104, 0))

        button_next = tk.Button(self, text='Зберегти', command=save_data)
        button_next.pack(side=RIGHT, padx=15, anchor='n', pady=(104, 0))


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
