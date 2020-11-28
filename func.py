from random import *
from tkinter import Label
import numpy as np
import matplotlib.pyplot as plt


#Caracteristicas para dibujar la curva
selective_speed = 0.0
voltage =''
magnetic_field = 0.5
in_magnetic_field = 0.00005
distance = 5e-2

# Clase particula
class Particle:
    def __init__(self, name, mass, charge):
        self.name = name
        self.mass = mass
        self.charge = charge

#------------Funciones que se pueden llamar antes del voltaje------------

"""
Funcion para obtener la particula que desea el usuario
Parametros: name - nombre de la particula seleccionada
Return: Un objeto tipo particula 
"""
def elegirParticula(name):
    with open('particulas.txt', 'r') as f:
        particles = [line.strip() for line in f]
    
    for particle in particles: #Por cada particula en el txt
        if particle.find(name): #Si la particula actual contiene el nombre de la seleccionada
            datos = particle.split("@") #Separamos los datos por el @
            nombre = datos[0] #Posicion 0 -> nombre de la particula
            masa = float(datos[1]) #Posicion 1 -> masa de la particula
            charge = float(datos[2]) #Posicion 2 -> carga de la particula
            return Particle(nombre, masa, charge)

"""
Funcion para obtener todas las particulas del txt
Return: Una lista que contiene todas las particulas
"""
def getAllParticles():
    particle_list = []

    with open('particulas.txt', 'r') as f:
        particles = [line.strip() for line in f]
    
    # Creando los objetos por cada linea del txt
    for particle in particles: 
        info = particle.split("@")
        name = info[0]              #[0] = nombre particula
        mass = float(info[1])         #[1] = masa de la particula
        charge = float(info[2])       #[2] = carga de la particula
        temp_particle = Particle(name, mass, charge)
        particle_list.append(temp_particle)
    
    return particle_list

"""
Funcion para obtener la particula que desea el usuario
Parametros: particle - objeto tipo particle la cual sera agregada al txt
"""
def addParticle(particle):
    # Preparando el string
    add_particle = particle.name + "@" + str(particle.mass) + "@" + str(particle.charge) + "\n"

    with open('particulas.txt', 'a') as f:
        f.write(add_particle)
        f.close()


"""
Funcion para que el usuario customice particula
Parametros: name - nombre de la particula creada
            n_neutrones - el numero de neutrones
            n_protones - el numero de protones
            n_electrones - el numero de electrones
Return: Un objeto tipo particula 
"""
def customizarParticula(name, n_neutrones, n_protones, n_electrones):
    # Masas
    neutron_mass = 1.6749e-27
    proton_mass = 1.6726e-27
    electron_mass = 9.1094e-31

    # Cargas
    neutron_charge = 0
    electron_charge = -1.6022e-19
    proton_charge = -1.0 * electron_charge

    # Calculando la carga y masa de la particula
    temp_mass = (n_neutrones*neutron_mass) + (n_protones*proton_mass) + (n_electrones*electron_mass)
    temp_charge = (n_neutrones*neutron_charge) + (n_protones*proton_charge) + (n_electrones*electron_charge)

    # Creando la particula
    particle = Particle(name, temp_mass, temp_charge)
    return particle
    
    
#Funcion para obtener el voltaje del selector
"""
Funcion para obtener el voltaje que tendra el selector
Parametros: volt - voltaje ingresado por el usuario
"""
def obtenerVoltaje(volt):
    global voltage
    voltage = volt

#------------Funciones luego de obtener el voltaje------------

#F uncion para que el usuario calcule la velocidad conocida
def speedSelector():
    global selective_speed, magnetic_field, distance, voltage
    campoE = voltage/distance
    selective_speed = campoE/magnetic_field

#Funcion para calcular la poblacion de particulas
def generarParticulas():
    global selective_speed
    for i in range(100): #Nuestra poblacion es de 100 particulas
        velocidadAleatoria = randint(selective_speed-50,selective_speed+50) #Calculamos velocidad aleatoria
        
        if velocidadAleatoria == selective_speed: #Si coincide con la velocidad del selector
            return True #La dejamos pasar
    return False #Salimos de la funcion

"""
Calcula el radio del semicirculo
Parametros: particle - particula en movimiento
Return: vector radio (positivo eje y & negativo eje -y)
"""
def calculateRadius(particle):
    global selective_speed, magnetic_field

    # Se calcula el radio (incluye negativo)
    if(particle.charge != 0):
        radius = (particle.mass * selective_speed)/(particle.charge * in_magnetic_field)
    else:
        radius = 0
    return radius

"""
Grafica todas las particulas que pasaron
Parametros: particle_list - una lista con todas las particulas que se deseen graficar
"""
def tracePath(particle_list):

    # Empieza a agregar las particulas
    for particle in particle_list:
        radius = calculateRadius(particle)
        if(radius != 0):
            x,y = generateSemicircle(radius)
            plt.plot(x, y, label=str(particle.name))
        else:
            plt.axvline(0, Label = str(particle.name))
    plt.legend(loc = (0, 0.7))
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.grid()
    plt.show()

"""
Obtiene los valores parametricos de x & y
Parametros: radius - el radio en m puede ser positivo o negativo
Return: dos listas con los valores a graficar 
"""
def generateSemicircle(radius):

    # Indicando cuanto del circulo se quiere
    theta = np.linspace(0, np.pi)

    x = radius*np.cos(theta) + radius

    y = abs(radius)*np.sin(theta)

    return x, y