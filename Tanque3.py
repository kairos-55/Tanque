#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, math, os, time, datetime
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from pygame.locals import *
#from pygame_functions import *
from decimal import *
import string
string.ascii_uppercase
from datetime import datetime
import checkButtons #Clase que maneja botones de selección
import random

pygame.init()
# Inicializar valores
black=(0,0,0)
white=(255,255,255)
blue=(0,0,200)
green=(0,200,0)
dimension_ventana = (1024,720)

dimension_boton_seleccion = (18,18)

coordenada_equilibro_masa = 398
coordenada_tanque = (160,101)
coordenada_logo = (0,-5)
coordenada_banersup = (68, 0)
coordenada_titulo = (640,15)
coordenada_banerinf = (0,645)
coordenada_bomba = (50, 580)
coordenada_reservorio = (135, 480)
coordenada_multimetro = (800, 150)
coordenada_sensor = (300, 353)
coordenada_plc = (110, 145)
coordenada_bornera1 = (100, 530)
coordenada_cablerojo = (102, 568)
coordenada_cableazul = (125, 568)
coordenada_cableverde = (146, 568)
coordenada_cablenegro = (169, 568)
coordenada_fuente24 = (650, 145)
coordenada_texcablerojo = (105, 610)
coordenada_texcableverde = (149, 605)
coordenada_canaleta_1 = (78, 400)
coordenada_canaleta_2 = (-4, 10)
coordenada_canaleta_3 = (78, 40)
coordenada_canaleta_4 = (935, 10)
coordenada_estructura_1 = (40, 445)
coordenada_estructura_2 = (10, 70)
coordenada_estructura_3 = (405, 70)
coordenada_estructura_4 = (40, 60)
coordenada_estructura_5 = (40, 635)
coordenada_cerrarsesion = (100, 10)
coordenada_bomba_tuberia = (540, 140)
coordenada_reservorio_animacion = (650, 460)
coordenada_tanque_animacion = (705, 190)
coordenada_aguares_animacion = (468, 640)
coordenada_aguares1_animacion = (561, 628)
coordenada_aguares2_animacion = (368, 660)
coordenada_planta_inicio = (10, 110)
coordenada_logoUV_inicio = (0, 0)
coordenada_zona_autenticacion = (522, 590)
coordenada_zona_descripcion = (522, 102)
coordenada_zona_planta = (-5, 102)
coordenada_zona_superior = (24, 0)
coordenada_cajon_cerrado = (70, 180)
coordenada_p_id = (450, 200)

coordenada_bplay = (1000, 150)

#Coordenadas de los botones de selección en la pantalla de fallos
coordenada_fallo1 = (450,125)
coordenada_fallo2 = (450,175)
coordenada_fallo3 = (450,225)
coordenada_fallo4 = (450,275)
coordenada_fallo5 = (450,325)
coordenada_fallo6 = (450,375)
coordenada_fallo7 = (450,425)
coordenada_fallo8 = (450,475)

origen = (30, 30)
color_fondo = (225,225,225)
fps = 60
posicion_incial = 198
global k
k = 0.0000401
h0 = 0
h1 = np.array([0,0,0])
qi0 = 1.0      
h = 0.1
at = 0.002376
hinic = 0
hf = 0.1
n = 1001
delta = (hf-hinic)/(n-1)
a = 0.00237583
kv = 0.00401
h1 = 0.5
k1 = 0
k2 = 0
var = 0
variable_cambio = 0
variable_cambio2 = 0
variable_cambio_sec = 0
variable_cambio_sec2 = 0
variable_cambio_sec3 = 0
variable_cambio_sec4 = 0
variable_cambio_sec5 = 0
variable_cerrarsesion = 0
v_pid = 0
v_transm = 0
v_motor = 0
global pantalla_errores, loop_ppal, loop_sec, autenticacion, loop_ppal_medicion, loop_sec_medicion, cerrarsesion, animacion_tanque, usuario, loop_control_cerrado
loop_ppal = False
loop_sec = False
autenticacion = True
loop_ppal_medicion = False
loop_sec_medicion = False
animacion_tanque = False
loop_control_cerrado = False
pantalla_errores = False
usuario = ""
usuario_fallos = "p"
seleccion_fallo = False
reproducir = False
pausa = False
fin = 600
vertical = False
horizontal = False
vertical2 = False
fallos_estudiante = False
sistema = False
#Definir propiedades ventana principal
ventana = pygame.display.set_mode(dimension_ventana)
pygame.display.set_caption("Tanque")
ventana.fill(color_fondo)
reloj = pygame.time.Clock()
myFont = pygame.font.SysFont("Times New Roman", 18, bold=True)
#myFont2 = pygame.font.SysFont("Times New Roman", 18, bold=True, background = "white")
anuncio = myFont.render("", 1, (255,0,0))
fallo = myFont.render("", 1, (255,0,0))

texto_fallo1= "FALLO 1"
texto_fallo2= "FALLO 2"
texto_fallo3= "FALLO 3"
texto_fallo4= "FALLO 4"
texto_fallo5= "FALLO 5"
texto_fallo6= "FALLO 6"
texto_fallo7= "FALLO 7"
texto_fallo8= "FALLO 8"

lista_fallos = [texto_fallo1, texto_fallo2, texto_fallo3, texto_fallo4, texto_fallo5, texto_fallo6, texto_fallo7, texto_fallo8]

fallo_seleccionado = ""

checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)
checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3) 
checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5) 
checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8)

#Digitar usuario y contraseña
class Input:
    
   def __init__(self):
      self.shift = False
      self.white = (255,255,255)
      self.red = (255,10,10)
      self.black = (0,0,0)
      
   def get_key(self):
      while True:
         event = pygame.event.poll()
         if event.type == pygame.KEYDOWN:
            #print(event.key)
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
               self.shift = True
               continue
               
            if self.shift:
               #return ascii code
               if event.key >= 97 and event.key <= 122:
                  return event.key - 32
               elif event.key == 50:
                  return 64 #return @
               elif event.key == 32:
                  return 32 #return space even if shifted
                  
            elif not self.shift:
               return event.key
         elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
               self.shift = False
         elif event.type == pygame.QUIT:
            sys.exit(0)
         else:
            pass

   def display_box(self, screen, message):
      fontobject = pygame.font.Font(None, 20)
      pygame.draw.rect(screen, self.white,
         ((screen.get_width()) - 450, (screen.get_height()) - 55, 204,30)) #if border add 1 for transp
      
      if len(message) != 0:
         screen.blit(fontobject.render(message, 1 , self.black),
            ((screen.get_width()) - 450, (screen.get_height()) - 50))
      
      pygame.display.update()
      
   def ask(self, screen, question):
      current_string = []      
      current_string_clave=[] #Variable que almacenará una cadena de '*' 
      
      self.display_box(screen, question + ': ' + ''.join(current_string))
      while True:
         inkey = self.get_key()
         if inkey == pygame.K_BACKSPACE:
            #Borrar el último caracter almacenado
            current_string_clave = current_string_clave[0:-1]
            current_string = current_string[0:-1]
            if question == "Clave":
               #Actualizar lo mostrado en pantalla
               self.display_box(screen, question + ': ' + ''.join(current_string_clave))
            else:
               #Actualizar lo mostrado en pantalla
               self.display_box(screen, question + ': ' + ''.join(current_string))
         elif inkey == pygame.K_RETURN:
            break
         else:
            #Adherir la letra ingresada
            current_string.append(chr(inkey))            
            if question == "Clave":
               #Adherir un '*' por cada tecla presionada
               current_string_clave.append('*')
               #Mostrar en pantalla la clave ocultada
               self.display_box(screen, question + ': ' + ''.join(current_string_clave))
            else:
               #Mostrar en pantalla el texto ingresado hasta el momento
               self.display_box(screen, question + ': ' + ''.join(current_string))
               
      return ''.join(current_string)
