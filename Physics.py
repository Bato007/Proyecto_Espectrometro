#_______________________________________________________
# Universidad del Valle de Guatemala
# CC3056 - Programacion de Microprocesadores
# Martín Amado         | Andrea Amaya
# Brandon Hernández    | Oliver de León  | Laura Tamath
# Proyecto no. 2
# Desencriptador de archivos
#_______________________________________________________

#Librerías utilizadas
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from os import path
from PIL import Image, ImageTk
import os
#import gmpy

# LLAVE COMPLETA
#\\]]^^__``aaHHIIJJKKZZ
#00112233445566778899..

# Interface
root = Tk()
root['bg'] = 'green'
#Diseño del GUI
root.title('SIMULADOR')

#root.call('wm', 'iconphoto', root._w, PhotoImage(file='icon/skull.png'))
root.resizable(False,False)
root.geometry('600x300')
frame = Frame()
frame.pack()
#Título del GUI
label = Label(root, text = 'SIMULADOR', font = ('Calibri Bold','40'), fg='white', bg='green')
label.place(x = 156, y = 5)

#Atributos
route = ''
keyRoute = ''
line = ''
key = 0
    
#Función para abrir archivos .txt
def open_file():
    global route
    file = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    route = file

#Función para buscar la llave
def key():
    global keyRoute
    global key
    #Lectura del documento txt
    keyRoute = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    file = open(keyRoute,'r')
    key = file.readlines()
    file.close

    if(key != []):
        #comprueba si la clave ingresada es correcta o no, y emite un mensaje
        if(key[0] == '18'):
            key = int(key[0])
            messagebox.showinfo(message = 'Llave Ingresada', title = 'Completo')
        else:
            messagebox.showinfo(message = 'Llave Erronea', title = 'Fatal')
            key = 0
    #Si el archivo no ha sido seleccionado, muestra una advertencia
    else:
        messagebox.showinfo(message = 'Archivo vacio', title = 'Contenido faltante')
  
#Función para leer el archivo a desencriptar
def read():
    if (route != ''):
        if (key == 18):
            global line
            file = open(route,'r')
            line = file.readlines()
            file.close
            #Desencripta el archivo, si todos los requerimientos están listos
            if(line != []):
                write(line)
            #Muestra advertencias depenendiendo del requerimiento que falte
            else:
                messagebox.showinfo(message = 'Archivo vacio', title = 'Contenido faltante')
        else:
            messagebox.showinfo(message = 'Ingrese llave', title = 'Llave faltante')
    else:
        messagebox.showinfo(message = 'Se debe de seleccionar un archivo', title = 'Ruta faltante')

#Función para enrutar el mensaje 
def write(line):
    final = []
    x = line[0].split(',')
    x.pop(len(x)-1)
    for i in range(len(x)):
        decrypted = ''
        for j in range(len(x[i])):
            decrypted += decrypt(x[i][j])
        final.append(decrypted)
    messagebox.showinfo(message = 'Indicar Ruta de Guardado', title = 'Requerimiento')
    route = filedialog.asksaveasfilename(filetypes=[("Text files","*.txt")])
    file = open(route,'w')
    for i in range(len(final)):
        file.write(str(final[i])+os.linesep)
    file.close()
    messagebox.showinfo(message = 'Desencriptado Finalizado', title = 'Completo')


#Función para transcribir el mensaje desencriptado
def decrypt(element):
    decrypted = 0
    element = ord(element)
    a = element-97
    #Utilizar aritmética modular inversa para desencriptar
    #invmod = int(gmpy.divm(a,1,26))
    if ((element < 98) & (element > 75)):
        #decrypted = invmod - 26*2 + (97 - key)
        decrypted = a + 26 - 26*2 + (97 - key)
    else:
        #decrypted = invmod - 26 + (97 - key)
        decrypted = a + 26 - 26 + (97 - key)
    decrypted = chr(decrypted)
    #retornar el mensaje desencriptado
    return decrypted

#Función para asegurar que el programa se cerrará
def closing():
    if messagebox.askokcancel("Close program","¿Seguro que quiere salir del programa?"):
        root.destroy()
    
#Diseño y funcionamiento de los botones
label_1 = Label(root, text = 'Voltaje', font = ('Calibri Bold','12'), fg='white', bg='green')
label_1.place(x = 275, y = 80)

        
entry_1 = ttk.Entry()
entry_1.place(x=275, y=105, width=150)

#Multiple choice box-----------------------------------
window = Tk() 
window.title('PARTICULAS') 
window.geometry('500x250') 
  
# label text for title 
ttk.Label(window, text = "PARTICULAS",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
# label 
ttk.Label(window, text = "Selecciona una partícula :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
n = StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' Proton',  
                          ' Neutron', 
                          ' Electron', 
                          ' Positron', 
                          ' Tau', 
                          ' Delta', 
                          ' Alpha', 
                          ' Deuterium') 
  
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current() 
#------------------------------------------------
#Button(text = 'Abrir archivo', bg='black', fg='white', command = open_file).place(x = 275,y = 105)
#Button(text = 'Desencriptar', bg='black', fg='white', command = read).place(x = 275,y = 195)
Button(text = 'INGRESAR', bg='black', fg='white', command = key).place(x = 275, y = 195)

#Imagen de GUI
img = Image.open("icon/ima.jpg")
img = img.resize((175,250), Image.ANTIALIAS)
my_image =  ImageTk.PhotoImage(img)

lbl = Label(image = my_image).place(x=229,y=250)

root.protocol("WM_DELETE_WINDOW", closing)


root.mainloop()