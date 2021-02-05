import pygame
import sys
from pygame.locals import *
#UNO SOLITO
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
amarillo = (255, 255, 0)
morado = (153, 5, 182)

pantalla = pygame.display.set_mode((1280,720),RESIZABLE)

pygame.display.set_caption("ULTRA OWO")

fondo = pygame.image.load("imagenes/FondoFinal2.png")
pantalla.blit(fondo, (0, 0))


class Arbusto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagenA = pygame.image.load("sprites/arbusto64alfa.png")
        self.imagenB = pygame.image.load("sprites/arbusto64alfa.png")

        self.listaimagenes = [self.imagenA, self.imagenB]
        self.posimagen = 0
        self.imagenarbusto = self.listaimagenes[self.posimagen]
        self.rect = self.imagenarbusto.get_rect()
        self.tiempocambio = 1

    def mostrar(self, ventana):

        self.imagenarbusto = self.listaimagenes[self.posimagen]

        ventana.blit(self.imagenarbusto, (555, 459))

    def cambio(self, tiempo):



        if self.tiempocambio == tiempo:
            self.posimagen += 1
            self.tiempocambio += 1

            if self.posimagen > len(self.listaimagenes)-1:
                self.posimagen = 0


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Caminando1 = pygame.image.load("sprites/OsoCaminando1.png")
        self.Caminando2 = pygame.image.load("sprites/OsoCaminando2.png")
        self.Caminando3 = pygame.image.load("sprites/OsoCaminando3.png")
        self.Caminando4 = pygame.image.load("sprites/OsoCaminando4.png")
        self.Caminando5 = pygame.image.load("sprites/OsoCaminando5.png")
        self.Caminando6 = pygame.image.load("sprites/OsoCaminando6.png")
        self.Caminando1v2 = pygame.image.load("sprites/OsoCaminando1.2.png")
        self.Caminando2v2 = pygame.image.load("sprites/OsoCaminando2.1.png")
        self.Caminando3v2 = pygame.image.load("sprites/OsoCaminando3.1.png")
        self.Caminando4v2 = pygame.image.load("sprites/OsoCaminando4.1.png")
        self.Caminando5v2 = pygame.image.load("sprites/OsoCaminando5.1.png")
        self.Caminando6v2 = pygame.image.load("sprites/OsoCaminando6.1.png")

        self.listaSpritesOsoCaminando = [self.Caminando1, self.Caminando2, self.Caminando3, self.Caminando4,
                                         self.Caminando5, self.Caminando6]
        self.posimagen = 0
        self.imagenosocaminando = self.listaSpritesOsoCaminando[self.posimagen]
        self.rect = self.imagenosocaminando.get_rect()
        self.tiempocambio = 1

        self.posI = 0

        self.listaSpritesOsoCaminandov2 = [self.Caminando1v2, self.Caminando2v2, self.Caminando3v2, self.Caminando4v2,
                                           self.Caminando5v2, self.Caminando6v2]
        self.imagenosocaminandov2 = self.listaSpritesOsoCaminandov2[self.posimagen]

        self.imageninicial = self.Caminando1

    def oso(self, ventana, posicionix, posicioniy ):
        pygame.event.pump()
        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_RIGHT]:

            self.imagenoso = self.listaSpritesOsoCaminando[self.posimagen]

        else:
            if (self.key[pygame.K_LEFT]):

                 self.imagenoso = self.listaSpritesOsoCaminandov2[self.posimagen]

            else: self.imagenoso = self.imageninicial


        ventana.blit(self.imagenoso, (posicionix, posicioniy))





    def cambio(self, tiempo):

     if self.tiempocambio == tiempo:


      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT or pygame.K_LEFT:

            self.posimagen += 1
            self.tiempocambio += 1



     if (self.posimagen > len(self.listaSpritesOsoCaminando)-1 or self.posimagen > len(self.listaSpritesOsoCaminandov2)-1):
                   self.posimagen = 0





def MiJuego():

    pygame.init()

    jugadorPosX = 0
    jugadorPosY = 405
    arbusto1 = Arbusto()
    jugador1 = Jugador()
    reloj = pygame.time.Clock()
    posimagen = 0


    while True:

        reloj.tick(60)

        repeticion = 100
        repeticion2 = 100

        pygame.key.set_repeat(repeticion, repeticion2)

        tiempo = int(pygame.time.get_ticks() / 1000)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:

                    jugadorPosX += 10

                if event.key == pygame.K_LEFT:

                    jugadorPosX -=10

            if event.type == pygame.KEYDOWN:


                if event.key == pygame.K_SPACE:

                    jugadorPosY -= 40

                    if (jugadorPosY < 405 - 40):

                        jugadorPosY = 405 - 40

            if jugadorPosY < 405 :
                jugadorPosY += 10




        pantalla.blit(fondo, (0, 0))
        arbusto1.mostrar(pantalla)
        arbusto1.cambio(tiempo)
        jugador1.oso(pantalla , jugadorPosX , jugadorPosY)
        jugador1.cambio(tiempo)
        pygame.display.update()

MiJuego()
