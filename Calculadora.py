### Proyecto Calculadora de Escritorio

# Este proyecto va a consistir en una calculadora básica escrita en python

import tkinter as tk

# Funcion reconocer showExp

def showExp(exp) :  
  if posText == 0 : # Cambiamos valor 0 por otro valor
    output.delete(1.0)
    output.insert(1.0, str(exp))
    updatePosText('IN')
  elif posText < 30 : # Mostramos los numeros en orden al que se marcan
    output.insert('1.' + str(posText), str(exp))
    updatePosText('IN')

def deleteExp(action) :
  if action == 'AC' : # Borramos y mostramos 0
    output.delete(1.0,'end')
    output.insert(1.0, '0')
    updatePosText(action)  
  elif action == 'BC': #Borramos una posicion de la pantalla
    updatePosText(action)
    if posText == 0 :
      output.delete(1.0)
      output.insert(1.0, '0')
    else :
      output.delete('1.' + str(posText))
    

def updatePosText(accion):
  global posText
  if accion == 'IN' and posText < 30:
    posText += 1
  elif accion == 'AC' and posText > 0 :
    posText = 0
  elif accion == 'BC' and posText > 0 :
    posText -= 1

# Main 

window = tk.Tk() # Crear ventana principal 

'''
    Mostrar salida 
'''

frame_output = tk.Frame(window) # Crear frame de salida
frame_output.grid(row=0, column=0) 
output = tk.Text(frame_output, width=25, height=2) # Crear label text
posText = 0 # Posicion columna donde se muestra el número
output.pack()
output.insert(1.0, "0") # Insertar valor inicial 0 en la salida

'''
  Agregar botones a la interfaz del uno al diez
'''

frame_botones = tk.Frame(window)
frame_botones.grid(row=1, column=0)

zero_button = tk.Button(frame_botones, text='0', width=5, height=2, command= lambda: showExp(0))
zero_button.grid(row=3, column=1)
one_button = tk.Button(frame_botones, text='1', width=5, height=2, command= lambda: showExp(1)) 
one_button.grid(row=2, column=0)
two_button = tk.Button(frame_botones, text='2', width=5, height=2, command= lambda: showExp(2))
two_button.grid(row=2, column=1)
three_button = tk.Button(frame_botones, text='3', width=5, height=2, command= lambda: showExp(3))
three_button.grid(row=2, column=2)
four_button = tk.Button(frame_botones, text='4', width=5, height=2, command= lambda: showExp(4))
four_button.grid(row=1,column=0)
five_button = tk.Button(frame_botones, text='5', width=5, height=2, command= lambda: showExp(5))
five_button.grid(row=1,column=1)
six_button = tk.Button(frame_botones, text='6', width=5, height=2, command= lambda: showExp(6))
six_button.grid(row=1,column=2)
seven_button = tk.Button(frame_botones, text='7', width=5, height=2, command= lambda: showExp(7))
seven_button.grid(row=0,column=0)
eight_button = tk.Button(frame_botones, text='8', width=5, height=2, command= lambda: showExp(8))
eight_button.grid(row=0,column=1)
nine_button = tk.Button(frame_botones, text='9', width=5, height=2, command= lambda: showExp(9))
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

ac_button = tk.Button(frame_botones, text='AC', width=5, height=2, command= lambda: deleteExp('AC'))
ac_button.grid(row=0, column=4)

'''
  Boton borrar un parámetro
'''

bc_button = tk.Button(frame_botones, text='BC', width=5, height=2, command=lambda: deleteExp('BC'))
bc_button.grid(row=0, column=3)

'''
  Agregar boton de igual
'''

eq_button = tk.Button(frame_botones, text='=', width=11, height=2)
eq_button.grid(row=3, column=3, columnspan=2)



window.mainloop() # Correr ventana principal

