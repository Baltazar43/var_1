from tkinter import *
from tkinter import messagebox
from turtle import color
 
def calculate_bmi():
   kg = int(weight_tf.get())
   m = int(height_tf.get())/100
   bmi = kg/(m*m)
   bmi = round(bmi, 1)
 
   if bmi < 18.5:
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
   elif (bmi > 18.5) and (bmi < 24.9):
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
   elif (bmi > 24.9) and (bmi < 29.9):
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
   else:
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')  
 
window = Tk()
window.title('Калькулятор индекса массы тела')
window.geometry('400x300')
window.resizable(True, False)
window.configure(bg="#1E466A")

 
frame = Frame(
    window,
    padx=20,
    pady=20,
    bg="#1E466A"
)
frame.pack(expand=True)
 
 
height_lb = Label(
   frame,
   text="Введите свой рост (в см) ",
   font='Georgia 12',
   bg="#1E466A",
   fg="#ffffff"
)
height_lb.grid(row=3, column=1)
 
weight_lb = Label(
    frame,
    text="Введите свой вес (в кг)  ",
    font='Georgia 12',
    bg="#1E466A",
    fg="white"
)
weight_lb.grid(row=4, column=1)
 
height_tf = Entry(
   frame,
   bg="#FEE0A5",
)
height_tf.grid(row=3, column=2, pady=5)
 
weight_tf = Entry(
    frame,
    bg="#FEE0A5",
)
weight_tf.grid(row=4, column=2, pady=5)
 
cal_btn = Button(
   frame,
   text='Рассчитать',
   command=calculate_bmi,
   font='GeorgiaBOLD 12',
   bg="#FEE0A5"
)
cal_btn.grid(row=5, column=2)
 
window.mainloop()