# Fin digitar usuario y contraseña

#cargar imagenes 
tanque = pygame.image.load('tanque_ppal.png')
logo = pygame.image.load('logoUV.png')
banersup = pygame.image.load('banersup.png')
titulotanque = pygame.image.load('titulo_tanque.png')
tituloanimacion = pygame.image.load('animacion.png')
titulocontrol = pygame.image.load('control.png')
titulofallos = pygame.image.load('fallos.png')
banerinf = pygame.image.load('banersup.png')
bomba = pygame.image.load('bomba.png')
reservorio = pygame.image.load('reservorio.png')
multimetro = pygame.image.load('imagen2.png')
sensor = pygame.image.load('sensor_flujo2.png')
plc = pygame.image.load('koyo_3d_1.png')
bornera1 = pygame.image.load('00450.png')
cablerojo = pygame.image.load('cablerojo3.png')
cableazul = pygame.image.load('cableazul3.png')
cableverde = pygame.image.load('cableverde3.png')
cablenegro = pygame.image.load('cablenegro3.png')
fuente24 = pygame.image.load('fuente24.png')
canaleta_1 = pygame.image.load('canaleta_1.png')
canaleta_2 = pygame.image.load('canaleta_2.png')
estructura_1 = pygame.image.load('estructura_1.png')
estructura_2 = pygame.image.load('estructura_2.png')
cerrarsesion = pygame.image.load('cerrarsesion.png')
bomba_tuberia = pygame.image.load('bomba_tuberia2.png')
reservorio_animacion = pygame.image.load('reservorio_animacion2.png')
tanque_animacion = pygame.image.load('tanque_animacion2.png')
aguares_animacion = pygame.image.load('aguares.png')
aguares_animacion1 = pygame.image.load('aguares1.png')
aguares_animacion2 = pygame.image.load('aguares2.png')
aguares_animacion3 = pygame.image.load('aguares3.png')
planta_inicio = pygame.image.load('planta_ppal.png')
logoUV_inicio = pygame.image.load('logoUV_inicio.png')
zona_autenticacion = pygame.image.load('descripcion.png')
zona_descripcion = pygame.image.load('descripcion.png')
zona_planta = pygame.image.load('zona_planta.png')
zona_superior = pygame.image.load('zona_superior.png')
cajon_cerrado = pygame.image.load('cajon_cerrado.png')
p_id = pygame.image.load('p_id2.png')
tapar_hora = pygame.image.load('hora.png')
punta_negra = pygame.image.load('pinza_negra.png')
punta_roja = pygame.image.load('pinza_roja.png')
caja_motor = pygame.image.load('caja_motor.png')
caja_transmisor = pygame.image.load('caja_transm.png')

# Imagenes Botones
bcontrol = pygame.image.load('boton_control.png') 
bmedicion = pygame.image.load('boton_medicion.png')
btransm = pygame.image.load('boton_transmisor.png')
bp_id = pygame.image.load('boton_p_id.png')
bmotor = pygame.image.load('boton_motor.png')
bppal = pygame.image.load('boton_ppal.png')
bfallos = pygame.image.load('boton_fallos.png')

bseleccionar = pygame.image.load('boton_seleccionar.png')
baceptar = pygame.image.load('boton_aceptar.png')
bcancelar = pygame.image.load('boton_cancelar.png')
bcambiar = pygame.image.load('boton_cambiar.png')

bplay = pygame.image.load('boton_play.png')
bpausa = pygame.image.load('boton_pausa.png')

velocidad_reproduccion = 10

base = 17
altura = 0
baseH = 0
alturaH = 15
baseV = 17
alturaV = 0

x = 262 #Valor inicial (nivel mínimo del tanque)
hv = np.linspace(h0,hf,n)
h = np.zeros([n])
k1 = kv/(2*a*(math.sqrt( h1 )))
k2 = 1/a
vary = 0

