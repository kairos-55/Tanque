#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, math
import numpy as np
from matplotlib import pyplot as plt
from pygame.locals import *
from decimal import *
from tkinter import *

pygame.init()
# Inicializar valores
black=(0,0,0)
dimension_ventana = (1024,720)
coordenada_equilibro_masa = 398
coordenada_tanque = (240,101)
coordenada_logo = (0,0)
coordenada_banersup = (98,0)
coordenada_titulotanque = (640,30)
coordenada_banerinf = (0,620)
color_fondo = (225,225,225)
fps = 60
posicion_incial = 198
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
x = 262 #Valor inicial (nivel mínimo del tanque)
hv = np.linspace(h0,hf,n)
h = np.zeros([n])

#Definir propiedades ventana principal
ventana = pygame.display.set_mode(dimension_ventana)
ventana = Tk()
pygame.display.set_caption("Tanque")
#ventana.fill(color_fondo)
reloj = pygame.time.Clock()
diceRoll = 0
myFont = pygame.font.SysFont("Times New Roman", 18)

#cargar imagenes 
tanque = pygame.image.load('tanque3.png')
masarosa = pygame.image.load('masa2.png')
logo = pygame.image.load('logoUV.png')
banersup = pygame.image.load('1.png')
titulotanque = pygame.image.load('titulo_tanque.png')
banerinf = pygame.image.load('3.png') 


#clase de botones
class Button():    

    def __init__(self, position, size):
       
    
        off = pygame.image.load('off.png')
        voltaje = pygame.image.load('voltaje.png') 
        corriente = pygame.image.load('corriente.png')
        resistencia = pygame.image.load('resistencia.png')

        # crear imagenes de botones
        self._images = [
            pygame.image.load('off.png'),    
            pygame.image.load('voltaje.png'),    
            pygame.image.load('corriente.png'), 
            pygame.image.load('resistencia.png'),    
        ]

        self._images[0].blit(off,(317,291))
        self._images[1].blit(voltaje,(317,291))
        self._images[2].blit(corriente,(317,291))
        self._images[3].blit(resistencia,(317,291))
        
        # Obtener tamaño y posicion de imagen
        self._rect = pygame.Rect(position, size)

        # seleccionar primera imagen
        self._index = 0

    def draw(self, screen):

        # Dibujar imagenes seleccionadas
        screen.blit(self._images[0], self._rect)
        screen.blit(self._images[1], self._rect)
        screen.blit(self._images[2], self._rect)
        screen.blit(self._images[3], self._rect)
        
    def event_handler(self, event):
        # Hacer cambios al botón cuando se hace click
        if event.type == pygame.MOUSEBUTTONDOWN: # Se hizo click 
            if  self._rect.collidepoint(event.pos):# El mouse está sobre el botón
                if event.button == 1: # is left button clicked
                    self._index = (self._index+1) % 4 # Cambiar imagen    
                    print self._index
                    time.sleep( 0.5 )                
#Final buttons class 




def leerUsuario():
    text=TextEntry.get()
    password=TextEntry2.get()
    text=text.upper()
    
    if text == "Docente" or "docente" and password == "controluv":
       usuario_docente()
    else:
        lbl2.config(text="Usuario o contraseña incorrectos") 


lbl = Label(ventana, text="Ingresar Usuario")
lbl.pack()
TextEntry=Entry(ventana,bd=5)  
TextEntry.pack()       

lbl3 = Label(ventana, text="Ingresar Contraseña")
lbl3.pack()
TextEntry2=Entry(ventana,bd=5)  
TextEntry2.pack()

button=Button(ventana,text="Submit",command=leerUsuario)
button.pack()
lbl2 = Label(ventana,text="")
lbl2.pack()


def tanque():
    ventana.blit(tanque, coordenada_tanque)
    ventana.blit(agua, (coordenada_equilibro_masa+1, 240+ int(h[i]))) 

def adicionales():
    ventana.blit(logo, coordenada_logo)
    ventana.blit(banersup, coordenada_banersup)
    ventana.blit(titulotanque, coordenada_titulotanque)
    ventana.blit(banerinf, coordenada_banerinf)

def ecuacion_nivel():
    for i in range(1,n):
         h[i] = h[i-1] + delta*((hv[i] - k*np.sqrt(h[i-1]))/at)
    
    for i in range(n):   
       print(hv[i],h[i]) 
       
def button(msg,x1,y,w,h2,ic,ac,action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x1 and y+h > mouse[1] > y:
        pygame.draw.rect(ventana, ac, (x1,y,w,h))


def usuario_docente():   
     
    lbl2.config(text="Bienvenido")     
    
def usuario_estudiante():       
     
   inicio = True          
     
   while inicio:
     
     for evento in pygame.event.get():
         if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    
     pygame.draw.rect(ventana, (255, 0, 0), (750, 650, 100, 100))
    
             
     if evento.type == KEYUP:
            if evento.key == K_q:
              if x>15: 
                x=x-1 
                plt.plot(hv,h,'x')
                plt.xlabel("Value of qin")
                plt.ylabel("value of h")  
                plt.title("Solucion aproximada por metodo de euler")
                plt.show()
            
              
            elif evento.key == K_w:           
                 k = k+0.001 
                
            
            elif evento.key == K_e:           
                 k = k-0.001 
                      

     pygame.display.update()
     pygame.display.flip()
     ventana.fill(color_fondo)
     reloj.tick(fps) 