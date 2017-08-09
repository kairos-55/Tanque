import pygame
 
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
         else:
            pass

   def display_box(self, screen, message):
      fontobject = pygame.font.Font(None, 18)
      pygame.draw.rect(screen, self.white,
         ((screen.get_width() / 2) - 102, (screen.get_height() / 2) - 15, 204,24)) #if border add 1 for transp
      
      #pygame.draw.rect(screen, self.white,
         #((screen.get_width() / 2) - 102, (screen.get_height() / 2) + 10, 204,24)) #if border add 1 for transp
      
      if len(message) != 0:
         screen.blit(fontobject.render(message, 1 , self.black),
            ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
      
      #if len(message) != 0:
         #screen.blit(fontobject.render(message, 1 , self.black),
            #((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 8))
      pygame.display.update()
      
   def ask(self, screen, question):
      current_string = []
      self.display_box(screen, question + ': ' + ''.join(current_string))
      while True:
         inkey = self.get_key()
         if inkey == pygame.K_BACKSPACE:
            current_string = current_string[0:-1]
         elif inkey == pygame.K_RETURN:
            break
         else:
            current_string.append(chr(inkey))
         self.display_box(screen, question + ': ' + ''.join(current_string))
      return ''.join(current_string)
# Fin digitar usuario y contraseña
      
pygame.quit()