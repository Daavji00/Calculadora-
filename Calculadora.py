### Proyecto Calculadora de Escritorio

# Este proyecto va a consistir en una calculadora básica escrita en python

from re import sub
import tkinter as tk

from pyparsing import col

# Main 

window = tk.Tk() #Crear ventana principal 

'''
  Agregar botones a la interfaz del uno al diez
'''
zero_button = tk.Button(window, text='0', width=5, height=2)
zero_button.grid(row=3, column=1)
one_button = tk.Button(window, text='1', width=5, height=2) 
one_button.grid(row=2, column=0)
two_button = tk.Button(window, text='2', width=5, height=2)
two_button.grid(row=2, column=1)
three_button = tk.Button(window, text='3', width=5, height=2)
three_button.grid(row=2, column=2)
four_button = tk.Button(window, text='4', width=5, height=2)
four_button.grid(row=1,column=0)
five_button = tk.Button(window, text='5', width=5, height=2)
five_button.grid(row=1,column=1)
six_button = tk.Button(window, text='6', width=5, height=2)
six_button.grid(row=1,column=2)
seven_button = tk.Button(window, text='7', width=5, height=2)
seven_button.grid(row=0,column=0)
eight_button = tk.Button(window, text='8', width=5, height=2)
eight_button.grid(row=0,column=1)
nine_button = tk.Button(window, text='9', width=5, height=2)
nine_button.grid(row=0,column=2)

'''
  Agregrar botones de operaciones aritméticas
'''

prod_button = tk.Button(window, text='x', width=5, height=2)
prod_button.grid(row=1, column=3)
div_button = tk.Button(window, text='/', width=5, height=2)
div_button.grid(row=1, column=4)
sum_button = tk.Button(window, text='+', width=5, height=2)
sum_button.grid(row=2, column=3)
sub_button = tk.Button(window, text='-', width=5, height=2)
sub_button.grid(row=2, column=4)

window.mainloop() # Correr ventana principal
