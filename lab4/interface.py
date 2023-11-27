import tkinter as tk
import Lexer
from pynput import keyboard

def convert():
    output_str.replace('1.0', tk.END, "")
    output_s = Lexer.output(input_str.get('1.0', tk.END))
    
    for i in output_s:
        output_str.insert(tk.END, str(i) + '\n'+ '\n')

def on_press(key):
    convert()

win = tk.Tk()   #создаем окно

win.title('Лексический анализатор')
win.geometry('1280x720+128+72') #1280х720 - размер окна, 1280+720 отступ от левой верхней точки
win.config(bg='#ff8c00')    #цвет фона

lable_input = tk.Label(win, text='Введите ваш код:', 
                                bg='#000000',
                                fg='#ffffff',
                                font=('Consolas')
                                ).grid(row=0, column=0)

lable_output = tk.Label(win, text='Токены:', 
                                bg='#000000',
                                fg='#ffffff',
                                font=('Consolas')
                                ).grid(row=0, column=2)

input_str = tk.Text(win, 
                bg='#000000',
                fg='#ffffff',
                width=70, 
                height=35,)
input_str.grid(row=1, column=0)


output_str = tk.Text(win, 
                bg='#000000',
                fg='#ffffff',
                width=70, 
                height=35,)
output_str.grid(row=1, column=2)



win.grid_columnconfigure(0, minsize=225)
win.grid_columnconfigure(1, minsize=0)
win.grid_columnconfigure(2, minsize=225)

with keyboard.Listener(
        on_press=on_press) as listener:
    win.mainloop()  #запускаем 
    listener.join()