import tkinter as tk
from tkinter import *
from tkinter import ttk

from change_docx import dictionary
from styles.button_next import back_button, next_button


class Page3Scheme1(tk.Frame):
    def __init__(self, parent, controller, bg=None, next_page=None, prev_page=None):
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
            controller.show_frame(next_page)

        tk.Frame.__init__(self, parent, bg=bg)

        title_frame = Frame(self, bg='white')
        title_frame.pack(padx=(250, 0))
        choose_dep_label = Label(title_frame, text="Технічна інформація об'єкта", font=('', 14), bg='white')
        choose_dep_label.pack(pady=(80, 5), padx=(102, 600))
        Canvas(title_frame, height=2, width=55, highlightbackground='white', bg='#D9DEED').place(x=40, y=92)
        Canvas(title_frame, height=2, width=300, highlightbackground='white', bg='#D9DEED').place(x=360, y=92)
        self.frame_for_entries_3 = Frame(self, background='#C7E4FF', highlightthickness=1,
                                         highlightbackground="#007AFF")
        self.frame_for_entries_3.pack(ipady=8)

        ttk.Label(self.frame_for_entries_3, text='Номер ТП').grid(sticky='s')
        tp_num = ttk.Entry(self.frame_for_entries_3)
        tp_num.grid(padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Потужність').grid()
        power = ttk.Entry(self.frame_for_entries_3)
        power.grid(padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Щитова').grid()
        zko_vrs = ttk.Combobox(self.frame_for_entries_3, values=('ЗКО', 'ВРЩ'))
        zko_vrs.grid(padx=10, pady=5)
        #
        ttk.Label(self.frame_for_entries_3, text='Ступінь напруги ТРЕЕ').grid(column=1, row=0, sticky='s')
        tree = ttk.Combobox(self.frame_for_entries_3, values=('0,22', '0,38'))
        tree.grid(column=1, row=1, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Тип лічильника').grid(column=1, row=2)
        type_l = ttk.Entry(self.frame_for_entries_3)
        type_l.grid(column=1, row=3, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Початкові показники').grid(column=1, row=4)
        indicators = ttk.Entry(self.frame_for_entries_3)
        indicators.grid(column=1, row=5, padx=10, pady=5)
        #
        ttk.Label(self.frame_for_entries_3, text='Струм').grid(column=2, row=0, sticky='s')
        stream = ttk.Entry(self.frame_for_entries_3)
        stream.grid(column=2, row=1, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Серійний номер лічильника').grid(column=2, row=2)
        serial_num = ttk.Entry(self.frame_for_entries_3)
        serial_num.grid(column=2, row=3, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Номінал лічильника').grid(column=2, row=4)
        par = ttk.Entry(self.frame_for_entries_3)
        par.grid(column=2, row=5, padx=10, pady=5)
        #
        ttk.Label(self.frame_for_entries_3, text='Категорія надійності\nструмоприймачів').grid(column=3, row=0,
                                                                                               pady=(5, 0))
        category = ttk.Combobox(self.frame_for_entries_3, values=('I', 'II', 'III'))
        category.grid(column=3, row=1, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Квартал та рік повірки').grid(column=3, row=2)
        cvartal = ttk.Entry(self.frame_for_entries_3)
        cvartal.grid(column=3, row=3, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Режим роботи').grid(column=3, row=4)
        rezhym = ttk.Entry(self.frame_for_entries_3)
        rezhym.grid(column=3, row=5, padx=10, pady=5)
        #
        Canvas(self.frame_for_entries_3, height=1, width=600, highlightbackground='white').grid(columnspan=4, pady=10)
        #
        ttk.Label(self.frame_for_entries_3, text='Номер опори').grid()
        num_opory = ttk.Entry(self.frame_for_entries_3)
        num_opory.grid(padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Номер лінії').grid()
        line_num = ttk.Entry(self.frame_for_entries_3)
        line_num.grid(padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Активний опір лінії').grid()
        active_opir = ttk.Entry(self.frame_for_entries_3)
        active_opir.grid(padx=10, pady=5)
        #
        ttk.Label(self.frame_for_entries_3, text='Номер фідера').grid(column=1, row=7)
        fider_num = ttk.Entry(self.frame_for_entries_3)
        fider_num.grid(column=1, row=8, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Тип лінії').grid(column=1, row=9)
        line_type = ttk.Combobox(self.frame_for_entries_3, values=('КЛ', 'ПЛ', 'ПЛІ'))
        line_type.grid(column=1, row=10, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Реактивний опір лінії').grid(column=1, row=11)
        reactive_opir = ttk.Entry(self.frame_for_entries_3)
        reactive_opir.grid(column=1, row=12, padx=10, pady=5)
        #
        ttk.Label(self.frame_for_entries_3, text='Назва підстанції').grid(column=2, row=7)
        substation_name = ttk.Entry(self.frame_for_entries_3)
        substation_name.grid(column=2, row=8, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Марка лінії').grid(column=2, row=9)
        line_mark = ttk.Entry(self.frame_for_entries_3)
        line_mark.grid(column=2, row=10, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Кількість проводів Х Переріз лінії').grid(column=2, row=11)
        wire_count = ttk.Entry(self.frame_for_entries_3)
        wire_count.grid(column=2, row=12, padx=10, pady=5)

        ttk.Label(self.frame_for_entries_3, text='Довжина лінії').grid(column=3, row=7)
        line_length = ttk.Entry(self.frame_for_entries_3)
        line_length.grid(column=3, row=8, padx=10, pady=5)
        ttk.Label(self.frame_for_entries_3, text='Повна потужність\nтрансформатора').grid(column=3, row=9)
        trans_power = ttk.Entry(self.frame_for_entries_3)
        trans_power.grid(column=3, row=10, padx=10, pady=5)

        back_button(self, self, command=lambda: controller.show_frame(prev_page))
        next_button(self, self, command=lambda: controller.show_frame(save_data()))


class Page3Scheme2(tk.Frame):
    def __init__(self, parent, controller, bg=None, next_page=None, prev_page=None):
        def save_data():
            dictionary['т1'] = tp_num.get()
            dictionary['т4'] = power.get()
            dictionary['с3'] = zko_vrs.get()
            dictionary['т2'] = tree.get()
            if dictionary['т2'] == '0,22':
                dictionary['т2_1'] = '1'
            elif dictionary['т2'] == '0,38':
                dictionary['т2_1'] = '3'
            dictionary['т6'] = type_l.get()
            dictionary['т9'] = indicators.get()
            dictionary['т7'] = serial_num.get()
            dictionary['т7_2'] = par.get()
            dictionary['т5'] = category.get()
            dictionary['т7_1'] = cvartal.get()
            dictionary['т8'] = rezhym.get()
            dictionary['т11'] = line_num.get()
            dictionary['р1'] = active_opir.get()
            dictionary['с1'] = fider_num.get()
            dictionary['л1'] = line_type.get()
            dictionary['р2'] = reactive_opir.get()
            dictionary['с2'] = substation_name.get()
            if line_type.get() == 'КЛ':
                dictionary['т99'] = "в місці кріплення кабелю живлення"
            elif line_type.get() in ('ПЛ', 'ПЛІ'):
                dictionary['т99'] = "в місці кріплення проводів ЛЕП"

            controller.show_frame(next_page)

        tk.Frame.__init__(self, parent, bg=bg)

        title_frame = Frame(self, bg='white')
        title_frame.pack(padx=(250, 0))
        choose_dep_label = Label(title_frame, text="Технічна інформація об'єкта", font=('', 14), bg='white')
        choose_dep_label.pack(pady=(80, 5), padx=(102, 600))
        Canvas(title_frame, height=1, width=55, highlightbackground='white', bg='#007AFF').place(x=40, y=92)
        Canvas(title_frame, height=1, width=300, highlightbackground='white', bg='#007AFF').place(x=360, y=92)
        self.frame_for_entries_3 = Frame(self, background='#C7E4FF', highlightthickness=1,
                                         highlightbackground="#007AFF")
        self.frame_for_entries_3.pack(ipady=8)

        ttk.Label(self.frame_for_entries_3, text='Оператор системи', font=('', 14)).grid(columnspan=4, pady=(10, 0))
        Canvas(self.frame_for_entries_3, height=1, width=250, highlightbackground='#C7E4FF', bg='#007AFF').place(x=0,
                                                                                                                 y=40)

        padx_label = 40
        entry_size_s = 6

        ttk.Label(self.frame_for_entries_3, text='Номер ТП').grid(row=1, column=0, pady=(20, 15), sticky='w',
                                                                  padx=(padx_label, 0))
        tp_num = ttk.Entry(self.frame_for_entries_3, width=entry_size_s)
        tp_num.grid(row=1, column=1, pady=(20, 15), ipady=1, padx=20)
        ttk.Label(self.frame_for_entries_3, text='Номер лінії').grid(row=2, sticky='w', pady=(0, 15),
                                                                     padx=(padx_label, 0))
        line_num = ttk.Entry(self.frame_for_entries_3, width=entry_size_s)
        line_num.grid(row=2, column=1, pady=(0, 15), ipady=1, padx=20)
        ttk.Label(self.frame_for_entries_3, text='Номер фідера').grid(row=3, sticky='w', pady=(0, 15),
                                                                      padx=(padx_label, 0))
        fider_num = ttk.Entry(self.frame_for_entries_3, width=entry_size_s)
        fider_num.grid(row=3, column=1, pady=(0, 15), ipady=1, padx=20)
        ttk.Label(self.frame_for_entries_3, text='Тип фідера').grid(row=4, sticky='w', pady=(0, 15),
                                                                    padx=(padx_label, 0))
        fider_type = ttk.Entry(self.frame_for_entries_3, width=entry_size_s)
        fider_type.grid(row=4, column=1, pady=(0, 15), ipady=1, padx=20)
        ttk.Label(self.frame_for_entries_3, text='Повна потужність Т1').grid(row=5, sticky='w', pady=(0, 15),
                                                                             padx=(padx_label, 0))
        full_power_t1 = ttk.Entry(self.frame_for_entries_3, width=entry_size_s)
        full_power_t1.grid(row=5, column=1, pady=(0, 15), ipady=1, padx=20)
        ttk.Label(self.frame_for_entries_3, text='Повна потужність Т2').grid(row=6, sticky='w', pady=(0, 15),
                                                                             padx=(padx_label, 0))
        full_power_t2 = ttk.Entry(self.frame_for_entries_3, width=entry_size_s)
        full_power_t2.grid(row=6, column=1, pady=(0, 15), ipady=1, padx=20)

        # column 2
        ttk.Label(self.frame_for_entries_3, text='Назва підстанції').grid(column=2, row=1, pady=(20, 15), sticky='w',
                                                                          padx=(padx_label, 0))
        substation_name = ttk.Entry(self.frame_for_entries_3, width=35)
        substation_name.grid(column=3, row=1, pady=(20, 15), ipady=1, padx=(0, 90))

        ttk.Label(self.frame_for_entries_3, text='Кількість Х Переріз лінії на балансі ОС').grid(column=2, row=2,
                                                                                                 pady=(0, 15),
                                                                                                 sticky='w',
                                                                                                 padx=(padx_label, 0))
        wire_count = ttk.Entry(self.frame_for_entries_3)
        wire_count.grid(column=3, row=2, pady=(0, 15), ipady=1, padx=20)

        # ttk.Label(self.frame_for_entries_3, text='Потужність').grid()
        # power = ttk.Entry(self.frame_for_entries_3)
        # power.grid(padx=10, pady=5)
        # ttk.Label(self.frame_for_entries_3, text='Щитова').grid()
        # zko_vrs = ttk.Combobox(self.frame_for_entries_3, values=('ЗКО', 'ВРЩ'))
        # zko_vrs.grid(padx=10, pady=5)
        # #
        # ttk.Label(self.frame_for_entries_3, text='Ступінь напруги ТРЕЕ').grid(column=1, row=1, sticky='s')
        # tree = ttk.Combobox(self.frame_for_entries_3, values=('0,22', '0,38'))
        # tree.grid(column=1, row=2, padx=10, pady=5)
        # ttk.Label(self.frame_for_entries_3, text='Тип лічильника').grid(column=1, row=3)
        # type_l = ttk.Entry(self.frame_for_entries_3)
        # type_l.grid(column=1, row=4, padx=10, pady=5)
        # ttk.Label(self.frame_for_entries_3, text='Початкові показники').grid(column=1, row=5)
        # indicators = ttk.Entry(self.frame_for_entries_3)
        # indicators.grid(column=1, row=6, padx=10, pady=5)
        # #

        # ttk.Label(self.frame_for_entries_3, text='Серійний номер лічильника').grid(column=2, row=2+1)
        # serial_num = ttk.Entry(self.frame_for_entries_3)
        # serial_num.grid(column=2, row=3+1, padx=10, pady=5)
        # ttk.Label(self.frame_for_entries_3, text='Номінал лічильника').grid(column=2, row=4+1)
        # par = ttk.Entry(self.frame_for_entries_3)
        # par.grid(column=2, row=5+1, padx=10, pady=5)
        # #
        # ttk.Label(self.frame_for_entries_3, text='Категорія надійності\nструмоприймачів').grid(column=3, row=0+1,
        #                                                                                        pady=(5, 0))
        # category = ttk.Combobox(self.frame_for_entries_3, values=('I', 'II', 'III'))
        # category.grid(column=3, row=1+1, padx=10, pady=5)
        # ttk.Label(self.frame_for_entries_3, text='Квартал та рік повірки').grid(column=3, row=2+1)
        # cvartal = ttk.Entry(self.frame_for_entries_3)
        # cvartal.grid(column=3, row=3+1, padx=10, pady=5)
        # ttk.Label(self.frame_for_entries_3, text='Режим роботи').grid(column=3, row=4+1)
        # rezhym = ttk.Entry(self.frame_for_entries_3)
        # rezhym.grid(column=3, row=5+1, padx=10, pady=5)
        # #
        # Canvas(self.frame_for_entries_3, height=1, width=600, highlightbackground='white').grid(columnspan=4, pady=10)
        # #

        # ttk.Label(self.frame_for_entries_3, text='Активний опір лінії').grid()
        # active_opir = ttk.Entry(self.frame_for_entries_3)
        # active_opir.grid(padx=10, pady=5)
        # #

        # ttk.Label(self.frame_for_entries_3, text='Тип лінії').grid(column=1, row=10)
        # line_type = ttk.Combobox(self.frame_for_entries_3, values=('КЛ', 'ПЛ', 'ПЛІ'))
        # line_type.grid(column=1, row=11, padx=10, pady=5)
        # ttk.Label(self.frame_for_entries_3, text='Реактивний опір лінії').grid(column=1, row=12)
        # reactive_opir = ttk.Entry(self.frame_for_entries_3)
        # reactive_opir.grid(column=1, row=13, padx=10, pady=5)

        back_button(self, self, command=lambda: controller.show_frame(prev_page))
        next_button(self, self, command=lambda: controller.show_frame(save_data()))
