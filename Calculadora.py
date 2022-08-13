### Proyecto Calculadora de Escritorio

# Este proyecto va a consistir en una calculadora básica escrita en python

import tkinter as tk

# Funcion para mostrar digito(s) en pantalla
def showExp(exp) : 
  if error: # Error, no hace nada
    pass 

  elif posText == 0 and (exp.isdigit() or exp == '.') : # Cambiamos valor 0 por otro valor
    updatePosText('IN') # Actualizamos pos. siguiente numero
    updateSExp(exp) # Actualizamos la expresion en pantalla
    output.delete(1.0)
    output.insert(1.0, exp) # Mostramos nuevo numero

  elif posText > 0 and posText < 30 : # Mostramos los numeros en orden (max. 30 digitos)
    updateSExp(exp)
    output.insert('1.' + str(posText), exp) # Mostramos nuevo número
    updatePosText('IN') # Actualizamos posicion siguiente digito 

# Función para borrar digito(s) de pantalla
def deleteExp(action) :
  if action == 'AC' : # Borramos todo y mostramos 0
    output.delete(1.0,'end')
    output.insert(1.0, '0') # Añadimos 0 a la pantalla
    updateSExp(action) # Actualizamos numero actual
    updatePosText(action) # Actualizamos posicion siguiente digito 
    if error: # Cambiar valor de error y resetear todo
      changeValErr()
  elif error: # Error, no hace nada
    pass
  elif action == 'BC': #Borramos una posicion de la pantalla
    updatePosText(action) # Actualizamos posicion siguiente digito
    updateSExp(action) # Actualizamos expresion
    if posText == 0 : # Se borra último dígito
      output.delete(1.0)
      output.insert(1.0, '0') # Añadimos 0 a la pantalla
    else : # No se borra último dígito
      output.delete(1.0,'end')
      output.insert(1.0, sExp) # Mostramos número actual

# Función para añadir punto a número de más de 3 cifras 
# No usada por ahora
def addPoint(sNum):
  lnum = list(reversed(sNum)) # Lista invertida con el número original
  pnum = '' # Variable para contener el número con puntos
  for l in range(0,len(sNum)): # Recorremos lista 
    if (l) % 3 == 0 and l != 0 : # Posición múltiplo de 3
      pnum = lnum[l] + '.' + pnum # Se añade digito con coma
    else: # Posición normal
      pnum = lnum[l] + pnum # Se añade digito
  return pnum 

# Función para actualizar donde se muestra el siguient dígito
def updatePosText(action): 
  global posText
  if action == 'IN' and posText < 30: # Posición siguiente
    posText += 1
  elif action == 'AC' and posText > 0 : # Posición inicial
    posText = 0
  elif action == 'BC' and posText > 0 : # Posición actual
    posText -= 1
  elif action == 'RES' and posText > 0:
    posText = len(sExp)

# Funcion para actualizar número en pantalla
# No usada por ahora
def updateSNum(action): 
  global sNum # Trabajamos con variable global sNum
  
  if action == 'AC': # Borrar todos los digitos de la pantalla
    sNum = ''
  elif action == 'BC': # Borrar último digito introducido
    sNum = sNum[:len(sNum)-1]
  elif action.isdigit() : # Añadir un dígito a la pantalla
    sNum += action

# Funcion que actualiza expresion para evaluar
def updateSExp(action):
  global sExp 

  if action == 'AC': # Borrar todos los digitos de la pantalla
    sExp = ''
  elif action == 'BC': # Borrar último digito introducido
    sExp = sExp[:len(sExp)-1]
  elif action == 'RES': # Calcular resultado expresion
    sExp = str(eval(sExp))
  else : # Añadir un dígito a la pantalla
    sExp += action