#Iniciar ciclo
while True:  
     
    global usuario, hora, mostrar_hora 
    usuario2 = myFont.render(usuario.upper(), True, white)
    hora = str(datetime.now().time())
    mostrar_hora = myFont.render(hora, True, white) 
    logouv1 = myFont.render("Logo UV", True, blue)
    cerrars = myFont.render("Cerrar sesion", True, blue)
    pantallaact = myFont.render("Pantalla actual", True, blue)
    tk_ppl = myFont.render("Tanque principal", True, blue) 
    bomba1 = myFont.render("Bomba", True, blue)
    reser = myFont.render("Reservorio", True, blue) 
    sen = myFont.render("Transmisor", True, blue)
    diag_pid = myFont.render("Diagrama P&ID", True, blue)      
        
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit(0)

        if pantalla_errores: 
           
           mouse = pygame.mouse.get_pos()           
           
           if coordenada_fallo1[0] + dimension_boton_seleccion[0] > mouse[0] > coordenada_fallo1[0] and coordenada_fallo1[1] + dimension_boton_seleccion[1] > mouse[1] > coordenada_fallo1[1]:

              checkbox1.update_checkbox(evento)
        
              if not checkbox1.checked and evento.type == pygame.MOUSEBUTTONDOWN:
                 checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)
                 checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3)                          
                 checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
                 checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5) 
                 checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
                 checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
                 checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8) 
                 fallo_seleccionado = texto_fallo1

           elif coordenada_fallo2[0] + dimension_boton_seleccion[0] > mouse[0] > coordenada_fallo2[0] and coordenada_fallo2[1] + dimension_boton_seleccion[1] > mouse[1] > coordenada_fallo2[1]:

              checkbox2.update_checkbox(evento)
        
              if not checkbox2.checked and evento.type == pygame.MOUSEBUTTONDOWN:
                 checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
                 checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3)                          
                 checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
                 checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5) 
                 checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
                 checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
                 checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8) 
                 fallo_seleccionado = texto_fallo2
                 
           elif coordenada_fallo3[0] + dimension_boton_seleccion[0] > mouse[0] > coordenada_fallo3[0] and coordenada_fallo3[1] + dimension_boton_seleccion[1] > mouse[1] > coordenada_fallo3[1]:

              checkbox3.update_checkbox(evento)
        
              if not checkbox3.checked and evento.type == pygame.MOUSEBUTTONDOWN:
                 checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
                 checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)                          
                 checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
                 checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5) 
                 checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
                 checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
                 checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8) 
                 fallo_seleccionado = texto_fallo3
                 
           elif coordenada_fallo4[0] + dimension_boton_seleccion[0] > mouse[0] > coordenada_fallo4[0] and coordenada_fallo4[1] + dimension_boton_seleccion[1] > mouse[1] > coordenada_fallo4[1]:

              checkbox4.update_checkbox(evento)
        
              if not checkbox4.checked and evento.type == pygame.MOUSEBUTTONDOWN:
                 checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
                 checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)                          
                 checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3) 
                 checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5) 
                 checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
                 checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
                 checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8) 
                 fallo_seleccionado = texto_fallo4
                 
           elif coordenada_fallo5[0] + dimension_boton_seleccion[0] > mouse[0] > coordenada_fallo5[0] and coordenada_fallo5[1] + dimension_boton_seleccion[1] > mouse[1] > coordenada_fallo5[1]:

              checkbox5.update_checkbox(evento)
        
              if not checkbox5.checked and evento.type == pygame.MOUSEBUTTONDOWN:
                 checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
                 checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)                          
                 checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3) 
                 checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
                 checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
                 checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
                 checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8) 
                 fallo_seleccionado = texto_fallo5
                 
           elif coordenada_fallo6[0] + dimension_boton_seleccion[0] > mouse[0] > coordenada_fallo6[0] and coordenada_fallo6[1] + dimension_boton_seleccion[1] > mouse[1] > coordenada_fallo6[1]:

              checkbox6.update_checkbox(evento)
        
              if not checkbox6.checked and evento.type == pygame.MOUSEBUTTONDOWN:
                 checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
                 checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)                          
                 checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3) 
                 checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
                 checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5)
                 checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
                 checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8) 
                 fallo_seleccionado = texto_fallo6
                 
           elif coordenada_fallo7[0] + dimension_boton_seleccion[0] > mouse[0] > coordenada_fallo7[0] and coordenada_fallo7[1] + dimension_boton_seleccion[1] > mouse[1] > coordenada_fallo7[1]:

              checkbox7.update_checkbox(evento)
        
              if not checkbox7.checked and evento.type == pygame.MOUSEBUTTONDOWN:
                 checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
                 checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)                          
                 checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3) 
                 checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
                 checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5)
                 checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
                 checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8) 
                 fallo_seleccionado = texto_fallo7
                 
           elif coordenada_fallo8[0] + dimension_boton_seleccion[0] > mouse[0] > coordenada_fallo8[0] and coordenada_fallo8[1] + dimension_boton_seleccion[1] > mouse[1] > coordenada_fallo8[1]:

              checkbox8.update_checkbox(evento)
        
              if not checkbox8.checked and evento.type == pygame.MOUSEBUTTONDOWN:
                 checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
                 checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)                          
                 checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3) 
                 checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
                 checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5)
                 checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
                 checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7) 
                 fallo_seleccionado = texto_fallo8

           elif 600 > mouse[0] > 400 and 600 > mouse[1] > 550 and evento.type == pygame.MOUSEBUTTONDOWN:
         
                 seleccion_fallo = True     
              
        if loop_control_cerrado:           
           
           if evento.type == pygame.MOUSEBUTTONDOWN:
              
              mouse = pygame.mouse.get_pos()
              
              if 900 > mouse[0] > 850 and 190 > mouse[1] > 150:

                 if fin < 600:
                    pausa = True
                    reproducir = False
                    fin = 600
                 else:
                    reproducir = True
                    vertical = True
                    pausa = False
      
        if fallos_estudiante:

           if evento.type == pygame.MOUSEBUTTONDOWN:

              mouse = pygame.mouse.get_pos()

              if sistema:

                 #Click botón Aceptar
                 if 740 > mouse[0] > 570 and 450 > mouse[1] > 400:

                    loop_ppal=True
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    loop_control_cerrado=False
                    pantalla_errores=False
                    autenticacion=False
                    cambiar_pantalla = False
                    seleccion_fallo = False
                    fallos_estudiante = False

                 #Click botón Cambiar
                 elif 490 > mouse[0] > 320 and 450 > mouse[1] > 400:

                    fallo_seleccionado = ""

                 
              else:
                 
                 #Click botón Aceptar
                 if 620 > mouse[0] > 450 and 450 > mouse[1] > 400:

                    loop_ppal=True
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    loop_control_cerrado=False
                    pantalla_errores=False
                    autenticacion=False
                    cambiar_pantalla = False
                    seleccion_fallo = False
                    fallos_estudiante = False
        

#Pantalla principal    
        
    if loop_ppal:
    
        
        if evento.type == KEYUP:
                if evento.key == K_q:
                  #if x>15: 
                    #x=x-1 
                    t, y = signal.step2(sys_tk) # Respuesta a escalón unitario
                    plt.plot(t, y)
                    plt.ylabel("value of h")  
                    plt.title("Solucion aproximada por metodo de euler")
                    plt.show()
                
                  
                elif evento.key == K_w:           
                     k = k+0.001 
                    
                
                elif evento.key == K_e:           
                     k = k-0.001 
                          
        for i in range(1,n):
             h[i] = h[i-1] + delta*((hv[i] - k*np.sqrt(h[i-1]))/at)
             sys_tk = signal.lti(k2, [1, k1]) # Funcion de transferencia LA
        
        
        
        #for i in range(n):   
          # print(hv[i],h[i])               
        porc = (x*-0.4049) + 106.07 #Ecuación nivel del tanque
        #porc2 = abs(float("{0:.1f}".format(h[i])))
        porc3 = float("{0:.1f}".format(h[i])) #Convertir formato de porc       
        porcentaje = myFont.render(str(porc3), 1, green) 
                                
       # agua =  pygame.transform.scale(masarosa, (140, (262 - int(h[i]))))  # Animacion aumento e incremento de agua
        ventana.blit(estructura_2, coordenada_estructura_2)
        ventana.blit(estructura_2, coordenada_estructura_3)
        ventana.blit(estructura_1, coordenada_estructura_4)
        ventana.blit(estructura_1, coordenada_estructura_5)
        ventana.blit(banersup, coordenada_banersup)
        ventana.blit(logo, coordenada_logo)
        ventana.blit(titulotanque, coordenada_titulo)
        ventana.blit(banerinf, coordenada_banerinf)
        ventana.blit(tanque, coordenada_tanque)
        #ventana.blit(agua, (coordenada_equilibro_masa+1, 240+ int(h[i]))) 
        ventana.blit(bomba, coordenada_bomba)
        ventana.blit(reservorio, coordenada_reservorio)
        ventana.blit(estructura_1, coordenada_estructura_1)
        #ventana.blit(multimetro, coordenada_multimetro)
        ventana.blit(sensor, coordenada_sensor)
        ventana.blit(porcentaje, (318, 370))# Mostrar porcentaje de agua 
        ventana.blit(cerrarsesion, coordenada_cerrarsesion) 
        ventana.blit(usuario2, (180, 18))
        ventana.blit(mostrar_hora, (180, 37))
        ventana.blit(tapar_hora, (247, 37))
        ventana.blit(bcontrol, (80, 660))
        ventana.blit(bfallos, (300, 660)) 
        ventana.blit(bmedicion, (450, 80))
        ventana.blit(btransm, (600, 80))
        ventana.blit(bp_id, (750, 80))
        ventana.blit(bmotor, (900, 80))

# Leer actividad de mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(mouse)

        # Click botón fallos
        if 470 > mouse[0] > 300 and 711 > mouse[1] > 660:
           #print(click[0])
           if click[0]:  
              if usuario == usuario_fallos:
                 
                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=True
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = False
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
              else:

                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=False
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = True
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        # Click botón control        
        elif 250 > mouse[0] > 80 and 711 > mouse[1] > 660:
           if click[0]:
              loop_ppal=False
              loop_ppal_medicion=False
              loop_sec_medicion=False
              loop_sec=False  
              loop_control_cerrado=True
              pantalla_errores=False
              autenticacion=False
              pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
              time.sleep(0.5) #Pausa la ejecución del programa
              pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento

