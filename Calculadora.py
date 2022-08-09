### Proyecto Calculadora de Escritorio

# Este proyecto va a consistir en una calculadora básica escrita en python

import tkinter as tk

# Funcion reconocer expresion

def expresion(exp) :
    
    output.insert(1.0, str(exp))



# Main 

window = tk.Tk() #Crear ventana principal 

'''
  Salida
'''

frame_output = tk.Frame(window)
frame_output.grid(row=0, column=0)
output = tk.Text(frame_output, width=25, height=2)
output.pack()
output.insert(tk.END, "0")



'''
  Agregar botones a la interfaz del uno al diez
'''

frame_botones = tk.Frame(window)
frame_botones.grid(row=1, column=0)

zero_button = tk.Button(frame_botones, text='0', width=5, height=2, command= lambda: expresion(0))
zero_button.grid(row=3, column=1)
one_button = tk.Button(frame_botones, text='1', width=5, height=2, command= lambda: expresion(1)) 
one_button.grid(row=2, column=0)
two_button = tk.Button(frame_botones, text='2', width=5, height=2, command= lambda: expresion(2))
two_button.grid(row=2, column=1)
three_button = tk.Button(frame_botones, text='3', width=5, height=2, command= lambda: expresion(3))
three_button.grid(row=2, column=2)
four_button = tk.Button(frame_botones, text='4', width=5, height=2, command= lambda: expresion(4))
four_button.grid(row=1,column=0)
five_button = tk.Button(frame_botones, text='5', width=5, height=2, command= lambda: expresion(5))
five_button.grid(row=1,column=1)
six_button = tk.Button(frame_botones, text='6', width=5, height=2, command= lambda: expresion(6))
six_button.grid(row=1,column=2)
seven_button = tk.Button(frame_botones, text='7', width=5, height=2, command= lambda: expresion(7))
seven_button.grid(row=0,column=0)
eight_button = tk.Button(frame_botones, text='8', width=5, height=2, command= lambda: expresion(8))
eight_button.grid(row=0,column=1)
nine_button = tk.Button(frame_botones, text='9', width=5, height=2, command= lambda: expresion(9))
nine_button.grid(row=0,column=2)

'''
  Agregar botones de operaciones aritméticas
'''

prod_button = tk.Button(frame_botones, text='x', width=5, height=2)
prod_button.grid(row=1, column=3)
div_button = tk.Button(frame_botones, text='/', width=5, height=2)
div_button.grid(row=1, column=4)
sum_button = tk.Button(frame_botones, text='+', width=5, height=2)
sum_button.grid(row=2, column=3)
sub_button = tk.Button(frame_botones, text='-', width=5, height=2)
sub_button.grid(row=2, column=4)

'''
  Agregar boton de all clear
'''

ac_button = tk.Button(frame_botones, text='AC', width=11, height=2)
ac_button.grid(row=0, column=3, columnspan=2)

'''
  Agregar boton de igual
'''

eq_button = tk.Button(frame_botones, text='=', width=5, height=2)
eq_button.grid(row=0, column=2)



window.mainloop() # Correr ventana principal

