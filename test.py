import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter import *

from change_docx import dictionary
from PIL import ImageTk, Image
from PIL.Image import Resampling
from change_docx import replace_data
from page_option import Page3Scheme1, Page3Scheme2
from styles.button_next import next_button, back_button, save_button
from values import *
from pathlib import Path
from tkcalendar import DateEntry
import locale

from tooltip import tooltip_grid
from shemes_counter import row_counts

locale.setlocale(locale.LC_ALL, 'uk_UA')


class Page1(tk.Frame):
    so_names_lst = get_so()  # {so_name: (id, address, №, date), ...}
    departments_dict = get_departments()  # {department: [so_id, code, address], ...}
    saved_name = ''
    saved_dep = ''

    def __init__(self, parent, controller, bg=None, next_page=None, prev_page=None):
        tk.Frame.__init__(self, parent, bg=bg)

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

        main_frame = Frame(self, bg='white')
        main_frame.pack()

        im = Image.open('media/main_logo.png')
        im = im.resize((380, 380), Resampling.LANCZOS)
        img = ImageTk.PhotoImage(im)
        label = Label(main_frame, image=img, bg='white')
        label.image = img
        label.grid()
        # Pick Department Frame

        title_frame = Frame(main_frame, bg='white')
        title_frame.grid()
        choose_dep_label = Label(title_frame, text='Оберіть дільницю', font=('', 14), bg='white')
        choose_dep_label.grid(row=1, column=0, pady=5, padx=(0, 200))
        Canvas(title_frame, height=1, width=40, highlightbackground='white', bg='#007AFF').grid(row=1, column=0,
                                                                                                padx=(0, 420), pady=(2, 0))
        Canvas(title_frame, height=1, width=250, highlightbackground='white', bg='#007AFF').grid(row=1, column=0,
                                                                                                 padx=(230, 0), pady=(2, 0))
        canvas = Frame(main_frame, background='#C7E4FF', highlightthickness=1, highlightbackground="#007AFF")
        canvas.grid(ipady=8, ipadx=11)

        # Labels
        name_so_label = ttk.Label(canvas, text='Назва СО')
        name_so_label.grid(row=0, column=0, pady=(15, 5))
        departments_label = ttk.Label(canvas, text='Дільниця')
        departments_label.grid(row=0, column=1, pady=(15, 5))
        date_label = ttk.Label(canvas, text='Дата укладення')
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

        # self повернути і буде кнопка

        next_button(self, self, save_name_dep)

        # button_next = ttk.Button(self, text='>', width=10, command=save_name_dep)
        # button_next.grid(pady=5)