# Botones lado derecho

        # Mostrar multimetro
        if 564 > mouse[0] > 450 and 118 > mouse[1] > 80:
           if click[0] == 1:
              loop_ppal=False
              loop_sec=False
              loop_ppal_medicion=True
              loop_sec_medicion=False
              animacion_tanque=False
              loop_control_cerrado=False
              pantalla_errores = False        
        
        # Mostrar P&ID
        if 864 > mouse[0] > 750 and 118 > mouse[1] > 80:
           if click[0] == 1: 
              v_motor = 0
              v_trans = 0
              v_pid = 1 
        
        if v_pid == 1:
           ventana.blit(p_id, coordenada_p_id) 
               
        # Mostrar caja transmisor
        if 715 > mouse[0] > 600 and 118 > mouse[1] > 80:
           if click[0] == 1:
              v_pid = 0
              v_motor = 0
              v_transm = 1 
        
        if v_transm == 1:
           ventana.blit(caja_transmisor, coordenada_p_id) 

        # Mostrar caja motor
        if 1014 > mouse[0] > 900 and 118 > mouse[1] > 80:
           if click[0] == 1:
              v_transm = 0 
              v_pid = 0
              v_motor = 1
                
        if v_motor == 1:
           ventana.blit(caja_motor, coordenada_p_id)

               
# Condición para cerrar sesión
        if 152 > mouse[0] > 100 and 60 > mouse[1] > 10:
            ventana.blit(cerrars, mouse)
            if click[0] == 1:
                 variable_cerrarsesion = 1
                           
# Mostrar descripciones según posición del mouse
        
        elif 970 > mouse[0] > 640 and 60 > mouse[1] > 15:
            ventana.blit(pantallaact, mouse)
        
        elif 70 > mouse[0] > 0 and 70 > mouse[1] > 0:
            ventana.blit(logouv1, mouse)  

        elif 226 > mouse[0] > 162 and 440 > mouse[1] > 104:
            ventana.blit(tk_ppl, mouse)  

        elif 130 > mouse[0] > 56 and 630 > mouse[1] > 586:
            ventana.blit(bomba1, mouse)              

        elif 247 > mouse[0] > 135 and 634 > mouse[1] > 485:
            ventana.blit(reser, mouse)
            
        elif 360 > mouse[0] > 303 and 473 > mouse[1] > 359:
            ventana.blit(sen, mouse)                 

# Cerrar sesión e ir a pantalla de autenticación              
        if variable_cerrarsesion == 1:
            loop_ppal=False
            loop_ppal_medicion=False
            loop_sec_medicion=False
            loop_sec=False  
            loop_control_cerrado=False
            pantalla_errores=False
            autenticacion=True
            
                               
        pygame.display.update()
        pygame.display.flip()
        ventana.fill(color_fondo)
        reloj.tick(fps)
 
#Pantalla principal modo medicion       
    if loop_ppal_medicion: 
        
        
        if evento.type == KEYUP:
                if evento.key == K_q:
                    t, y = signal.step2(sys_tk) # Respuesta a escalón unitario
                    plt.plot(t, y)
                    plt.ylabel("value of h")  
                    plt.title("Solucion aproximada por metodo de euler")
                    plt.show()
                
                  
                elif evento.key == K_w:           
                     k = k+0.001 
                    
            
#Función  de transferencia en LA                          
        for i in range(1,n):
             h[i] = h[i-1] + delta*((hv[i] - k*np.sqrt(h[i-1]))/at)
             sys_tk = signal.lti(k2, [1, k1]) # Funcion de transferencia LA
        
        
        #for i in range(n):   
          # print(hv[i],h[i])               
        porc = (x*-0.4049) + 106.07 #Ecuación nivel del tanque
        #porc2 = abs(float("{0:.1f}".format(porc)))
        porc3 = float("{0:.1f}".format(h[i])) #Convertir formato de porc       
        porcentaje = myFont.render(str(porc3), 1, green)
            
        
        ventana.blit(estructura_2, coordenada_estructura_2)
        ventana.blit(estructura_2, coordenada_estructura_3)
        ventana.blit(estructura_1, coordenada_estructura_4)
        ventana.blit(estructura_1, coordenada_estructura_5)
        ventana.blit(banersup, coordenada_banersup)
        ventana.blit(logo, coordenada_logo)
        ventana.blit(titulotanque, coordenada_titulo)
        ventana.blit(banerinf, coordenada_banerinf)
        ventana.blit(tanque, coordenada_tanque)
        ventana.blit(bomba, coordenada_bomba)
        ventana.blit(reservorio, coordenada_reservorio)
        ventana.blit(estructura_1, coordenada_estructura_1)
        ventana.blit(multimetro, coordenada_multimetro)
        ventana.blit(sensor, coordenada_sensor)
        ventana.blit(porcentaje, (318, 370))# Mostrar porcentaje de agua  
        ventana.blit(cerrarsesion, coordenada_cerrarsesion)  
        ventana.blit(usuario2, (180, 18))
        ventana.blit(mostrar_hora, (180, 37))
        ventana.blit(tapar_hora, (247, 37))
        ventana.blit(btransm, (600, 80))
        ventana.blit(bp_id, (750, 80))
        ventana.blit(bmotor, (900, 80))
        ventana.blit(bcontrol, (80, 660))
        ventana.blit(bfallos, (300, 660))
        
# Leer actividad de mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(mouse)
        
        # Click botón control
        if 250 > mouse[0] > 80 and 711 > mouse[1] > 660:
           if click[0] == 1: 
                loop_ppal=False
                loop_ppal_medicion=False
                loop_sec_medicion=False
                loop_sec=False  
                pantalla_errores=False
                autenticacion=False 
                loop_control_cerrado=True                
                pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                time.sleep(0.5) #Pausa la ejecución del programa
                pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
        # Click botón fallos
        elif 470 > mouse[0] > 300 and 711 > mouse[1] > 660:
           if click[0] == 1:

              if usuario == usuario_fallos:
                 
                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=True
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = False
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
              else:

                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=False
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = True
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
                  

# Botones lado derecho
        
        # Mostrar P&ID
        if 864 > mouse[0] > 750 and 118 > mouse[1] > 80:
           if click[0] == 1:  
              v_motor = 0
              v_transm = 0
              v_pid = 1
        
        if v_pid == 1:
           ventana.blit(p_id, coordenada_p_id) 
               
        # Mostrar caja transmisor
        if 715 > mouse[0] > 600 and 118 > mouse[1] > 80:
           if click[0] == 1: 
              v_pid = 0
              v_motor = 0
              v_transm = 1
        
        if v_transm == 1:
           ventana.blit(caja_transmisor, coordenada_p_id) 

        # Mostrar caja motor
        if 1014 > mouse[0] > 900 and 118 > mouse[1] > 80:
           if click[0] == 1:
              v_transm = 0 
              v_pid = 0
              v_motor = 1
                
        if v_motor == 1:
           ventana.blit(caja_motor, coordenada_p_id) 

# Condición para cerrar sesión            
        if 152 > mouse[0] > 100 and 60 > mouse[1] > 10:
            ventana.blit(cerrars, mouse)
            if click[0] == 1:
                 variable_cerrarsesion = 1                  

# Mostrar descripciones según posición del mouse                
        elif 970 > mouse[0] > 640 and 60 > mouse[1] > 15:
            ventana.blit(pantallaact, mouse)
        
        elif 70 > mouse[0] > 0 and 70 > mouse[1] > 0:
            ventana.blit(logouv1, mouse) 
            
        elif 226 > mouse[0] > 162 and 440 > mouse[1] > 104:
            ventana.blit(tk_ppl, mouse)  

        elif 130 > mouse[0] > 56 and 630 > mouse[1] > 586:
            ventana.blit(bomba1, mouse)              

        elif 247 > mouse[0] > 135 and 634 > mouse[1] > 485:
            ventana.blit(reser, mouse)
            
        elif 360 > mouse[0] > 303 and 473 > mouse[1] > 359:
            ventana.blit(sen, mouse)

        elif 765 > mouse[0] > 472 and 597 > mouse[1] > 217:
            ventana.blit(diag_pid, mouse) 
            
