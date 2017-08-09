#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

global k
k = 0.0000401

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

#clase de botones
class Button_1():    

    def __init__(self, position, size):  
        global cambio, bfallos, bfallos2         
        bfallos2 = pygame.image.load('bfallos2.png')
        bfallos = pygame.image.load('bfallos.png')
        
        # crear imagen de boton
        cambio = pygame.image.load('bfallos.png')   
        #Dibujar botón
        cambio.blit(bfallos,(100,100))
        # Obtener tamaño y posicion de imagen
        self._rect1 = pygame.Rect(position, size)

    def draw1(self, screen):
        global cambio, bfallos, bfallos2
        # Dibujar imagenes seleccionadas
        screen.blit(cambio, self._rect1)
        screen.blit(bfallos, self._rect1)
        
    def draw2(self,screen):    
        screen.blit(bfallos2, self._rect1)
    
    def event_handler0(self, event):
        global k
        # Hacer cambios al botón cuando se hace click
        if event.type == pygame.MOUSEBUTTONDOWN: # Se hizo click 
            if  self._rect1.collidepoint(event.pos):# El mouse está sobre el botón
                if event.button == 1: # is left button clicked
                    #self._index = (self._index+1) % 3 # Cambiar imagen
                    k = k+0.001   
                    print(event, k)       
        
    def event_handler1(self, event):
        global loop_ppal, loop_sec
        # Hacer cambios al botón cuando se hace click
        if event.type == pygame.MOUSEBUTTONDOWN: # Se hizo click 
            if  self._rect1.collidepoint(event.pos):# El mouse está sobre el botón
                if event.button == 1: # is left button clicked
                   loop_ppal=False
                   loop_sec=True   
    
    def event_handler2(self, event):
        global loop_ppal, loop_sec
        # Hacer cambios al botón cuando se hace click
        if event.type == pygame.MOUSEBUTTONDOWN: # Se hizo click 
            if  self._rect1.collidepoint(event.pos):# El mouse está sobre el botón
                if event.button == 1: # is left button clicked
                   loop_ppal=True
                   loop_sec=False
                   time.sleep( 0.5 )  
                   
    def event_handler3(self, event):
        # Hacer cambios al botón cuando se hace click
        if event.type == pygame.MOUSEBUTTONDOWN: # Se hizo click 
            if  self._rect1.collidepoint(event.pos):# El mouse está sobre el botón
                if event.button == 1: # is left button clicked
                    button4.draw2(ventana)                                              
#Final buttons class 

