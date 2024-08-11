import tkinter as tk
from random import randint, choice
from tkinter import messagebox


# def AddIdea():
#     text = EnterText.get()
#     if text != '':
#         with open('How.txt', 'w', encoding='utf-8') as f:  # открываем для записи
#             f.write(text + '\n')  # записали
#         EnterText.delete(0, 'end')
#     else:
#         tk.messagebox.showinfo('Ошибка', 'Поле ввода пустое.')



# def RandomIdea():
#     with open('How.txt', 'r', encoding='utf-8') as f:  # открываем для чтения
#         ideas = f.readlines()  # считали все строки
#         idea = choice(ideas)  # выбираем случайную строку
#         messagebox.showinfo('Идея', idea)

def AddIdea():
    res = float(EnterText.get()) / 100 * float(EnterText_1.get()) * float(EnterText_2.get()) - float(EnterText_3.get())
    return tk.messagebox.showinfo('Равно', f'Сумма счёта: {float(EnterText.get()) / 100 * float(EnterText_1.get()) * float(EnterText_2.get())} '
            f'Сумма комиссии: {str(res)}')

def EnterClick(e):
    AddIdea()


window = tk.Tk()

window.resizable(width=False, height=False)

window.title("Расчет стоимости страхования для клиента")

window.geometry('720x360')

window['bg'] = 'black'

idea = tk.Label(window, text='Калькулятор страхования', font=('arial', 15), fg='white', bg='black')  # текст Привет
idea.place(x=220, y=25)  # где на экране расположен

idea = tk.Label(window, text='Страховая сумма', font=('arial', 12), fg='white', bg='black')  # текст страховая сумма
idea.place(x=45, y=60)
EnterText = tk.Entry(fg='black', width=45)  # Ввод текста
EnterText.place(x=220, y=65)  # Где на экране расположен


idea = tk.Label(window, text='Введите процент', font=('arial', 12), fg='white', bg='black')  # текст Введите процент
idea.place(x=45, y=90)
EnterText_1 = tk.Entry(fg='black', width=45)
EnterText_1.place(x=220, y=95)  # Где на экране расположен


idea = tk.Label(window, text='Введите курс', font=('arial', 12), fg='white', bg='black')  # текст Введите курс
idea.place(x=45, y=120)
EnterText_2 = tk.Entry(fg='black', width=45)
EnterText_2.place(x=220, y=125)  # Где на экране расположен


idea = tk.Label(window, text='Введите страховую пр.', font=('arial', 12), fg='white', bg='black')  # текст Введите страховую премию
idea.place(x=45, y=150)
EnterText_3 = tk.Entry(fg='black', width=45)
EnterText_3.place(x=220, y=155)  # Где на экране расположен

btn = tk.Button(window, text='Равно', command=AddIdea, width='38', height='2', fg='black',
                bg='white')  # Добавил кнопку
btn.place(x=220, y=185)  # Где на экране расположен

window.bind('<Return>', EnterClick)



window.mainloop()