# Cerrar sesión e ir a pantalla de autenticación                 
        if variable_cerrarsesion == 1:
            loop_ppal=False
            loop_ppal_medicion=False
            loop_sec_medicion=False
            loop_sec=False  
            loop_control_cerrado=False
            pantalla_errores=False
            autenticacion=True
               
    # Medición de corriente        
        if 835 > mouse[0] > 815 and 225 > mouse[1] > 210:
            if click[0] == 1:
                variable_cambio = 1   
                print(mouse)  
                pygame.draw.line(ventana, (30, 0, 20), origen, evento.pos, 5) 
                 
    # Medición de voltaje        
        elif 860 > mouse[0] > 840 and 225 > mouse[1] > 210:
            if click[0] == 1: 
                variable_cambio = 2  
                print(mouse)  
                pygame.draw.line(ventana, (30, 0, 20), origen, evento.pos, 5)  
    
    # Medición de resistencia        
        elif 885 > mouse[0] > 864 and 225 > mouse[1] > 210:
            if click[0] == 1:
                variable_cambio = 3  
                print(mouse)   
                pygame.draw.line(ventana, (30, 0, 20), origen, evento.pos, 5)
            
    # Acciones en modo medición de corriente        
        if variable_cambio == 1:
            if 858 > mouse[0] > 844 and 280 > mouse[1] > 264 and click[0] == 1:
                variable_cambio2 = 1
                  
        if variable_cambio2 == 1:  
            pygame.draw.line(ventana, (30, 0, 20), (850,270), (850, 400), 5)       
                            
        #agua =  pygame.transform.scale(masarosa, (140, (262 - int(h[i]))))  # Animacion aumento e incremento de agua

        
            
        pygame.display.update()
        pygame.display.flip()
        ventana.fill(color_fondo)
        reloj.tick(fps) 
            
            
#Pantalla de animacion

    if loop_control_cerrado: 
        
        logouv1 = myFont.render("Logo UV", True, blue)
        cerrars = myFont.render("Cerrar sesion", True, blue)
        pantallaact = myFont.render("Pantalla actual", True, blue)
        anim = myFont.render("Animacion", True, blue)
        cajon = myFont.render("Control cerrado", True, blue)
        abrir = myFont.render("Abrir cajon de control", True, blue)
        ventana.blit(bomba_tuberia, coordenada_bomba_tuberia)
        ventana.blit(reservorio_animacion, coordenada_reservorio_animacion)
        ventana.blit(tanque_animacion, coordenada_tanque_animacion)
        ventana.blit(banersup, coordenada_banersup)
        ventana.blit(banerinf, coordenada_banerinf)
        ventana.blit(logo, coordenada_logo)
        ventana.blit(tituloanimacion, coordenada_titulo)
        ventana.blit(aguares_animacion1, coordenada_aguares1_animacion)
        ventana.blit(cerrarsesion, coordenada_cerrarsesion) 
        ventana.blit(usuario2, (180, 18))
        ventana.blit(mostrar_hora, (180, 37))
        ventana.blit(tapar_hora, (247, 37))
        ventana.blit(cajon_cerrado, coordenada_cajon_cerrado)
        ventana.blit(zona_descripcion, (0,75))
        ventana.blit(zona_descripcion, (515,75))
        agua =  pygame.transform.scale(aguares_animacion3, (17, (440 - int(x)))) 
        ventana.blit(agua, (544, 202+ int(x))) 
        ventana.blit(bppal, (80, 660))
        ventana.blit(bfallos, (300, 660))
        ventana.blit(bplay, (850, 150))

        if reproducir:
           ventana.blit(bpausa, (850, 150))
           pygame.draw.rect(ventana, (0,162,232), (544, 465, base, altura))
              
           if vertical:
                                
              if abs(altura) >= 320:
                 fin = 601
                 vertical = False
                 horizontal = True
                 
              elif fin % velocidad_reproduccion == 0:
                 altura -= 20

              fin -= 1

           elif horizontal:              
              pygame.draw.rect(ventana, (0,162,232), (544, 144, baseH, alturaH))
           #561
              if baseH >= 200:
                 horizontal = False
                 vertical2 = True
                 fin = 601
                 
              elif fin % velocidad_reproduccion == 0:
                 baseH += 20

              fin -= 1

           elif vertical2:
              pygame.draw.rect(ventana, (0,162,232), (544, 144, baseH, alturaH))
           
              pygame.draw.rect(ventana, (0,162,232), (744, 144, baseV, alturaV))
           
              if alturaV >= 50:
                 reproducir = False
                 pausa = False                 
                 vertical2 = False
                 fin = 601
                 base = 17
                 altura = 0
                 baseH = 0
                 alturaH = 15
                 baseV = 17
                 alturaV = 0
              elif fin % velocidad_reproduccion == 0:
                 alturaV += 20

              fin -= 1

        if pausa:
           
           ventana.blit(bplay, (850, 150))
           pygame.draw.rect(ventana, (0,162,232), (544, 465, base, altura))

           if horizontal:
              pygame.draw.rect(ventana, (0,162,232), (544, 144, baseH, alturaH))
           elif vertical2:              
              pygame.draw.rect(ventana, (0,162,232), (544, 144, baseH, alturaH))
              pygame.draw.rect(ventana, (0,162,232), (744, 144, baseV, alturaV))

           

# Leer actividad de mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(mouse)
        
        # Click botón ppal
        if 250 > mouse[0] > 80 and 711 > mouse[1] > 660:
           if click[0] == 1:  
                loop_ppal=True
                loop_ppal_medicion=False
                loop_sec_medicion=False
                loop_sec=False  
                loop_control_cerrado=False
                pantalla_errores=False
                autenticacion=False                
                pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                time.sleep(0.5) #Pausa la ejecución del programa
                pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
                
        # Click botón Fallos
        elif 470 > mouse[0] > 300 and 711 > mouse[1] > 660:
           if click[0] == 1:  
              if usuario == usuario_fallos:
                 
                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=True
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = False
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
              else:

                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=False
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = True
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
# Mostrar descripción de campo        
        if 951 > mouse[0] > 540  and 649 > mouse[1] > 138:
            ventana.blit(anim, mouse)
            
            
        elif 970 > mouse[0] > 640 and 60 > mouse[1] > 15:
            ventana.blit(pantallaact, mouse)
        
        elif 70 > mouse[0] > 0 and 70 > mouse[1] > 0:
            ventana.blit(logouv1, mouse)
            
        elif 136 > mouse[0] > 123 and 434 > mouse[1] > 395:
            ventana.blit(abrir, mouse)
            if click[0] == 1:
               loop_ppal=False
               loop_ppal_medicion=False
               loop_sec_medicion=False
               loop_sec=True 
               loop_control_cerrado=False
               pantalla_errores=False
               autenticacion=False    

# Animar tanque

        if 0 < mouse[0] < 100 and 0 < mouse[1] < 100:
           if click[0] == 1:
              var = 2
    
        #print(var)
    
        if var == 2:
          for i in range(1, 62):
             x = x-1   
        var = 0