# Funcion para evaluar expresion y mostrar resultado en pantalla
def evalExp():
  if error: # Hay error, no hace nada
    pass 
  else : # Intentar calcular resultado expresion
    try: 
      updateSExp('RES') # Actualizamos expresion
      updatePosText('RES') # Actualizamos posText
      output.delete(1.0, 'end')
      output.insert(1.0, sExp) 
    except: # Error al evaluar expresion
      output.delete(1.0, 'end')
      output.insert(1.0, "Syntax Error")
      changeValErr() # Cambiar estado error a True

# Funcion para cambiar estado error 
def changeValErr(): 
  global error 
  error = not error

# Main 

posText = 0 # Posicion columna donde se muestra el número
# sNum = '' # Número que se tiene que motrar por pantalla
# gNum = ['None'] * 2 # Matriz para guardar dos números
sExp = '' # Expresion mostrada en pantalla
error = False # Controla si se produce error de sintaxis (bloque todo si es True)

window = tk.Tk() # Crear ventana principal 

'''
    Mostrar salida 
'''

frame_output = tk.Frame(window) # Frame para mostrar números introducidos y resultados
frame_output.grid(row=0, column=0) # Definimos posicion de celda del frame
output = tk.Text(frame_output, width=25, height=2) # Crear label text
output.pack()
output.insert(1.0, "0") # Insertar valor inicial 0 en la salida

'''
  Agregar botones a la interfaz del uno al diez
'''

frame_botones = tk.Frame(window) # Frame que contiene los botones a pulsar
frame_botones.grid(row=1, column=0) # Posicion del frame

zero_button = tk.Button(frame_botones, text='0', width=5, height=2, command= lambda: showExp('0'))
zero_button.grid(row=3, column=1)
one_button = tk.Button(frame_botones, text='1', width=5, height=2, command= lambda: showExp('1')) 
one_button.grid(row=2, column=0)
two_button = tk.Button(frame_botones, text='2', width=5, height=2, command= lambda: showExp('2'))
two_button.grid(row=2, column=1)
three_button = tk.Button(frame_botones, text='3', width=5, height=2, command= lambda: showExp('3'))
three_button.grid(row=2, column=2)
four_button = tk.Button(frame_botones, text='4', width=5, height=2, command= lambda: showExp('4'))
four_button.grid(row=1,column=0)
five_button = tk.Button(frame_botones, text='5', width=5, height=2, command= lambda: showExp('5'))
five_button.grid(row=1,column=1)
six_button = tk.Button(frame_botones, text='6', width=5, height=2, command= lambda: showExp('6'))
six_button.grid(row=1,column=2)
seven_button = tk.Button(frame_botones, text='7', width=5, height=2, command= lambda: showExp('7'))
seven_button.grid(row=0,column=0)
eight_button = tk.Button(frame_botones, text='8', width=5, height=2, command= lambda: showExp('8'))
eight_button.grid(row=0,column=1)
nine_button = tk.Button(frame_botones, text='9', width=5, height=2, command= lambda: showExp('9'))
nine_button.grid(row=0,column=2)

'''
  Agregar botones de operaciones aritméticas
'''
prod_button = tk.Button(frame_botones, text='x', width=5, height=2, command= lambda: showExp('*'))
prod_button.grid(row=1, column=3)
div_button = tk.Button(frame_botones, text='/', width=5, height=2, command= lambda: showExp('/'))
div_button.grid(row=1, column=4)
sum_button = tk.Button(frame_botones, text='+', width=5, height=2, command= lambda: showExp('+'))
sum_button.grid(row=2, column=3)
sub_button = tk.Button(frame_botones, text='-', width=5, height=2, command= lambda: showExp('-'))
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
eq_button = tk.Button(frame_botones, text='=', width=11, height=2, command=evalExp)
eq_button.grid(row=3, column=3, columnspan=2)

'''
  Boton punto
'''
pt_button = tk.Button(frame_botones, text='.', width=5, height=2, command=lambda: showExp('.'))
pt_button.grid(row=3, column=2)

window.mainloop() # Correr ventana principal