class Page2(tk.Frame):

    def __init__(self, parent, controller, bg=None, next_page=None, prev_page=None):
        tk.Frame.__init__(self, parent, bg=bg)

        level_var = tk.IntVar()

        # title frame
        title_frame = Frame(self, bg='white')
        title_frame.pack()
        choose_dep_label = Label(title_frame, text='Оберіть схему', font=('', 14), bg='white')
        choose_dep_label.pack(pady=(30, 5), padx=(102, 510))
        Canvas(title_frame, height=2, width=55, highlightbackground='white', bg='#D9DEED').place(x=40, y=42)
        Canvas(title_frame, height=2, width=460, highlightbackground='white', bg='#D9DEED').place(x=240, y=42)

        self.schemes_frame = Frame(self, bg='#C7E4FF', highlightthickness=1, highlightbackground='#007AFF')
        self.schemes_frame.pack()

        self.canvas = Canvas(self.schemes_frame, bg='#C7E4FF', highlightthickness=0, width=650,
                             height=305 * row_counts())
        scrollbar = ttk.Scrollbar(self.schemes_frame, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.canvas.yview)
        self.canvas.pack(side=LEFT, pady=20, padx=20, fill=BOTH)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.sec_frame = tk.Frame(self.canvas, bg='#C7E4FF')
        self.canvas.create_window((0, 0), window=self.sec_frame, anchor='nw')

        def on_mouse_wheel(event):
            """Mouse wheel"""
            self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
            return "break"

        self.canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        folder_dir = 'media/schemes'
        images = Path(folder_dir).glob('*.png')

        def page_3_variant():
            scheme_value = level_var.get()
            if scheme_value == 1:
                return Page3Scheme1
            elif scheme_value == 2:
                return Page3Scheme2
            else:
                return Page3Scheme1

        column = 0
        row = 0
        value = 1

        for i in images:  # show real schemes
            #     print(i)
            # for i in range(5):  # show how it looks with 15 schemes
            im = Image.open(i)
            # im = Image.open(folder_dir + '/scheme_new.png')
            im = im.resize((190, 264), Resampling.LANCZOS)
            image = ImageTk.PhotoImage(im)
            if column == 3:
                row += 1
                column = 0
            choice = tk.Radiobutton(self.sec_frame, indicatoron=False, borderwidth=1 / 15, bg='#7989BE',
                                    variable=level_var,
                                    image=image,
                                    value=value, selectcolor='yellow', command=page_3_variant)
            choice.image = image
            choice.grid(row=row, column=column, padx=12, pady=(0, 20), sticky='n')

            # scheme name
            Label(self.sec_frame, text=f'Схема', font=('', 12), bg='#C7E4FF').grid(row=row, column=column,
                                                                                   pady=(275, 10))
            tooltip_grid(self.sec_frame, msg='Інформація про схему', row=row, column=column, pady=(265, 0),
                         padx=(0, 25))
            column += 1
            value += 1

        back_button(self, self, command=lambda: controller.show_frame(Page1))
        next_button(self, self, command=lambda: controller.show_frame(page_3_variant()))


# class Page3(tk.Frame):
#     def __init__(self, parent, controller, bg=None):
# def save_data():
#     dictionary['т1'] = tp_num.get()
#     dictionary['т1_1'] = trans_power.get()
#     dictionary['т4'] = power.get()
#     dictionary['с3'] = zko_vrs.get()
#     dictionary['т2'] = tree.get()
#     if dictionary['т2'] == '0,22':
#         dictionary['т2_1'] = '1'
#     elif dictionary['т2'] == '0,38':
#         dictionary['т2_1'] = '3'
#     dictionary['т6'] = type_l.get()
#     dictionary['т9'] = indicators.get()
#     dictionary['т3'] = stream.get()
#     dictionary['т7'] = serial_num.get()
#     dictionary['т7_2'] = par.get()
#     dictionary['т5'] = category.get()
#     dictionary['т7_1'] = cvartal.get()
#     dictionary['т8'] = rezhym.get()
#     dictionary['т10'] = num_opory.get()
#     dictionary['т11'] = line_num.get()
#     dictionary['т12'] = line_length.get()
#     dictionary['т12_1'] = int(line_length.get()) / 1000
#     dictionary['р1'] = active_opir.get()
#     dictionary['с1'] = fider_num.get()
#     dictionary['л1'] = line_type.get()
#     dictionary['р2'] = reactive_opir.get()
#     dictionary['с2'] = substation_name.get()
#     dictionary['л1_2'] = line_mark.get()
#     dictionary['л2'] = wire_count.get()
#     if line_type.get() == 'КЛ':
#         dictionary['т99'] = "в місці кріплення кабелю живлення"
#     elif line_type.get() in ('ПЛ', 'ПЛІ'):
#         dictionary['т99'] = "в місці кріплення проводів ЛЕП"
#     controller.show_frame(Page4)

# tk.Frame.__init__(self, parent, bg=bg)
#
# title_frame = Frame(self, bg='white')
# title_frame.pack(padx=(250, 0))
# choose_dep_label = Label(title_frame, text="Технічна інформація об'єкта", font=('', 14), bg='white')
# choose_dep_label.pack(pady=(80, 5), padx=(102, 600))
# Canvas(title_frame, height=2, width=55, highlightbackground='white', bg='#D9DEED').place(x=40, y=92)
# Canvas(title_frame, height=2, width=300, highlightbackground='white', bg='#D9DEED').place(x=360, y=92)
# self.frame_for_entries_3 = ttk.Frame(self)
# self.frame_for_entries_3.pack(ipady=8)