# Cerrar sesion        
        if 152 > mouse[0] > 100 and 60 > mouse[1] > 10: 
           ventana.blit(cerrars, mouse)
           if click[0] == 1:
             variable_cerrarsesion = 1  
        
        if variable_cerrarsesion == 1:
            loop_ppal=False
            loop_ppal_medicion=False
            loop_sec_medicion=False
            loop_sec=False  
            loop_control_cerrado=False
            pantalla_errores=False
            autenticacion=True
           
        pygame.display.update()
        pygame.display.flip()
        ventana.fill(color_fondo)
        reloj.tick(fps)                    
            
#Pantalla control    
    if loop_sec:

        
        ventana.blit(canaleta_2, coordenada_canaleta_4)
        ventana.blit(canaleta_2, coordenada_canaleta_2)
        ventana.blit(plc, coordenada_plc)
        #ventana.blit(multimetro, coordenada_multimetro)
        ventana.blit(bornera1, coordenada_bornera1)
        ventana.blit(cablerojo, coordenada_cablerojo)
        ventana.blit(cableazul, coordenada_cableazul)
        ventana.blit(cableverde, coordenada_cableverde)
        ventana.blit(cablenegro, coordenada_cablenegro)
        ventana.blit(banerinf, coordenada_banerinf)
        ventana.blit(fuente24, coordenada_fuente24)
    
        cablerojo2 = pygame.transform.rotate(cablerojo, 180)
        ventana.blit(cablerojo2, (102, 458))
        cableazul2 = pygame.transform.rotate(cableazul, 180)
        ventana.blit(cableazul2, (125, 458))
        cableverde2 = pygame.transform.rotate(cableverde, 180)
        ventana.blit(cableverde2, (146, 458))
        cablenegro2 = pygame.transform.rotate(cablenegro, 180)
        ventana.blit(cablenegro2, (169, 458))
        ventana.blit(canaleta_1, coordenada_canaleta_1)
        ventana.blit(canaleta_1, coordenada_canaleta_3)
        ventana.blit(banersup, coordenada_banersup)
        ventana.blit(logo, coordenada_logo)
        ventana.blit(titulocontrol, coordenada_titulo)
        ventana.blit(cerrarsesion, coordenada_cerrarsesion) 
        ventana.blit(usuario2, (180, 18))
        ventana.blit(mostrar_hora, (180, 37))
        ventana.blit(tapar_hora, (247, 37))
        ventana.blit(bppal, (80, 660))
        ventana.blit(bfallos, (300, 660))
        
# Marquillas del cableado   
        texto = myFont.render("Vcc", True, black)
        texto = pygame.transform.rotate(texto, 90)
        ventana.blit(texto, coordenada_texcablerojo)
        
        textognd = myFont.render("GND", True, black)
        textognd= pygame.transform.rotate(textognd, 90)
        ventana.blit(textognd, coordenada_texcableverde)        

# Leer actividad de mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(mouse)
        
        # Click botón ppal
        if 250 > mouse[0] > 80 and 711 > mouse[1] > 660:
           #print(click[0])
           if click[0]:  
                loop_ppal=True
                loop_ppal_medicion=False
                loop_sec_medicion=False
                loop_sec=False  
                loop_control_cerrado=False
                pantalla_errores=False
                autenticacion=False 
                pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                time.sleep(0.5) #Pausa la ejecución del programa
                pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
                
        # Click botón fallos
        elif 470 > mouse[0] > 300 and 711 > mouse[1] > 660:
           #print(click[0])
           if click[0]:  
              if usuario == usuario_fallos:
                 
                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=True
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = False
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
              else:

                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=False
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = True
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
# Cerrar sesion        
        if 152 > mouse[0] > 100 and 60 > mouse[1] > 10:
            ventana.blit(cerrars, mouse)
            if click[0] == 1:
                 variable_cerrarsesion = 1  

# Mostrar descripcion de campo                
        elif 970 > mouse[0] > 640 and 60 > mouse[1] > 15:
            ventana.blit(pantallaact, mouse)
        
        elif 70 > mouse[0] > 0 and 70 > mouse[1] > 0:
            ventana.blit(logouv1, mouse)                
        
        if variable_cerrarsesion == 1:
            loop_ppal=False
            loop_ppal_medicion=False
            loop_sec_medicion=False
            loop_sec=False  
            loop_control_cerrado=False
            pantalla_errores=False
            autenticacion=True
           
        pygame.display.update()
        pygame.display.flip()
        ventana.fill(color_fondo)
        reloj.tick(fps)  


    if loop_sec_medicion:

        
        for i in range(1,n):
             h[i] = h[i-1] + delta*((hv[i] - k*np.sqrt(h[i-1]))/at)
             sys_tk = signal.lti(k2, [1, k1]) # Funcion de transferencia LA
        
        ventana.blit(canaleta_2, coordenada_canaleta_4)
        ventana.blit(canaleta_2, coordenada_canaleta_2)
        ventana.blit(plc, coordenada_plc)
        ventana.blit(multimetro, coordenada_multimetro)
        ventana.blit(bornera1, coordenada_bornera1)
        ventana.blit(cablerojo, coordenada_cablerojo)
        ventana.blit(cableazul, coordenada_cableazul)
        ventana.blit(cableverde, coordenada_cableverde)
        ventana.blit(cablenegro, coordenada_cablenegro)
        ventana.blit(banerinf, coordenada_banerinf)
        ventana.blit(fuente24, coordenada_fuente24)
    
        cablerojo2 = pygame.transform.rotate(cablerojo, 180)
        ventana.blit(cablerojo2, (102, 458))
        cableazul2 = pygame.transform.rotate(cableazul, 180)
        ventana.blit(cableazul2, (125, 458))
        cableverde2 = pygame.transform.rotate(cableverde, 180)
        ventana.blit(cableverde2, (146, 458))
        cablenegro2 = pygame.transform.rotate(cablenegro, 180)
        ventana.blit(cablenegro2, (169, 458))
        ventana.blit(canaleta_1, coordenada_canaleta_1)
        ventana.blit(canaleta_1, coordenada_canaleta_3)
        ventana.blit(banersup, coordenada_banersup)
        ventana.blit(logo, coordenada_logo)
        ventana.blit(titulocontrol, coordenada_titulo)
        ventana.blit(cerrarsesion, coordenada_cerrarsesion) 
        ventana.blit(usuario2, (180, 18))
        ventana.blit(mostrar_hora, (180, 37))
        ventana.blit(tapar_hora, (247, 37))
        ventana.blit(bppal, (80, 660))
        ventana.blit(bfallos, (300, 660))
        
# Marquillas del cableado   
        texto = myFont.render("Vcc", True, black)
        texto = pygame.transform.rotate(texto, 90)
        ventana.blit(texto, coordenada_texcablerojo)
        
        textognd = myFont.render("GND", True, black)
        textognd= pygame.transform.rotate(textognd, 90)
        ventana.blit(textognd, coordenada_texcableverde)
 
#Ecuaciones de nivel        
        
        porc = (x*-0.4049) + 106.07 #Ecuación nivel del tanque
        porc2 = abs(float("{0:.1f}".format(porc)))
        porc3 = float("{0:.1f}".format(h[i])) #Convertir formato de porc       
        porcentaje = myFont.render(str(porc3), 1, black) 
        vcc24 = myFont.render("24", 1, black)
        
