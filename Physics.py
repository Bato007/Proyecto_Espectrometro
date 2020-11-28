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
name = ''
proton = ''
electron = ''
neutron = ''

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

# Finished Selection
def finishSel():
    if(f.voltage != ''):
        if((variable.get() != ' Particula 1') & (variable_2.get() != ' Particula 2') & (variable_3.get() != ' Particula 3')):
            # verifies txt existence
            if (os.path.isfile("particulas.txt")):
                os.remove("particulas.txt")
            file= open("particulas.txt","w+")
            temp = [variable.get(),variable_2.get(),variable_3.get()] 
            for j in temp:
                file.write(particle_dicc[str(j)]+'\n')
            file.close()
            messagebox.showinfo(message = 'VALORES ingresados con EXITO', title = 'Valor Ingresado')
            window.withdraw()
            generatePlot()
        else:
            messagebox.showinfo(message = 'Ingrese valores ADECUADOS', title = 'Fatal!!')
    else:
        messagebox.showinfo(message = 'Ingrese el VOLTAJE antes de continuar', title = 'Fatal!!')
    
# Finished Selection 2
def finishSel_2():
    if(f.voltage != ''):
        if((nNeutron.get() != ' Neutrones') & (nElectron.get() != ' Electrones') & (nProton.get() != ' Protones')):
            # verifies txt existence
            if (os.path.isfile("particulas.txt")):
                os.remove("particulas.txt")
            file= open("particulas.txt","w+")
            a = f.customizarParticula('Customized', float(nNeutron.get()), float(nProton.get()), float(nElectron.get()))
            f.addParticle(a)
            messagebox.showinfo(message = 'VALORES ingresados con EXITO', title = 'Valor Ingresado')
            window_2.withdraw()
            generatePlot()
        else:
            messagebox.showinfo(message = 'Ingrese valores ADECUADOS', title = 'Fatal!!')
    else:
        messagebox.showinfo(message = 'Ingrese el VOLTAJE antes de continuar', title = 'Fatal!!')
# Customize window
    
def customize():
    if(f.voltage != ''):
        global nNeutron, nProton, nElectron, window_2
        window_2 = tk.Toplevel()
        window_2['bg'] = 'gray14'
        window_2.title('Particula costumizada ') 
        window_2.geometry('550x370')
        # labels ---------------------------------------------------------
        ttk.Label(window_2, text = "COSTUMIZADO",  
                      background = 'gray14', foreground ="cyan3",  
                      font = ("Calibri Bold", 26)).place(x=175,y=0)
        ttk.Label(window_2, text = "Nombre de particula",
                      background = 'gray14', foreground ="white",  
                      font = ("Times New Roman", 12)).place(x=120,y=50)
        ttk.Label(window_2, text = "No. Neutrones",
                      background = 'gray14', foreground ="white",  
                      font = ("Times New Roman", 12)).place(x=120,y=100)
        ttk.Label(window_2, text = "No. Protones",
                      background = 'gray14', foreground ="white",  
                      font = ("Times New Roman", 12)).place(x=120,y=150)
        ttk.Label(window_2, text = "No. Electrones",
                      background = 'gray14', foreground ="white",  
                      font = ("Times New Roman", 12)).place(x=120,y=200)
        # Entries----------------------------------------------------------
       # Choice box
        entry_1 = ttk.Entry(window_2)
        entry_1.place(x=120, y=75, width=300)
       
        neutrons = (' 1',  
                    ' 2', 
                    ' 3', 
                    ' 4', 
                    ' 5', 
                    ' 6', 
                    ' 7',
                    ' 8',
                    ' 9',
                    ' 10')
        nNeutron = StringVar(window_2)
        nNeutron.set(' Neutrones')
        neu_box = OptionMenu(window_2,nNeutron,*neutrons).place(x=120,y=120)
        
        protons = (' 1',  
                ' 2', 
                ' 3', 
                ' 4', 
                ' 5', 
                ' 6', 
                ' 7',
                ' 8',
                ' 9',
                ' 10')
        nProton = StringVar(window_2)
        nProton.set(' Protones')
        pro_box = OptionMenu(window_2,nProton,*protons).place(x=120,y=170)
        
        electrons = (' 1',  
                    ' 2', 
                    ' 3', 
                    ' 4', 
                    ' 5', 
                    ' 6', 
                    ' 7',
                    ' 8',
                    ' 9',
                    ' 10')
        nElectron = StringVar(window_2)
        nElectron.set(' Electrones')
        ele_box = OptionMenu(window_2,nElectron,*electrons).place(x=120,y=220)
    
         # Button----------------------------------------------------------
        Button(window_2,text = 'INGRESAR', bg='turquoise4', fg='gray97', font = ('Calibri Bold','10'),
           command = finishSel_2).place(x = 250, y = 300)
    else:
        messagebox.showinfo(message = 'Ingrese VOLTAJE', title = 'Fatal!!')

#---------ends func-------------------------------------------------------

# Particle summoner
def particleSummoner():
    if(f.voltage != ''):
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
    else:
        messagebox.showinfo(message = 'Ingrese VOLTAJE', title = 'Fatal!!')
    
# Summons particle choosing window
Button(text = 'Escoger Partículas', bg='turquoise4', fg='gray97', font = ('Calibri Bold','10'),
       command = particleSummoner).place(x = 100, y = 160)
        
Button(text = 'Costumizar', bg='turquoise4', fg='gray97', font = ('Calibri Bold','10'),
       command = customize).place(x = 300, y = 160)        

#Imagen de GUI
img = Image.open("particle.jpg")
img = img.resize((185,130), Image.ANTIALIAS)
my_image =  ImageTk.PhotoImage(img)
lbl = Label(image = my_image).place(x=229,y=225)
root.protocol("WM_DELETE_WINDOW")


root.mainloop()
