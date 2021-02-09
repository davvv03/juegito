import pygame

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.F1 = pygame.image.load("imagenes/fondo/Frame1.png")
        self.F2 = pygame.image.load("imagenes/fondo/Frame2.png")
        self.F3 = pygame.image.load("imagenes/fondo/Frame3.png")
        self.F4 = pygame.image.load("imagenes/fondo/Frame4.png")
        self.F5 = pygame.image.load("imagenes/fondo/Frame5.png")
        self.F6 = pygame.image.load("imagenes/fondo/Frame6.png")
        self.F7 = pygame.image.load("imagenes/fondo/Frame7.png")
        self.F8 = pygame.image.load("imagenes/fondo/Frame8.png")
        self.Listafondo=[self.F1,self.F2,self.F3,self.F4,self.F5,self.F6,self.F7,self.F8]
        self.pos=0
        self.actual=self.F1
        
    def update(self,pantalla):
        self.actual=self.Listafondo[self.pos]
        pygame.time.delay(90)
       
        pantalla.blit(self.actual,(0,0))
        if self.pos<7:
            self.pos+=1
        else:self.pos=0
