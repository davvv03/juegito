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
fondo = Fondo()
pantalla.blit(fondo.F1, (0,0))


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
    x=0
    jugadorPosX = 0
    jugadorPosY = 528
    arbusto1 = Arbusto()

    reloj = pygame.time.Clock()
    posimagen = 0
    gravedad = 8
    
    jumpcount = 10 
    desp = 2        
    fuente1 = pygame.font.SysFont("Arial" , 20 )    
    aux = 1  
    global IsJump 
    IsJump = False
    jugador1 = Jugador(jugadorPosY , desp  , jugadorPosX)



    while True:

        reloj.tick(45)

        repeticion = 100
        repeticion2 = 100

        pygame.key.set_repeat(repeticion, repeticion2)

        tiempo = int(pygame.time.get_ticks() / 1000)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.event.pump()
        Key = pygame.key.get_pressed()

        if Key[pygame.K_RIGHT] and not Key[pygame.K_LEFT]:
            jugadorPosX= jugador1.movX('D')

        else: 
            if Key[pygame.K_LEFT]:
                jugadorPosX = jugador1.movX('I')


        if jugador1.statey == "falling":

            jugador1.velocidady = jugador1.fallingTimer*gravedad
            jugador1.fallingTimer += 0.15

        elif jugador1.statey == "jumping":

            jugador1.velocidady = (jugador1.jump_timer / 15.0) * -gravedad
            jugador1.jumptimer -= 1

        elif jugador1.statey == "standing":

            jugador1.velocidad_y = 1
        
            jugador1.velocidady = -1
           
            jugador1.velocidady = 0
         

        if not  (IsJump):

            if Key[pygame.K_SPACE]:
                
                IsJump = True 
                desp = 7

        '''else:
            if jumpcount >= -10:
             jugadorPosY -= ((jumpcount * abs(jumpcount))*0.5)
             jumpcount -= 1
            else:
                jumpcount = 10
                IsJump = False
                desp = 2'''


        fondo.update(pantalla)
        #pantalla.blit(fondo.F2, (0, 0))
        arbusto1.mostrar(pantalla)
        arbusto1.cambio(tiempo)
        jugador1.oso(pantalla , jugadorPosX , jugadorPosY)
        jugador1.cambio(tiempo)
        segundos = str(tiempo)
        altura = str(jugadorPosY)
        contador = fuente1.render(segundos  , 0 , (blanco))
        y = fuente1.render(altura , 0 , (blanco))
        pantalla.blit(contador , (0 , 0))
      
        pantalla.blit(y , (35  , 0))
          

        pygame.display.update()

MiJuego()