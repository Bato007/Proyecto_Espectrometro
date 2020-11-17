from random import *

#Caracteristicas particula
carga = 0
masa = 0
nombre = ""

#Caracteristicas para dibujar la curva
velocidadConocida = 0
voltaje = 0
campoM = 100
distancia = 10

#Funcion para que el usuario elija particula
def elegirParticula(nombre):
    with open('particulas.txt', 'r') as f:
        particulas = [line.strip() for line in f]
    
    for particula in particulas: #Por cada particula en el txt
        if particula.find(nombre): #Si la particula actual contiene el nombre de la seleccionada
            datos = particula.split("@") #Separamos los datos por el @
            nombre = particula[0] #Posicion 0 -> nombre de la particula
            masa = particula[1] #Posicion 1 -> masa de la particula
            carga = particula[2] #Posicion 2 -> carga de la particula
            
#Funcion para que el usuario customice particula
def customizarParticula():
    global carga, masa
    protones = pro
    neutrones = neu
    elec = electrones    
    #En esta parte no tengo ni idea de como calcular la carga y la masa
    
    
#Funcion para obtener el voltaje del selector
def obtenerVoltaje(volt):
    global voltaje
    voltaje = volt
    
#Funcion para que el usuario calcule la velocidad conocida
def calcularSelectorVelocidad():
    global velocidadConocida, campoM, distancia
    campoE = voltaje/distancia
    velocidadConocida = campoE/campoM
    
#Funcion para calcular la poblacion de particulas
def generarParticulas():
    global velocidadConocida
    for i in range(100): #Nuestra poblacion es de 100 particulas
        velocidadAleatoria = randint(velocidadConocida-50,velocidadConocida+50) #Calculamos velocidad aleatoria
        
        if velocidadAleatoria == velocidadConocida: #Si coincide con la velocidad del selector
            return True #La dejamos pasar
    return False #Salimos de la funcion

#Funcion para calcular la orbita del campo magnetico
def graficarCurva():
    global masa, carga, velocidadConocida, campoM
    radio = (masa*velocidadConocida)/(carga*campoM) #Calculamos el radio de la orbita
    #Se grafica el radio con matplot