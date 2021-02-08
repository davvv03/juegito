import pygame,sys
from pygame.locals import*
from jugador import*
#Estos colores funcionan para dibujar en pantalla simplemente se crean las variables 
#para usarlos con mayor facilidad 

blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
amarillo = (255, 255, 0)
morado = (153, 5, 182)


#Se determina el tamaño que va a tomar la pantalla ademas de su tipo esta es su estructura
#set_mode (tamaño = (0, 0), banderas = 0, profundidad = 0, pantalla = 0, vsync = 0)
Ancho=1350
Alto=700
pantalla = pygame.display.set_mode((Ancho,Alto))


#Nombre de la ventanass
icono=pygame.image.load("imagenes/IconFinal4.png")
pygame.display.set_icon(icono)
pygame.display.set_caption("ULTRA OWO")


#Se carga la imagen fondo y luego con .blit se establece la coordenada en la que se va a dibujar
#estructura: blit (fuente, destino, área = Ninguno, banderas_especiales = 0)
fondo = pygame.image.load("imagenes/FondoFinal2.png")
pantalla.blit(fondo, (0,0))


#Se crea la clase arbusto y hereda de Sprite para que pueda usar los metodos incluidos en dicha clase
#cualquier sprite debe heredar de esa clase
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
                self.posimagen = 1




#Bucle General del Juego
def MiJuego():
    #Inicializacion de Pygame
    pygame.init()

    jugadorPosX = 0
    jugadorPosY = 405
    arbusto1 = Arbusto()
    jugador1 = Jugador()
    reloj = pygame.time.Clock()
    posimagen = 0
    IsJump = False
    jumpcount = 10                                        



    while True:

        reloj.tick(45)

        repeticion = 100
        repeticion2 = 100

        pygame.key.set_repeat(repeticion, repeticion2)

        tiempo = int(pygame.time.get_ticks() * 1000)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.event.pump()
        Key = pygame.key.get_pressed()

        if Key[pygame.K_RIGHT]:
            jugadorPosX += 2

        else: 
            if Key[pygame.K_LEFT]:
                jugadorPosX -= 2
         

        if not  (IsJump):

            if Key[pygame.K_SPACE]:

                IsJump = True 

        else:
            if jumpcount >= -10:
             jugadorPosY -= (jumpcount * abs(jumpcount))*0.5
             jumpcount -= 1
            else:
                jumpcount = 10
                IsJump = False



        pantalla.blit(fondo, (0, 0))
        arbusto1.mostrar(pantalla)
        arbusto1.cambio(tiempo)
        jugador1.oso(pantalla , jugadorPosX , jugadorPosY)
        jugador1.cambio(tiempo)
        pygame.display.update()

MiJuego()