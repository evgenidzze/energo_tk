import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter import *
from change_docx import dictionary
from PIL import ImageTk, Image
from PIL.Image import Resampling
from change_docx import replace_data
from styles.button_next import next_button, back_button
from values import *
from pathlib import Path
from tkcalendar import DateEntry
import locale

locale.setlocale(locale.LC_ALL, 'uk_UA')


class Page1(tk.Frame):
    so_names_lst = get_so()  # {so_name: (id, address, №, date), ...}
    departments_dict = get_departments()  # {department: [so_id, code, address], ...}
    saved_name = ''
    saved_dep = ''

    def __init__(self, parent, controller, bg=None):
        tk.Frame.__init__(self, parent, bg='white')

        def pick_dep(e):
            """Create dependent list of departments"""
            departments_lst = []
            val = name_so_combo.get()
            for name in Page1.departments_dict:
                if Page1.so_names_lst[val][0] in Page1.departments_dict[name]:
                    departments_lst.append(name)
            department_combo.config(value=departments_lst)
            dictionary['і_б_директора'] = Page1.so_names_lst[val][1].split(',')[1].strip()
            dictionary['повне_директора'] = Page1.so_names_lst[val][1].split(',')[0]
            return departments_lst

        def save_name_dep():
            dictionary['ю0_1'] = name_so_combo.get()[4:-1]
            dictionary['ю0_2'] = Page1.departments_dict[department_combo.get()][1]
            f_date = date.get_date()
            dictionary['число'] = f_date.strftime("%d")
            dictionary['місяця'] = rod_months[f_date.strftime("%B")][0]
            dictionary['місяць'] = f_date.strftime("%B")
            dictionary['міс_цифра'] = rod_months[f_date.strftime("%B")][1]
            dictionary['рік'] = f_date.strftime("%Y")
            dictionary['адреса_оператора'] = Page1.departments_dict[department_combo.get()][2]
            controller.show_frame(Page2)

        im = Image.open('media/main_logo.png')
        im = im.resize((380, 380), Resampling.LANCZOS)
        img = ImageTk.PhotoImage(im)
        label = Label(self, image=img, bg='white')
        label.image = img
        label.grid(padx=(250, 0))
        # Pick Department Frame
        # choose_dep_frame = tk.Canvas(self)
        # choose_dep_frame.grid(padx=130, pady=(10, 0), ipady=10)

        choose_dep_label = Label(self, text='Оберіть дільницю', font=('', 14), bg='white')
        choose_dep_label.grid(row=1, column=0, pady=5, padx=(30, 0))

        # lines near name
        Canvas(self, height=2, width=40, highlightbackground='white', bg='#D9DEED').grid(row=1, column=0, padx=(0, 185))
        Canvas(self, height=2, width=250, highlightbackground='white', bg='#D9DEED').grid(row=1, column=0,
                                                                                          padx=(460, 0))

        canvas = Canvas(self, bg='#D9DEED')
        canvas.grid(row=2, column=0, ipady=8, padx=(250, 0), ipadx=11)

        # Labels
        name_so_label = Label(canvas, text='Назва СО', bg='#D9DEED')
        name_so_label.grid(row=0, column=0, pady=(15, 5))
        departments_label = Label(canvas, text='Дільниця', bg='#D9DEED')
        departments_label.grid(row=0, column=1, pady=(15, 5))
        date_label = Label(canvas, text='Дата укладення', bg='#D9DEED')
        date_label.grid(row=0, column=2, pady=(15, 5))

        # Name So Combobox
        name_so_combo = ttk.Combobox(canvas, values=list(Page1.so_names_lst), width=27)
        name_so_combo.grid(row=1, column=0, padx=(23, 15), pady=5)
        name_so_combo.bind("<<ComboboxSelected>>", pick_dep)

        # Department Combobox
        department_combo = ttk.Combobox(canvas, value=[''], width=27)
        department_combo.grid(row=1, column=1, pady=5)

        # Date
        date = DateEntry(canvas)
        date.grid(row=1, column=2, pady=5, padx=(15, 0))

        footer_frame = tk.Frame(self, background="white")
        footer_frame.grid(pady=(190, 0), padx=(210, 0), sticky='se', column=1)

        # self повернути і буде кнопка

        next_button(self, footer_frame, save_name_dep)
        # button_next = ttk.Button(self, text='>', width=10, command=save_name_dep)
        # button_next.grid(pady=5)