# ttk.Label(self.frame_for_entries_3, text='Номер ТП').grid(sticky='s')
# tp_num = ttk.Entry(self.frame_for_entries_3)
# tp_num.grid(padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Потужність').grid()
# power = ttk.Entry(self.frame_for_entries_3)
# power.grid(padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Щитова').grid()
# zko_vrs = ttk.Combobox(self.frame_for_entries_3, values=('ЗКО', 'ВРЩ'))
# zko_vrs.grid(padx=10, pady=5)
# #
# ttk.Label(self.frame_for_entries_3, text='Ступінь напруги ТРЕЕ').grid(column=1, row=0, sticky='s')
# tree = ttk.Combobox(self.frame_for_entries_3, values=('0,22', '0,38'))
# tree.grid(column=1, row=1, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Тип лічильника').grid(column=1, row=2)
# type_l = ttk.Entry(self.frame_for_entries_3)
# type_l.grid(column=1, row=3, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Початкові показники').grid(column=1, row=4)
# indicators = ttk.Entry(self.frame_for_entries_3)
# indicators.grid(column=1, row=5, padx=10, pady=5)
# #
# ttk.Label(self.frame_for_entries_3, text='Струм').grid(column=2, row=0, sticky='s')
# stream = ttk.Entry(self.frame_for_entries_3)
# stream.grid(column=2, row=1, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Серійний номер лічильника').grid(column=2, row=2)
# serial_num = ttk.Entry(self.frame_for_entries_3)
# serial_num.grid(column=2, row=3, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Номінал лічильника').grid(column=2, row=4)
# par = ttk.Entry(self.frame_for_entries_3)
# par.grid(column=2, row=5, padx=10, pady=5)
# #
# ttk.Label(self.frame_for_entries_3, text='Категорія надійності\nструмоприймачів').grid(column=3, row=0,
#                                                                                        pady=(5, 0))
# category = ttk.Combobox(self.frame_for_entries_3, values=('I', 'II', 'III'))
# category.grid(column=3, row=1, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Квартал та рік повірки').grid(column=3, row=2)
# cvartal = ttk.Entry(self.frame_for_entries_3)
# cvartal.grid(column=3, row=3, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Режим роботи').grid(column=3, row=4)
# rezhym = ttk.Entry(self.frame_for_entries_3)
# rezhym.grid(column=3, row=5, padx=10, pady=5)
# #
# Canvas(self.frame_for_entries_3, height=1, width=600, highlightbackground='white').grid(columnspan=4, pady=10)
# #
# ttk.Label(self.frame_for_entries_3, text='Номер опори').grid()
# num_opory = ttk.Entry(self.frame_for_entries_3)
# num_opory.grid(padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Номер лінії').grid()
# line_num = ttk.Entry(self.frame_for_entries_3)
# line_num.grid(padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Активний опір лінії').grid()
# active_opir = ttk.Entry(self.frame_for_entries_3)
# active_opir.grid(padx=10, pady=5)
# #
# ttk.Label(self.frame_for_entries_3, text='Номер фідера').grid(column=1, row=7)
# fider_num = ttk.Entry(self.frame_for_entries_3)
# fider_num.grid(column=1, row=8, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Тип лінії').grid(column=1, row=9)
# line_type = ttk.Combobox(self.frame_for_entries_3, values=('КЛ', 'ПЛ', 'ПЛІ'))
# line_type.grid(column=1, row=10, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Реактивний опір лінії').grid(column=1, row=11)
# reactive_opir = ttk.Entry(self.frame_for_entries_3)
# reactive_opir.grid(column=1, row=12, padx=10, pady=5)
# #
# ttk.Label(self.frame_for_entries_3, text='Назва підстанції').grid(column=2, row=7)
# substation_name = ttk.Entry(self.frame_for_entries_3)
# substation_name.grid(column=2, row=8, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Марка лінії').grid(column=2, row=9)
# line_mark = ttk.Entry(self.frame_for_entries_3)
# line_mark.grid(column=2, row=10, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Кількість проводів Х Переріз лінії').grid(column=2, row=11)
# wire_count = ttk.Entry(self.frame_for_entries_3)
# wire_count.grid(column=2, row=12, padx=10, pady=5)
#
# ttk.Label(self.frame_for_entries_3, text='Довжина лінії').grid(column=3, row=7)
# line_length = ttk.Entry(self.frame_for_entries_3)
# line_length.grid(column=3, row=8, padx=10, pady=5)
# ttk.Label(self.frame_for_entries_3, text='Повна потужність\nтрансформатора').grid(column=3, row=9)
# trans_power = ttk.Entry(self.frame_for_entries_3)
# trans_power.grid(column=3, row=10, padx=10, pady=5)
# page_3_scheme_1(self)
#
# back_button(self, self, command=lambda: controller.show_frame(Page2))
# next_button(self, self, command=lambda: controller.show_frame(save_data()))


