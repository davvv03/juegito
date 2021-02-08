import pygame
from pygame.locals import *
import sys
import os
 
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
 
ANCHO = 1024
ALTO = 768
 
# pygame.NOFRAME sin margenes
ventana = pygame.display.set_mode((ANCHO, ALTO))
 
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 192, 0)
 
# Clases -----------------------------------------------------------------------
class Pared(pygame.sprite.Sprite):
    def __init__(self, x, y, largo, alto, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((largo, alto))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO/2
        self.rect.centery = ALTO/2
        self.velocidad = 0
    def update(self):
        ventana.blit(self.image, self.rect)
 
class Personaje(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.state_y = 'falling'
        self.jump_timer = 0
        self.falling_timer = 0
 
    def __str__(self):
        return ('Coordenada X: ' + str(self.rect.x) + ' Coordenada Y: ' + str(self.rect.y))
 
    def mover_x(self):
        self.rect.move_ip(self.velocidad_x, 0)
 
    def mover_y(self):
        self.rect.move_ip(0, self.velocidad_y)
 
    def mover(self):
        self.rect.move_ip(self.velocidad_x, self.velocidad_y)
 
    def colision(self, other):
        return self.rect.colliderect(other)
 
    def update(self):
        ventana.blit(self.image, self.rect)
 
class Enemigos(pygame.sprite.Sprite):
    pass
# ------------------------------------------------------------------------------
 
muro = Pared(0, 0, 800, 32, AZUL)
heroe = Personaje(100, 100)
 
 
 
def run():
    fps = pygame.time.Clock()
    salir = False
    heroe.velocidad_y = 4
    heroe.velocidad_x = 0
    gravedad = 8
    myfont = pygame.font.SysFont("monospace", 15)
 
    while not salir:
        for evento in pygame.event.get():
            # con raton: pygame.MOUSEBUTTONDOWN
            if evento.type == pygame.QUIT:
                salir = True
 
         # Movimiento del personaje
        tecla = pygame.key.get_pressed()
 
        if tecla[K_q]:
            break
 
        if tecla[K_LEFT] and not tecla[K_RIGHT]:
            heroe.velocidad_x = -4
        elif tecla[K_RIGHT] and not tecla[K_LEFT]:
            heroe.velocidad_x = 4
        else:
            heroe.velocidad_x = 0
        heroe.mover_x()
        if heroe.colision(muro):
            if heroe.velocidad_x > 0:
                heroe.rect.right = muro.rect.left
            if heroe.velocidad_x < 0:
                heroe.rect.left = muro.rect.right
 
        # Estado a velocidad
        if heroe.state_y == 'falling':
            heroe.velocidad_y = heroe.falling_timer * gravedad
            heroe.falling_timer += 0.15
        elif heroe.state_y == 'jumping':
            heroe.velocidad_y = (heroe.jump_timer / 15.0) * -gravedad
            heroe.jump_timer -= 1
        elif heroe.state_y == 'standing':
            heroe.velocidad_y = 0
            heroe.jump_timer = 30
            heroe.falling_timer = 0
 
        if tecla[K_UP]:
            if heroe.state_y == 'standing':
                heroe.state_y = 'jumping'
        else:
            if heroe.state_y == 'jumping':
                heroe.state_y = 'falling'
        if heroe.jump_timer <= 0:
            heroe.state_y = 'falling'
 
        heroe.mover_y()
        if heroe.colision(muro):
            if heroe.state_y == 'falling':
                heroe.rect.bottom = muro.rect.top
                heroe.state_y = 'standing'
            elif heroe.state_y == 'jumping':
                heroe.rect.top = muro.rect.bottom
        if heroe.state_y == 'standing':
            heroe.velocidad_y = 1
            heroe.mover_y()
            ground = heroe.rect.bottom > ALTO
            wall_colision = heroe.colision(muro)
            heroe.velocidad_y = -1
            heroe.mover_y()
            heroe.velocidad_y = 0
 
            if not wall_colision and not ground:
                heroe.state_y = 'falling'
 
        # Evita que salga por los extremos de la ventana
        if heroe.rect.left < 0:
            heroe.rect.left = 0
        elif heroe.rect.right > ANCHO:
            heroe.rect.right = ANCHO
        if heroe.rect.top < 0:
            heroe.rect.top = 0
        elif heroe.rect.bottom > ALTO:
            heroe.rect.bottom = ALTO
            heroe.state_y = 'standing'
 
        # Actulizacion y dibujo de pantalla
        ventana.fill(NEGRO)
        muro.update()
        heroe.update()
        # render text
        if heroe.state_y == 'jumping':
            label = myfont.render("%s %.03f" % (heroe.state_y, heroe.jump_timer), 1, (0,255,0))
        elif heroe.state_y == 'falling':
            label = myfont.render("%s %.03f" % (heroe.state_y, heroe.falling_timer), 1, (0,255,0))
        else:
            label = myfont.render("%s" % (heroe.state_y,), 1, (0,255,0))
        ventana.blit(label, (800, 100))
        pygame.display.flip()
        fps.tick(30)
run()
pygame.quit()
sys.exit()