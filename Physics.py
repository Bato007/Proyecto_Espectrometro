#_______________________________________________________
# Universidad del Valle de Guatemala
# Laura Tamath         | Andrea Amaya
# Brandon Hernández    | Oliver de León
# Proyecto final
#_______________________________________________________

#Librerías utilizadas
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from os import path
import tkinter as tk
from PIL import Image, ImageTk
import os
import func as f

#----------------G-U-I------------------------------------------------------------------

# Interface
root = Tk()
root['bg'] = 'gray13'

# GUI's design
root.title('Proyecto Física | Espectrómetro')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='atomo.png'))
root.resizable(False,False)
root.geometry('600x400')
frame = Frame()
frame.pack()

# GUI's tittle
label = Label(root, text = 'SIMULADOR', font = ('Calibri Bold','40'), fg='cyan2', bg='gray13')
label.place(x = 128, y = 5)

# Just stuff
particle_dicc = {' Proton':'protones@1.67E-27@1.67E-19',
                 ' Neutron':'neutrones@1.67E-27@0',
                 ' Electron':'electron@9.109E-31@-1.67E-19',
                 ' Positron':'positron@9.11E-31@1.60E-19',
                 ' Antimuon':'antimuon@1.89E-28@1.60e-19',
                 ' Alpha':'particula alfa@6.64E-27@3.2e-19',
                 ' Deuterium':'nucleo de deuterio@3.96E-30@1.602E-19',
                 ' Ninguna':'nada@0@0'}
variable = ''
variable_2 = ''
variable_3 = ''
window = ''

#-----------------V-O-L-T-A-G-E---S-T-U-F-F-----------------------------------------------

# Reads voltage
def voltageReader():
    try:
        temp_volt = int(vol_entry.get())
        f.obtenerVoltaje(temp_volt)
        messagebox.showinfo(message = 'VALOR ingresado con EXITO', title = 'Valor Ingresado')
    except:
        messagebox.showinfo(message = 'Ingrese un VALOR VALIDO', title = 'Error 404!')
# Voltage command
Button(text = 'INGRESAR', bg='turquoise4', fg='gray97', font = ('Calibri Bold','10'),
       command = voltageReader).place(x = 400, y = 100)
voltage_lbl = Label(root, text = 'Voltaje', font = ('Calibri Bold','12'),
                    fg='white', bg='gray13').place(x = 100, y = 105)
vol_entry = ttk.Entry()
vol_entry.place(x=190, y=105, width=170)

#-----------------P-A-R-T-I-C-L-E---C-H-O-O-S-I-N-G---------------------------------------

# Finish Selection

def generatePlot():
    f.speedSelector()
    f.tracePath(f.getAllParticles())

def finishSel():
    if(f.voltage != ''):
        if((variable.get() != ' Particula 1') & (variable_2.get() != ' Particula 2') & (variable_3.get() != ' Particula 3')):
            # verifies txt existence
            if (os.path.isfile("particulas.txt")):
                os.remove("particulas.txt")
            f= open("particulas.txt","w+")
            f.write(particle_dicc[variable.get()]+'\n')
            f.write(particle_dicc[variable_2.get()]+'\n')
            f.write(particle_dicc[variable_3.get()])
            f.close()
            generatePlot()
            messagebox.showinfo(message = 'VALORES ingresados con EXITO', title = 'Valor Ingresado')
            window.withdraw()
        else:
            messagebox.showinfo(message = 'Ingrese valores ADECUADOS', title = 'Fatal!!')
    else:
        messagebox.showinfo(message = 'Ingrese el VOLTAJE antes de continuar', title = 'Fatal!!')
    
        
# Particle summoner
def particleSummoner():
    global variable, variable_2, variable_3, window
    window = tk.Toplevel()
    window['bg'] = 'gray14'
    window.title('Choose particle') 
    window.geometry('550x300')
    
    # label text for title 
    ttk.Label(window, text = "PARTICULAS",  
              background = 'gray14', foreground ="cyan3",  
              font = ("Calibri Bold", 26)).place(x=175,y=0)

#----------------FIRST PARTICLE---------------------
    # label 
    ttk.Label(window, text = "Primera particula",
              background = 'gray14', foreground ="white",  
              font = ("Times New Roman", 12)).place(x=50,y=70)
      

    # Choice box
    particles = (' Proton',  
                ' Neutron', 
                ' Electron', 
                ' Positron', 
                ' Antimuon', 
                ' Alpha', 
              ' Deuterium')
    variable = StringVar(window)
    variable.set(' Particula 1')
    box_1 = OptionMenu(window,variable,*particles).place(x=60,y=100)
    
#----------------2nd PARTICLE---------------------

    # label 
    ttk.Label(window, text = "Segunda particula",
              background = 'gray14', foreground ="white",  
              font = ("Times New Roman", 12)).place(x=225,y=70)
      

    # Choice box
    particles_2 = (' Ninguna',
                ' Proton',  
                ' Neutron', 
                ' Electron', 
                ' Positron', 
                ' Antimuon', 
                ' Alpha', 
              ' Deuterium')
    variable_2 = StringVar(window)
    variable_2.set(' Particula 2')
    box_2 = OptionMenu(window,variable_2,*particles_2).place(x=240,y=100)
    

#----------------3rd PARTICLE---------------------

    # label 
    ttk.Label(window, text = "Tercera particula",
              background = 'gray14', foreground ="white",  
              font = ("Times New Roman", 12)).place(x=400,y=70)
      
    # Choice box
    particles_3 = (' Ninguna',
                ' Proton',  
                ' Neutron', 
                ' Electron', 
                ' Positron', 
                ' Antimuon', 
                ' Alpha', 
              ' Deuterium')
    variable_3 = StringVar(window)
    variable_3.set(' Particula 3')
    box_3 = OptionMenu(window,variable_3,*particles_3).place(x=400,y=100)

#----------------Final Button---------------------
    
    Button(window,text = 'INGRESAR', bg='turquoise4', fg='gray97', font = ('Calibri Bold','10'),
       command = finishSel).place(x = 240, y = 250)
#----Ends func-----    
    
# Summons particle choosing window
Button(text = 'Escoger Partículas', bg='turquoise4', fg='gray97', font = ('Calibri Bold','10'),
       command = particleSummoner).place(x = 100, y = 160)
        
        

#Imagen de GUI
img = Image.open("particle.jpg")
img = img.resize((185,130), Image.ANTIALIAS)
my_image =  ImageTk.PhotoImage(img)
lbl = Label(image = my_image).place(x=229,y=225)
root.protocol("WM_DELETE_WINDOW", closing)


root.mainloop()