class Page4(tk.Frame):
    def __init__(self, parent, controller, bg=None, next_page=None, prev_page=None):
        tk.Frame.__init__(self, parent, bg=bg)

        def save_data():
            dictionary['ю1'] = full_name.get('1.0', 'end-1c')
            dictionary['ю0'] = type_obj.get()
            dictionary['ю1_1'] = doc_activity.get('1.0', 'end-1c')
            dictionary['ю2'] = eis_code.get()
            dictionary['ю3'] = object_address.get('1.0', 'end-1c')
            dictionary['ю4'] = consumer_name.get()
            dictionary['ю6'] = doc_flow.get('1.0', 'end-1c')
            if not (abbreviated_name.get()):
                dictionary['ю4_1'] = consumer_name.get()
            else:
                dictionary['ю4_1'] = abbreviated_name.get()
            if legal_address.get('1.0', 'end-1c') == '':
                dictionary['ю5'] = doc_flow.get('1.0', 'end-1c')
            else:
                dictionary['ю5'] = legal_address.get('1.0', 'end-1c')
            dictionary['н_д'] = contract_num.get()
            replace_data()

        title_frame = Frame(self, bg='white')
        title_frame.pack(ipadx=200)
        choose_dep_label = Label(title_frame, text="Інформація об'єкта", font=('', 14), bg='white')
        choose_dep_label.pack(pady=(80, 5))
        # Canvas(title_frame, height=2, width=55, highlightbackground='white', bg='#D9DEED').place(x=40, y=92)
        # Canvas(title_frame, height=2, width=400, highlightbackground='white', bg='#D9DEED').place(x=280, y=92)
        object_info = ttk.Frame(self)
        object_info.pack(pady=(10, 0))

        self.frame_for_entries_4 = Frame(object_info,background='#C7E4FF', highlightthickness=1, highlightbackground="#007AFF")
        self.frame_for_entries_4.pack(ipady=8)

        ttk.Label(self.frame_for_entries_4, text='Номер договору').grid(column=0, row=0, columnspan=2, pady=(10, 0))
        contract_num = ttk.Entry(self.frame_for_entries_4, width=35)
        contract_num.grid(column=0, row=1, pady=5, columnspan=2)

        ttk.Label(self.frame_for_entries_4, text='ЕІС-код').grid(column=0, row=2, padx=(40, 10))
        eis_code = ttk.Entry(self.frame_for_entries_4, width=35)
        eis_code.grid(column=0, row=3, padx=(40, 10), pady=5)

        ttk.Label(self.frame_for_entries_4, text="Вид об'єкта").grid(column=0, row=4, padx=(40, 10))
        type_obj = ttk.Entry(self.frame_for_entries_4, width=35)
        type_obj.grid(column=0, row=5, padx=(40, 10), pady=5)

        ttk.Label(self.frame_for_entries_4, text='Посада, П.І.Б. уповноваженої особи').grid(column=0, row=6,
                                                                                            padx=(40, 10))
        full_name = Text(self.frame_for_entries_4, width=27, height=2, wrap='word', borderwidth=0, highlightthickness=1,
                         highlightbackground='grey')
        full_name.grid(column=0, row=7, padx=(40, 10), pady=5)

        ttk.Label(self.frame_for_entries_4, text="Фактична адреса об'єкту").grid(column=0, row=8, sticky='s',
                                                                                 padx=(40, 10))
        object_address = Text(self.frame_for_entries_4, width=30, height=3, wrap='word', borderwidth=0,
                              highlightthickness=1, highlightbackground='grey')
        object_address.grid(column=0, row=9, padx=(40, 10), pady=5)

        ttk.Label(self.frame_for_entries_4, text='Індекс, Юридична адреса').grid(column=0, row=10, padx=(40, 10))
        legal_address = Text(self.frame_for_entries_4, width=30, height=3, wrap='word', borderwidth=0,
                             highlightthickness=1, highlightbackground='grey')
        legal_address.grid(column=0, row=11, padx=(40, 10), pady=5)

        ttk.Label(self.frame_for_entries_4, text='Документ, за яким\nспоживач здійснює діяльність').grid(column=1,
                                                                                                         row=10,
                                                                                                         pady=(5, 0))
        doc_activity = Text(self.frame_for_entries_4, width=30, height=3, wrap='word', borderwidth=0,
                            highlightthickness=1, highlightbackground='grey')
        doc_activity.grid(column=1, row=11, padx=10, pady=5)

        ttk.Label(self.frame_for_entries_4, text='П.І.Б. споживача').grid(column=1, row=2)
        consumer_name = ttk.Entry(self.frame_for_entries_4, width=35)
        consumer_name.grid(column=1, row=3, padx=10, pady=5)

        ttk.Label(self.frame_for_entries_4, text='Скорочена повна назва споживача').grid(column=1, row=4)
        abbreviated_name = ttk.Entry(self.frame_for_entries_4, width=35)
        abbreviated_name.grid(column=1, row=5, pady=5)

        ttk.Label(self.frame_for_entries_4, text='Повна назва споживача').grid(column=1, row=6)
        full_name = Text(self.frame_for_entries_4, width=27, height=2, wrap='word', borderwidth=0, highlightthickness=1,
                         highlightbackground='grey')
        full_name.grid(column=1, row=7, padx=10, pady=5)

        ttk.Label(self.frame_for_entries_4, text='Індекс, Адреса для документообігу').grid(column=1, row=8)
        doc_flow = Text(self.frame_for_entries_4, width=30, height=3, wrap='word', borderwidth=0, highlightthickness=1,
                        highlightbackground='grey')
        doc_flow.grid(column=1, row=9, padx=10, pady=5)
        tooltip_grid(self.frame_for_entries_4,
                     msg='Залиште поле порожнім, якщо співпадає з\nАдресою для документообігу', column=1, row=9,
                     padx=(290, 10))

        back_button(self, self, command=lambda: controller.show_frame(Page3Scheme1))
        save_button(self, self, command=save_data)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        menubar = Menu(self)
        menubar.add_command(label="Інформація", command=info_window)
        self.config(menu=menubar)
        Frame(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight()).grid(sticky='nsew')

        self.frames = {}
        pages = (Page1, Page2, Page3Scheme1, Page3Scheme2, Page4)
        for F in pages:
            frame = F(self, self, bg='white', next_page=Page4, prev_page=Page2)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # default is Page1
        self.show_frame(Page3Scheme2)

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
s.configure('TLabel', background='#C7E4FF', font=('', 10), justify='center', foreground='black')
app.configure(bg='white')
# app.state('zoomed')
app.geometry('1000x600')
app.mainloop()
