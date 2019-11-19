# coding: utf-8

#Importaciones de librerias
import numpy
import time
from neopixel import *
import argparse
import pymysql

# LED strip configuration:
LED_COUNT      = 256      # Numeros de leds de la matriz.
LED_PIN        = 18      # GPIO pin conectado a los leds (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connectado a los leds (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # frecuencia de señal led LED (usualmente 800khz)
LED_DMA        = 10      # canal DMA (siempre 10)
LED_BRIGHTNESS = 25     # brillo de los leds desde 0 el apagado a 255 muy intenso 
LED_INVERT     = False   # True para invertir señal
LED_CHANNEL    = 0       # Cambiar a '1' para GPIOs 13, 19, 41, 45 or 53

 
#Permite configurar los leds
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()


#globales

global matriz8x32 #guarda los numeros de los leds en una matriz
matriz8x32 = [[],[],[],[],[],[],[],[]]

global gListaNotificaciones #guarda las notificaciones en un minuto
gListaNotificaciones= []

global db #Coneccion a base de datos
db = pymysql.connect(host="exosdata.net", user="exosdatanet_proyectoArqui", passwd="daniel2700", db="exosdatanet_proyectoArqui")

global nula32 #global para vaciar la matriz
nula32 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

global mostrartexto #aqui se guarda el texto a guardar para ir corriendolo hacia la izquierda, se transpone para obtener primero las columnas
mostrartexto = numpy.transpose([[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
								[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
								[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]).tolist ()
global nula8 #permite agregar un espacio entre letras
nula8 = [[2],
		 [0],
		 [0],
		 [0],
		 [0],
		 [0],
		 [0],
		 [2]]
    
 
global nula16 #permite agregar un espacio entre palabras
nula16 = [[2,2],
		 [0,0],
		 [0,0],
		 [0,0],
		 [0,0],
		 [0,0],
		 [0,0],
		 [2,2]]


#INICIO DE LETRAS Y NUMEROS cada matriz representa un caracter alfanumerico		  
global letraA
letraA = [[2,2,2,2,2,2],
		  [0,0,1,1,0,0],
		  [0,1,0,0,1,0],
		  [1,0,0,0,0,1],
		  [1,1,1,1,1,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [2,2,2,2,2,2]]
		  
		  
global letraB
letraB = [[2,2,2,2,2,2],
		  [1,1,1,1,1,0],
		  [1,0,0,0,0,1],
		  [1,1,1,1,1,0],
		  [1,1,1,1,1,0],
		  [1,0,0,0,0,1],
		  [1,1,1,1,1,0],
		  [2,2,2,2,2,2]]


global letraC
letraC = [[2,2,2,2,2,2],
		  [0,1,1,1,1,1],
		  [1,0,0,0,0,0],
		  [1,0,0,0,0,0],
		  [1,0,0,0,0,0],
		  [1,0,0,0,0,0],
		  [0,1,1,1,1,1],
		  [2,2,2,2,2,2]]

global letraD
letraD = [[2,2,2,2,2,2],
		  [1,1,1,1,1,0],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,1,1,1,1,0],
		  [2,2,2,2,2,2]]

global letraE
letraE = [[2,2,2,2,2,2],
		  [1,1,1,1,1,1],
		  [1,0,0,0,0,0],
		  [1,1,1,1,0,0],
		  [1,1,1,1,0,0],
		  [1,0,0,0,0,0],
		  [1,1,1,1,1,1],
		  [2,2,2,2,2,2]]

global letraF
letraF = [[2,2,2,2,2,2],
		  [1,1,1,1,1,1],
		  [1,0,0,0,0,0],
		  [1,0,0,0,0,0],
		  [1,1,1,1,0,0],
		  [1,0,0,0,0,0],
		  [1,0,0,0,0,0],
		  [2,2,2,2,2,2]]

global letraG
letraG = [[2,2,2,2,2,2],
		  [0,1,1,1,1,1],
		  [1,0,0,0,0,0],
		  [1,0,0,0,0,0],
		  [1,0,0,1,1,1],
		  [1,0,0,0,0,1],
		  [0,1,1,1,1,1],
		  [2,2,2,2,2,2]]

global letraH
letraH = [[2,2,2,2,2,2],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,1,1,1,1,1],
		  [1,1,1,1,1,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [2,2,2,2,2,2]]

global letraI
letraI = [[2,2,2,2,2,2],
		  [1,1,1,1,1,1],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [1,1,1,1,1,1],
		  [2,2,2,2,2,2]]

global letraJ
letraJ = [[2,2,2,2,2,2],
		  [1,1,1,1,1,1],
		  [0,0,0,1,0,0],
		  [0,0,0,1,0,0],
		  [0,0,0,1,0,0],
		  [1,0,0,1,0,0],
		  [1,1,1,1,0,0],
		  [2,2,2,2,2,2]]

global letraK
letraK = [[2,2,2,2,2,2],
		  [1,1,0,0,0,1],
		  [1,1,0,0,1,0],
		  [1,1,1,1,0,0],
		  [1,1,1,1,0,0],
		  [1,1,0,0,1,0],
		  [1,1,0,0,0,1],
		  [2,2,2,2,2,2]]

global letraL
letraL = [[2,2,2,2,2,2],
		  [1,1,0,0,0,0],
		  [1,1,0,0,0,0],
		  [1,1,0,0,0,0],
		  [1,1,0,0,0,0],
		  [1,1,0,0,0,0],
		  [1,1,1,1,1,1],
		  [2,2,2,2,2,2]]

global letraM
letraM = [[2,2,2,2,2,2],
		  [1,0,0,0,0,1],
		  [1,1,0,0,1,1],
		  [1,0,1,1,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [2,2,2,2,2,2]]

global letraN
letraN = [[2,2,2,2,2,2],
		  [1,0,0,0,0,1],
		  [1,1,0,0,0,1],
		  [1,0,1,0,0,1],
		  [1,0,0,1,0,1],
		  [1,0,0,0,1,1],
		  [1,0,0,0,0,1],
		  [2,2,2,2,2,2]]

global letraNN
letraNN = [[2,2,2,2,2,2],
		  [0,1,1,1,1,0],
		  [0,0,0,0,0,0],
		  [1,1,0,0,0,1],
		  [1,0,1,0,0,1],
		  [1,0,0,1,0,1],
		  [1,0,0,0,1,1],
		  [2,2,2,2,2,2]]

global letraO
letraO = [[2,2,2,2,2,2],
		  [0,1,1,1,1,0],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [0,1,1,1,1,0],
		  [2,2,2,2,2,2]]
		  
global letraP
letraP = [[2,2,2,2,2,2],
		  [1,1,1,1,1,0],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,1,1,1,1,0],
		  [1,0,0,0,0,0],
		  [1,0,0,0,0,0],
		  [2,2,2,2,2,2]]
		  
global letraQ
letraQ = [[2,2,2,2,2,2],
		  [0,1,1,1,1,0],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,1,0,1],
		  [1,0,0,0,1,0],
		  [0,1,1,1,0,1],
		  [2,2,2,2,2,2]]

global letraR
letraR = [[2,2,2,2,2,2],
		  [1,1,1,1,1,0],
		  [1,0,0,0,0,1],
		  [1,1,1,1,1,0],
		  [1,0,1,0,0,0],
		  [1,0,0,1,0,0],
		  [1,0,0,0,1,0],
		  [2,2,2,2,2,2]]

global letraS
letraS = [[2,2,2,2,2,2],
		  [0,1,1,1,1,1],
		  [1,0,0,0,0,0],
		  [0,1,1,1,1,0],
		  [0,0,0,0,0,1],
		  [0,0,0,0,0,1],
		  [1,1,1,1,1,0],
		  [2,2,2,2,2,2]]

global letraT
letraT = [[2,2,2,2,2,2],
		  [1,1,1,1,1,1],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [2,2,2,2,2,2]]

global letraU
letraU = [[2,2,2,2,2,2],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [0,1,1,1,1,0],
		  [2,2,2,2,2,2]]

global letraV
letraV = [[2,2,2,2,2,2],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [0,1,0,0,1,0],
		  [0,0,1,1,0,0],
		  [2,2,2,2,2,2]]

global letraW
letraW = [[2,2,2,2,2,2],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,0,0,0,1],
		  [1,0,1,1,0,1],
		  [1,1,0,0,1,1],
		  [1,0,0,0,0,1],
		  [2,2,2,2,2,2]]

global letraX
letraX = [[2,2,2,2,2,2],
		  [1,0,0,0,0,1],
		  [0,1,0,0,1,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [0,1,0,0,1,0],
		  [1,0,0,0,0,1],
		  [2,2,2,2,2,2]]

global letraY
letraY = [[2,2,2,2,2,2],
		  [1,0,0,0,0,1],
		  [0,1,0,0,1,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [0,0,1,1,0,0],
		  [2,2,2,2,2,2]]

global letraZ
letraZ = [[2,2,2,2,2,2],
		  [1,1,1,1,1,1],
		  [0,0,0,0,1,0],
		  [0,0,0,1,0,0],
		  [0,0,1,0,0,0],
		  [0,1,0,0,0,0],
		  [1,1,1,1,1,1],
		  [2,2,2,2,2,2]]
		  

global numero0
numero0 = [[2,2,2,2,2,2],
		   [0,1,1,1,1,0],
		   [1,1,0,0,0,1],
		   [1,0,1,0,0,1],
		   [1,0,0,1,0,1],
		   [1,0,0,0,1,1],
		   [0,1,1,1,1,0],
		   [2,2,2,2,2,2]]

global numero1
numero1 = [[2,2,2,2,2,2],
		   [0,0,1,1,0,0],
		   [0,1,1,1,0,0],
		   [0,0,1,1,0,0],
		   [0,0,1,1,0,0],
		   [0,0,1,1,0,0],
		   [1,1,1,1,1,1],
		   [2,2,2,2,2,2]]

global numero2
numero2 = [[2,2,2,2,2,2],
		   [0,1,1,1,1,0],
		   [1,0,0,0,0,1],
		   [0,0,0,0,1,0],
		   [0,0,0,1,0,0],
		   [0,0,1,0,0,0],
		   [1,1,1,1,1,1],
		   [2,2,2,2,2,2]]

global numero3
numero3 = [[2,2,2,2,2,2],
		   [0,1,1,1,1,0],
		   [1,0,0,0,0,1],
		   [0,0,0,1,1,0],
		   [0,0,0,1,1,0],
		   [1,0,0,0,0,1],
		   [0,1,1,1,1,0],
		   [2,2,2,2,2,2]]

global numero4
numero4 = [[2,2,2,2,2,2],
		   [1,0,0,0,1,1],
		   [1,0,0,0,1,1],
		   [1,1,1,1,1,1],
		   [0,0,0,0,1,1],
		   [0,0,0,0,1,1],
		   [0,0,0,0,1,1],
		   [2,2,2,2,2,2]]

global numero5
numero5 = [[2,2,2,2,2,2],
		   [1,1,1,1,1,1],
		   [1,0,0,0,0,0],
		   [1,1,1,1,1,1],
		   [0,0,0,0,0,1],
		   [0,0,0,0,0,1],
		   [1,1,1,1,1,1],
		   [2,2,2,2,2,2]]

global numero6
numero6 = [[2,2,2,2,2,2],
		   [0,1,1,1,1,1],
		   [1,0,0,0,0,0],
		   [1,0,0,0,0,0],
		   [1,1,1,1,1,0],
		   [1,0,0,0,0,1],
		   [0,1,1,1,1,0],
		   [2,2,2,2,2,2]]

global numero7
numero7 = [[2,2,2,2,2,2],
		   [1,1,1,1,1,1],
		   [0,0,0,0,0,1],
		   [0,0,0,0,1,0],
		   [0,0,0,1,0,0],
		   [0,0,0,1,0,0],
		   [0,0,0,1,0,0],
		   [2,2,2,2,2,2]]

global numero8
numero8 = [[2,2,2,2,2,2],
		   [0,1,1,1,1,0],
		   [1,0,0,0,0,1],
		   [0,1,1,1,1,0],
		   [0,1,1,1,1,0],
		   [1,0,0,0,0,1],
		   [0,1,1,1,1,0],
		   [2,2,2,2,2,2]]

global numero9
numero9 = [[2,2,2,2,2,2],
		   [0,1,1,1,1,0],
		   [1,0,0,0,0,1],
		   [0,1,1,1,1,0],
		   [0,0,0,1,0,0],
		   [0,0,1,0,0,0],
		   [0,1,0,0,0,0],
		   [2,2,2,2,2,2]]







		  
		  
#Este codigo permite cargar la matriz donde se obtiene el numero de cada led para ser representado y utilizado como posiciones de una matriz		  
def iniciar_matriz():
	global matriz8x32 #esta matriz se utilizara para guardar cada 
	cont = 0
	bandera1 = 0

	while cont < 256:
		if bandera1 == 0:
			cont1 = 0
			while cont1 < 8:
				matriz8x32[cont1].append(cont)
				cont+=1
				cont1+=1
			bandera1=1
		else:
			cont1 = 7
			while cont1>=0:
				matriz8x32[cont1].append(cont)
				cont+=1
				cont1-=1
			bandera1 = 0
##########################################################################

#Entradas: no posee entradas de parametros
#Salidas: Retorna una lista de notificaciones
#Restricciones: El raspberry debe estar conectado a internet para obtener la lista
def notificaciones(): #Esta funcion se utiliza para obtener las notificaciones de la base de datos
	global db
	notificacionesL = []
	cur = db.cursor()
	cur.execute("SELECT fecha,mensaje,id FROM recordatorio")
	for row in cur.fetchall() :
		identi=str(row[2])
		mensaje = str(row[1])
		fecha = str(row[0])
		notificacionesL = notificacionesL + [[mensaje,fecha,identi]]
	return notificacionesL


#Entradas: Recibe una matriz con lista de palabras en codigo 
#Salidas: No posee salidas per envia la palabras a ser interpretadas
#Restricciones: Debe ingresar una matriz valida
def mostrarMensaje(matrizMensaje):
	global mostrartexto
	for letra in matrizMensaje:
		for codigo in letra:
			mostrartexto = mostrartexto[1:]
			mostrartexto += [codigo]
			mostrarMatriz(mostrartexto)

#Entradas: Una matriz de 8x32  
#Salidas: No posee salidas pero modifica los leds para ser encendidos segun la matriz de entrada
#Restricciones: No posee restricciones
def mostrarMatriz (matriz): 
	global matriz8x32
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] == 1:
				strip.setPixelColor(matriz8x32[j][i], 125)
			elif matriz[i][j]==0:
				strip.setPixelColor(matriz8x32[j][i], Color(0,0,0))
			elif matriz[i][j]==2:
				strip.setPixelColor(matriz8x32[j][i], Color(0,255,0)) #GRB
	strip.show()
	time.sleep(0.04	)

#Entradas: Recibe un texto para ser codificado en matrices de letras
#Salidas: No posee salidas pero envia la matriz codificada segun el texto a ser impresa
#Restricciones: Debe ser caracteres validos
def desplegarTexto(string):
	string=string.replace("ñ","+")
	string=string.replace("Ñ","+")
	matrizVacia=[]
	cont = 0
	letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","+","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","0","1","2","3","4","5","6","7","8","9"]
	matrices = [letraA,letraB,letraC,letraD,letraE,letraF,letraG,letraH,letraI,letraJ,letraK,letraL,letraM,letraN,letraNN,letraO,letraP,letraQ,letraR,letraS,letraT,letraU,letraV,letraW,letraX,letraY,letraZ,nula16,numero0,numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8,numero9]
	contRep = 0

	while contRep < 7:
		matrizVacia = []
		cont = 0
		while cont < len(string):
			matrizVacia = matrizVacia+[numpy.transpose(matrices[letras.index(string[cont].upper())]).tolist()]
			matrizVacia = matrizVacia+[numpy.transpose(nula8).tolist()]
		
			cont+=1
		matrizVacia = matrizVacia + [numpy.transpose(nula32).tolist ()]
		mostrarMensaje(matrizVacia)
		contRep += 1
	
#Entradas: Recibe la fecha actual y la lista de notificaciones
#salidas: Retorna la lista de notificaciones filtrada por la fecha actual
#Restricciones: No posee
def filtrarPorFecha(fecha,noti):
	lista = []
	for listaNoti in noti:
		if listaNoti != []:
			if listaNoti[1].split("T")[0] == fecha:
				lista+= [listaNoti]
	return lista

#Entradas: La hora actual y la lista de notificaciones
#Salidas: Retorna la lista de notificaciones filtrada por la hora actual
#Restricciones: No posee
def filtrarPorHora(hora,noti):
	lista = []
	for listaNoti in noti:
		if listaNoti != []:
			if listaNoti[1].split("T")[1] == hora:
				lista+= [listaNoti]
	return lista

#Entradas: Recibe la lista de notificaciones ya filtradas por fecha y hora
#Salidas: No posee pero envia a imprimir las notificaciones
#Restricciones: no posee
def mostrarListaNotificaciones(lista):
		for mensaje in lista:
			if mensaje != [] :
				desplegarTexto(mensaje[0])

#Entradas: La lista de notificaciones ya desplegadas
#Salidas: No posee pero envia a eliminar las notificaciones ya desplegadas al servidor
#Restricciones: El raspberry debe estar conectado a internet
def eliminarNotificaciones(lista):
	db = pymysql.connect(host="exosdata.net", user="exosdatanet_proyectoArqui", passwd="daniel2700", db="exosdatanet_proyectoArqui")
	cur = db.cursor()
	for mensaje in lista:
		if mensaje != []:
			cur.execute("DELETE FROM recordatorio WHERE id="+"'"+mensaje[2]+"'")

#Entradas: No posee
#Salidas: no posee pero ejecuta el proceso
#Restricciones: no posee
def main():
	iniciar_matriz()
	cont = 0
	while True:
		horaActual= time.strftime("%H:%M")
		fechaActual = time.strftime("%Y-%m-%d")
		lista = filtrarPorFecha(fechaActual,notificaciones())
		lista = filtrarPorHora(horaActual,lista)
		mostrarListaNotificaciones(lista)
		eliminarNotificaciones(lista)
		time.sleep(0.5)
		cont += 1
		
		
main()