class Page2(tk.Frame):
    def __init__(self, parent, controller, bg=None):
        tk.Frame.__init__(self, parent, bg=bg)
        choose_dep_label = Label(self, text='Оберіть схему', font=('', 14), bg='white')
        choose_dep_label.pack(pady=(80, 5), padx=(0, 620))

        # lines near label
        Canvas(self, height=2, width=55, highlightbackground='white', bg='#D9DEED').place(x=150, y=92)
        Canvas(self, height=2, width=480, highlightbackground='white', bg='#D9DEED').place(x=365, y=92)

        self.scheme_frame = Canvas(self, bg='#D9DEED')
        self.scheme_frame.pack(padx=(0, 170))

        canvas = Canvas(self.scheme_frame, width=740, height=480, bg='#D9DEED')
        canvas.pack(side=LEFT, fill=BOTH, expand=1, pady=20, padx=20)

        scrollbar = Scrollbar(self.scheme_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        sec_frame = tk.Frame(canvas, bg='#D9DEED')
        canvas.create_window((0, 0), window=sec_frame, anchor='nw')

        def on_mouse_wheel(event):
            """Mouse wheel"""
            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        folder_dir = 'media/schemes'
        images = Path(folder_dir).glob('*.png')

        column = 0
        row = 0
        value = 0
        # for i in images:  # show real schemes
        for i in range(12):  # show how it looks with 15 schemes
            im = Image.open('media/schemes/scheme_new.png')
            im = im.resize((158, 220), Resampling.LANCZOS)
            image = ImageTk.PhotoImage(im)
            if column == 4:
                row += 1
                column = 0
            choice = tk.Radiobutton(sec_frame, indicatoron=0, borderwidth=1 / 15, bg='#7989BE', variable=1,
                                    image=image,
                                    value=value,
                                    relief=GROOVE)
            choice.image = image
            choice.grid(row=row, column=column, padx=12, pady=10)
            column += 1
            value += 1

        # button_next = ttk.Button(self, text='Далі', width=8, command=lambda: controller.show_frame(Page3))
        # button_next.pack(side=RIGHT, padx=15)
        self.next_b = Image.open('media/button_next.png').resize((105, 35))
        self.img_n = ImageTk.PhotoImage(self.next_b)
        next_b = Button(self, image=self.img_n, command=lambda: controller.show_frame(Page3), bg='white', border=0,
               activebackground='white')
        next_b.place(x=750, y=650)

        self.back_b = Image.open('media/back_b.png').resize((105, 35))
        self.img_b = ImageTk.PhotoImage(self.back_b)
        next_b = Button(self, image=self.img_b, command=lambda: controller.show_frame(Page1), bg='white', border=0,
                        activebackground='white')
        next_b.place(x=100, y=650)

        # next_button(self, frame=self, command=lambda: controller.show_frame(Page3), )
        # back_button(self, frame=self, command=lambda: controller.show_frame(Page3), padx=100, pady=650)
        # back_button(self, frame=self, command=lambda: controller.show_frame(Page1))


class Page3(tk.Frame):
    def __init__(self, parent, controller, bg=None):
        def save_data():
            dictionary['т1'] = tp_num.get()
            dictionary['т1_1'] = trans_power.get()
            dictionary['т4'] = power.get()
            dictionary['с3'] = zko_vrs.get()
            dictionary['т2'] = tree.get()
            if dictionary['т2'] == '0,22':
                dictionary['т2_1'] = '1'
            elif dictionary['т2'] == '0,38':
                dictionary['т2_1'] = '3'
            dictionary['т6'] = type_l.get()
            dictionary['т9'] = indicators.get()
            dictionary['т3'] = stream.get()
            dictionary['т7'] = serial_num.get()
            dictionary['т7_2'] = par.get()
            dictionary['т5'] = category.get()
            dictionary['т7_1'] = cvartal.get()
            dictionary['т8'] = rezhym.get()
            dictionary['т10'] = num_opory.get()
            dictionary['т11'] = line_num.get()
            dictionary['т12'] = line_length.get()
            dictionary['т12_1'] = int(line_length.get()) / 1000
            dictionary['р1'] = active_opir.get()
            dictionary['с1'] = fider_num.get()
            dictionary['л1'] = line_type.get()
            dictionary['р2'] = reactive_opir.get()
            dictionary['с2'] = substation_name.get()
            dictionary['л1_2'] = line_mark.get()
            dictionary['л2'] = wire_count.get()
            if line_type.get() == 'КЛ':
                dictionary['т99'] = "в місці кріплення кабелю живлення"
            elif line_type.get() in ('ПЛ', 'ПЛІ'):
                dictionary['т99'] = "в місці кріплення проводів ЛЕП"
            controller.show_frame(Page4)

        tk.Frame.__init__(self, parent, bg=bg)
        object_info = ttk.LabelFrame(self, text="Технічна інформація об'єкта")
        object_info.pack(pady=(10, 0))

        canv_2 = Canvas(object_info, bg='white', width=700, height=400)
        canv_2.pack(ipady=8)

        Label(canv_2, text='Номер ТП', bg='white').grid(sticky='s')
        tp_num = ttk.Entry(canv_2)
        tp_num.grid(padx=10, pady=5)
        Label(canv_2, text='Потужність', bg='white').grid()
        power = ttk.Entry(canv_2)
        power.grid(padx=10, pady=5)
        Label(canv_2, text='Щитова', bg='white').grid()
        zko_vrs = ttk.Combobox(canv_2, values=('ЗКО', 'ВРЩ'))
        zko_vrs.grid(padx=10, pady=5)
        #
        Label(canv_2, text='Ступінь напруги ТРЕЕ', bg='white').grid(column=1, row=0, sticky='s')
        tree = ttk.Combobox(canv_2, values=('0,22', '0,38'))
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
        Canvas(canv_2, height=1, width=600, highlightbackground='white').grid(columnspan=4, pady=10)
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
        line_type = ttk.Combobox(canv_2, values=('КЛ', 'ПЛ', 'ПЛІ'))
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

        Label(canv_2, text='Довжина лінії', bg='white').grid(column=3, row=7)
        line_length = ttk.Entry(canv_2)
        line_length.grid(column=3, row=8, padx=10, pady=5)
        Label(canv_2, text='Повна потужність\nтрансформатора', bg='white').grid(column=3, row=9)
        trans_power = ttk.Entry(canv_2)
        trans_power.grid(column=3, row=10, padx=10, pady=5)

        button_next = ttk.Button(self, text='Назад', width=8, command=lambda: controller.show_frame(Page2))
        button_next.pack(side=LEFT, padx=15, anchor='n', pady=(42, 0))

        button_next = ttk.Button(self, text='Далі', width=8, command=save_data)
        button_next.pack(side=RIGHT, padx=15, anchor='n', pady=(42, 0))


class Page4(tk.Frame):
    def __init__(self, parent, controller, bg=None):
        tk.Frame.__init__(self, parent, bg=bg)

        def save_data():
            dictionary['ю1'] = full_name.get()
            dictionary['ю0'] = type_obj.get()
            dictionary['ю1_1'] = doc_activity.get()
            dictionary['ю2'] = eis_code.get()
            dictionary['ю3'] = object_address.get()
            dictionary['ю4'] = consumer_name.get()
            dictionary['ю6'] = doc_flow.get()
            if not (abbreviated_name.get()):
                dictionary['ю4_1'] = consumer_name.get()
            else:
                dictionary['ю4_1'] = abbreviated_name.get()
            if legal_address.get() == 'Співпадає з адресою для документообігу':
                dictionary['ю5'] = doc_flow.get()
            else:
                dictionary['ю5'] = legal_address.get()
            dictionary['н_д'] = contract_num.get()
            replace_data()

        object_info = ttk.LabelFrame(self, text="Інформація об'єкта")
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

        button_next = ttk.Button(self, text='Назад', width=8, command=lambda: controller.show_frame(Page3))
        button_next.pack(side=LEFT, padx=15, anchor='n', pady=(104, 0))

        button_next = ttk.Button(self, text='Зберегти', command=save_data)
        button_next.pack(side=RIGHT, padx=15, anchor='n', pady=(104, 0))


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        menubar = Menu(self)
        menubar.add_command(label="Інформація", command=info_window)
        self.config(menu=menubar)

        window = tk.Frame(self, bg='white', height=750, width=1200)
        window.grid(padx=250)
        window.grid_propagate(0)
        self.frames = {}
        for F in (Page1, Page2, Page3, Page4):
            frame = F(window, self, bg='white')
            self.frames[F] = frame
            frame.grid(row=0, column=0, ipadx=50, sticky='nsew')

        # default is Page1
        self.show_frame(Page2)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


def info_window():
    new_window = Toplevel(app)
    new_window.title('Інформація')
    new_window.geometry('200x100')
    Label(new_window, text='AutoContract\n'
                           'Автор: Сметанюк Є.О.', font=('Arial', 10)).pack()
    link = Label(new_window, text='Telegram', fg='blue', cursor='hand2')
    link.pack()
    link.bind("<Button-1>", lambda e: webbrowser.open_new('https://t.me/evgenidzee'))


app = Application()
s = ttk.Style()
s.configure('TFrame', background='white', )
s.configure('TLabelFrame', background='white')
app.configure(bg='white')
app.state('zoomed')
app.mainloop()