# Leer actividad de mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(mouse) 

        # Click botón ppal
        if 470 > mouse[0] > 300 and 711 > mouse[1] > 660:
           #print(click[0])
           if click[0]:  
                loop_ppal=True
                loop_ppal_medicion=False
                loop_sec_medicion=False
                loop_sec=False  
                loop_control_cerrado=False
                pantalla_errores=False
                autenticacion=False
                pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                time.sleep(0.5) #Pausa la ejecución del programa
                pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
                
        # Click botón fallos
        elif 250 > mouse[0] > 80 and 711 > mouse[1] > 660:
           #print(click[0])
           if click[0]:  
              if usuario == usuario_fallos:
                 
                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=True
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = False
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
              else:

                    loop_ppal=False
                    loop_ppal_medicion=False
                    loop_sec_medicion=False
                    loop_sec=False  
                    pantalla_errores=False
                    autenticacion=False 
                    loop_control_cerrado=False
                    fallos_estudiante = True
                    pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                    time.sleep(0.5) #Pausa la ejecución del programa
                    pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
        
        elif 152 > mouse[0] > 100 and 60 > mouse[1] > 10:
            ventana.blit(cerrars, mouse)
            if click[0] == 1:
                 variable_cerrarsesion = 1  
                
#Mostrar descripcion de campo

        elif 970 > mouse[0] > 640 and 60 > mouse[1] > 15:
            ventana.blit(pantallaact, mouse)
        
        elif 70 > mouse[0] > 0 and 70 > mouse[1] > 0:
            ventana.blit(logouv1, mouse)
                
        if variable_cerrarsesion == 1:
            loop_ppal=False
            loop_ppal_medicion=False
            loop_sec_medicion=False
            loop_sec=False  
            loop_control_cerrado=False
            pantalla_errores=False
            autenticacion=True
           
# Medición de voltaje        
        if 860 > mouse[0] > 840 and 225 > mouse[1] > 210:
           if click[0] == 1: 
             variable_cambio_sec = 2    
             pygame.draw.line(ventana, (30, 0, 20), origen, evento.pos, 5)
                       
# Acciones en modo medicion de voltaje             
        if variable_cambio_sec == 2:
           if 166 > mouse[0] > 156 and 590 > mouse[1] > 570 and click[0] == 1:
              variable_cambio_sec2 = 2
              posxy = mouse  
        
        if variable_cambio_sec2 == 2:
            ventana.blit(punta_negra, posxy)          
            if 120 > mouse[0] > 112 and 595 > mouse[1] > 570 and click[0] == 1:
               variable_cambio_sec3 = 2
               posxy2 = mouse 
            
        if variable_cambio_sec3 == 2:
            ventana.blit(punta_roja, posxy2)
            ventana.blit(vcc24, (835, 166))
            
# Fin de acciones en modo medición de voltaje            
                   
        pygame.display.update()
        pygame.display.flip()
        ventana.fill(color_fondo)
        reloj.tick(fps)
       
          
# Pantalla registro                            
    if autenticacion:
        
        descripcion = myFont.render("La herramienta para formacion en diagnostico de fallas en", True, black) 
        descripcion2 = myFont.render("sistemas de control que fue diseñada para promover el", True, black)
        descripcion3 = myFont.render("aprendizaje activo y la construccion de conocimiento", True, black)
        nombre_app = myFont.render("HERRAMIENTA VIRTUAL PARA FORMACION ", True, white)
        nombre_app2 = myFont.render("EN DIAGNOSTICO DE FALLAS EN SISTEMAS DE CONTROL", True, white)
        titulo_descripcion = myFont.render("Descripcion de la herramienta", True, white)
        titulo_autenticacion = myFont.render("Autenticacion de usuario", True, white)
        variable_cerrarsesion = 0
        ventana.blit(zona_superior, coordenada_zona_superior)
        ventana.blit(zona_planta, coordenada_zona_planta)
        ventana.blit(zona_descripcion, coordenada_zona_descripcion)
        ventana.blit(zona_autenticacion, coordenada_zona_autenticacion)
        ventana.blit(planta_inicio, coordenada_planta_inicio)
        ventana.blit(logoUV_inicio, coordenada_logoUV_inicio)
        ventana.blit(nombre_app, (320,30))
        ventana.blit(nombre_app2, (260,47))
        ventana.blit(titulo_descripcion, (650,120))
        ventana.blit(titulo_autenticacion, (670,610))
        ventana.blit(descripcion, (540,170))
        ventana.blit(descripcion2, (540,190))
        ventana.blit(descripcion3, (540,210))
        #ventana =  pygame.display.set_mode((400, 400))
        input_box = Input()
        usuario = input_box.ask(ventana, 'Usuario')
        #print(usuario + ' was entered')

        clave = input_box.ask(ventana, 'Clave')
        #print(clave + ' was entered')  

                        
        pygame.display.update()
        pygame.display.flip()
        ventana.fill(color_fondo)
        reloj.tick(fps)        
        
        
        if usuario == "e" and clave == "e":
            loop_ppal = False
            loop_sec = True
            autenticacion = False 
            loop_ppal_medicion = False
            loop_sec_medicion = False
            loop_control_cerrado= False
            pantalla_errores = False
            
        
        elif usuario == "p" and clave == "p":
            loop_ppal = False
            loop_sec = False
            autenticacion = False
            loop_ppal_medicion = False
            loop_sec_medicion = True
            loop_control_cerrado=False
            pantalla_errores = False

            
        elif usuario == "" and clave == "":
            loop_ppal = False
            loop_sec = False
            autenticacion = True
            loop_ppal_medicion = False
            loop_sec_medicion = False
            loop_control_cerrado=False
            pantalla_errores = False
            
        else: 
            errorusuario = myFont.render("Usuario o clave incorrectos", 1, (255,0,0))
            ventana.blit(errorusuario, (800, 670))             
            time.sleep( 1 )

    
