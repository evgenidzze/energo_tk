from tkinter import *

root = Tk()


def update_options_B(*args):
    countries = data[variable_a.get()]
    variable_b.set(countries[0])
    menu = optionmenu_b['menu']
    menu.delete(0, 'end')
    for country in countries:
        menu.add_command(label=country, command=lambda nation=country: variable_b.set(nation))


data = {'Asia': ['Japan', 'China', 'Malasia'], 'Europe': ['Germany', 'France', 'Switzerland'],
        'Africa': ['Nigeria', 'Kenya', 'Ethiopia']}
data2 = {'Japan': ["jiustu", "kamikaz", "Tokyo"], 'China': ["Shaigon", "Hong Kong"],
         'Malasia': ["tiramusto", "quala lopour"], 'Germany': ["Dusseldorf", "Berlin", "Hambourg"],
         'France': ["Paris", "Lille"], 'Switzerland': ["Biern", "Bonn"], 'Nigeria': ['Nigeria1', 'Nigeria3'],
         'Kenya': ["Keny West", "Notorious"], 'Ethiopia': ["Etanpi", "Neeandertaal"]}
variable_a = StringVar()
variable_b = StringVar()

variable_a.trace('w', update_options_B)
optionmenu_a = OptionMenu(root, variable_a, *data.keys())
optionmenu_b = OptionMenu(root, variable_b, '')

variable_a.set('Asia')
optionmenu_a.pack()
optionmenu_b.pack()

root.mainloop()
