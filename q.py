import tkinter as tk

window_main = tk.Tk(className='Tkinter - TutorialKart')
window_main.geometry("400x200")

frame_1 = tk.Frame(window_main, bg='green', width=500, height=500)
frame_1.grid()
frame_1.grid_propagate(0)

frame_2 = tk.Frame(frame_1, bg='black', width=100, height=100)
frame_2.grid()
frame_2.grid_propagate(0)



window_main.mainloop()