# Pantalla Fallos

    if pantalla_errores:
       
        ventana.blit(banersup, coordenada_banersup)
        ventana.blit(logo, coordenada_logo)
        ventana.blit(titulofallos, coordenada_titulo)
        ventana.blit(cerrarsesion, coordenada_cerrarsesion) 
        ventana.blit(usuario2, (180, 18))
        ventana.blit(mostrar_hora, (180, 37))
        ventana.blit(tapar_hora, (247, 37))
        ventana.blit(banerinf, coordenada_banerinf)
        ventana.blit(bppal, (80, 660))
        ventana.blit(bcontrol, (300, 660))
        ventana.blit(bseleccionar, (400, 550))
        
        # Leer actividad de mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()        
        #print(mouse)
                
        # Click botón ppal
        if 250 > mouse[0] > 80 and 711 > mouse[1] > 660:
           
           if click[0]:  
                loop_ppal=True
                loop_ppal_medicion=False
                loop_sec_medicion=False
                loop_sec=False  
                loop_control_cerrado=False
                pantalla_errores=False
                autenticacion=False
                cambiar_pantalla = False
                pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                time.sleep(0.5) #Pausa la ejecución del programa
                pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
                
        # Click botón control
        elif 470 > mouse[0] > 300 and 711 > mouse[1] > 660:
           #print(click[0])
           if click[0]:  
                loop_ppal=False
                loop_ppal_medicion=False
                loop_sec_medicion=False
                loop_sec=False  
                loop_control_cerrado=True
                pantalla_errores=False
                autenticacion=False
                pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                time.sleep(0.5) #Pausa la ejecución del programa
                pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
                
        # Cerrar sesion        
        elif 152 > mouse[0] > 100 and 60 > mouse[1] > 10:
            ventana.blit(cerrars, mouse)
            if click[0] == 1:
                 variable_cerrarsesion = 1

        elif 970 > mouse[0] > 640 and 60 > mouse[1] > 15:
            ventana.blit(pantallaact, mouse)
        
        elif 70 > mouse[0] > 0 and 70 > mouse[1] > 0:
            ventana.blit(logouv1, mouse)
        
        
        # Cerrar sesión e ir a pantalla de autenticación              
        if variable_cerrarsesion == 1:
            loop_ppal=False
            loop_ppal_medicion=False
            loop_sec_medicion=False
            loop_sec=False  
            loop_control_cerrado=False
            pantalla_errores=False
            autenticacion=True

        if not seleccion_fallo:
           
           checkbox1.render_checkbox()
           checkbox2.render_checkbox()
           checkbox3.render_checkbox()
           checkbox4.render_checkbox()
           checkbox5.render_checkbox()
           checkbox6.render_checkbox()
           checkbox7.render_checkbox()        
           checkbox8.render_checkbox()

        else:

           if not checkbox1.checked and not checkbox2.checked and not checkbox3.checked and not checkbox4.checked and not checkbox5.checked and not checkbox6.checked and not checkbox7.checked and not checkbox8.checked:

              anuncio = myFont.render("Usted NO ha seleccionado fallo alguno.", 1, (255,0,0))
                            
              ventana.fill(color_fondo)
              ventana.blit(banersup, coordenada_banersup)
              ventana.blit(logo, coordenada_logo)
              ventana.blit(titulofallos, coordenada_titulo)
              ventana.blit(cerrarsesion, coordenada_cerrarsesion) 
              ventana.blit(usuario2, (180, 18))
              ventana.blit(mostrar_hora, (180, 37))
              ventana.blit(tapar_hora, (247, 37))
              ventana.blit(banerinf, coordenada_banerinf)
              ventana.blit(anuncio, (400, 300))
              ventana.blit(baceptar, (450, 350))

              #Click botón Aceptar
              if 620 > mouse[0] > 450 and 400 > mouse[1] > 350 and click[0]:

                 loop_ppal=False
                 loop_ppal_medicion=False
                 loop_sec_medicion=False
                 loop_sec=False  
                 loop_control_cerrado=False
                 pantalla_errores=True
                 autenticacion=False
                 cambiar_pantalla = False
                 seleccion_fallo = False
                 fallo_seleccionado = ""
                 pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                 time.sleep(0.5) #Pausa la ejecución del programa
                 pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 

           else:
              anuncio = myFont.render("Usted ha seleccionado el fallo:", 1, (255,0,0))
              fallo = myFont.render(fallo_seleccionado, 1, (255,0,0))
              ventana.fill(color_fondo)
              ventana.blit(banersup, coordenada_banersup)
              ventana.blit(logo, coordenada_logo)
              ventana.blit(titulofallos, coordenada_titulo)
              ventana.blit(cerrarsesion, coordenada_cerrarsesion) 
              ventana.blit(usuario2, (180, 18))
              ventana.blit(mostrar_hora, (180, 37))
              ventana.blit(tapar_hora, (247, 37))
              ventana.blit(banerinf, coordenada_banerinf)
              ventana.blit(anuncio, (400,300))
              ventana.blit(fallo, (470,350))
              ventana.blit (bcancelar, (300, 400))
              ventana.blit (baceptar, (550, 400))
              
              #Click botón Aceptar
              if 720 > mouse[0] > 550 and 450 > mouse[1] > 400 and click[0]:
                 loop_ppal=True
                 loop_ppal_medicion=False
                 loop_sec_medicion=False
                 loop_sec=False  
                 loop_control_cerrado=False
                 pantalla_errores=False
                 autenticacion=False
                 cambiar_pantalla = False
                 seleccion_fallo = False
                 pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                 time.sleep(0.5) #Pausa la ejecución del programa
                 pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento 
              
              #Click botón Cancelar   
              elif 470 > mouse[0] > 300 and 450 > mouse[1] > 400 and click[0]:
                 loop_ppal=False
                 loop_ppal_medicion=False
                 loop_sec_medicion=False
                 loop_sec=False  
                 loop_control_cerrado=False
                 pantalla_errores=True
                 autenticacion=False
                 cambiar_pantalla = False
                 seleccion_fallo = False                 
                 fallo_seleccionado = ""
                 checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
                 checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)
                 checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3) 
                 checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
                 checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5) 
                 checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
                 checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
                 checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8)

                 pygame.event.clear() #Borra todos los eventos que ocurrieron hasta el momento 
                 time.sleep(0.5) #Pausa la ejecución del programa
                 pygame.event.clear()#Borra todos los eventos que ocurrieron hasta el momento

           
        pygame.display.update()
        pygame.display.flip()               
        ventana.fill(color_fondo)
        reloj.tick(fps) 

    if fallos_estudiante:

       if fallo_seleccionado == "":
          fallo_seleccionado = random.choice(lista_fallos)
          checkbox1 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo1, texto_fallo1)
          checkbox2 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo2, texto_fallo2)
          checkbox3 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo3, texto_fallo3) 
          checkbox4 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo4, texto_fallo4) 
          checkbox5 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo5, texto_fallo5) 
          checkbox6 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo6, texto_fallo6)
          checkbox7 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo7, texto_fallo7)
          checkbox8 = checkButtons.Checkbox(ventana, dimension_boton_seleccion, coordenada_fallo8, texto_fallo8)

          sistema = True
       else:
          if sistema:
             anuncio = myFont.render("El sistema ha seleccionado el fallo:", 1, (255,0,0))
             fallo = myFont.render(fallo_seleccionado, 1, (255,0,0))
             ventana.blit(baceptar, (570, 400))
             ventana.blit(bcambiar, (320, 400))
          else:
             anuncio = myFont.render("El docente ha seleccionado el fallo:", 1, (255,0,0))
             fallo = myFont.render(fallo_seleccionado, 1, (255,0,0))
             sistema = False
             ventana.blit(baceptar, (450, 400))
       
       ventana.blit(banersup, coordenada_banersup)
       ventana.blit(logo, coordenada_logo)
       ventana.blit(titulofallos, coordenada_titulo)
       ventana.blit(cerrarsesion, coordenada_cerrarsesion) 
       ventana.blit(usuario2, (180, 18))
       ventana.blit(mostrar_hora, (180, 37))
       ventana.blit(tapar_hora, (247, 37))
       ventana.blit(banerinf, coordenada_banerinf)
       ventana.blit(anuncio, (400, 300))
       ventana.blit(fallo, (500, 350))       

       # Leer actividad de mouse
       mouse = pygame.mouse.get_pos()
       click = pygame.mouse.get_pressed()        
       #print(mouse)
        
       # Cerrar sesion        
       if 152 > mouse[0] > 100 and 60 > mouse[1] > 10:
          ventana.blit(cerrars, mouse)
          if click[0] == 1:
              variable_cerrarsesion = 1

       elif 970 > mouse[0] > 640 and 60 > mouse[1] > 15:
          ventana.blit(pantallaact, mouse)
        
       elif 70 > mouse[0] > 0 and 70 > mouse[1] > 0:
            ventana.blit(logouv1, mouse)
        
        
       # Cerrar sesión e ir a pantalla de autenticación              
       if variable_cerrarsesion == 1:
          loop_ppal=False
          loop_ppal_medicion=False
          loop_sec_medicion=False
          loop_sec=False  
          loop_control_cerrado=False
          pantalla_errores=False
          autenticacion=True

       
       pygame.display.update()
       pygame.display.flip()               
       ventana.fill(color_fondo)
       reloj.tick(fps) 

        
                                 
