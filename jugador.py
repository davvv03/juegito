import pygame


class Jugador(pygame.sprite.Sprite):

    #awqa
    def __init__(self , jugadorPosY , desp , jugadorPosX):
        super().__init__() 
        self.jugadorPosY = jugadorPosY
        self.desp = desp
        self.jugadorPosX = jugadorPosX
        self.statey = "falling"
        self.jumptimer = 0
        self.fallingTimer = 0
        self.velocidady = 0
        self.QUIETA = pygame.image.load("sprites/SpriteMujer1/Quieta.png")

        self.CD1 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD1.png")
        self.CD2 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD2.png")
        self.CD3 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD3.png")
        self.CD4 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD4.png")
        self.CD5 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD5.png")
        self.CD6 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD6.png")
        self.CD7 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD7.png")
        self.CD8 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD8.png")
        self.CD9 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD9.png")
        self.CD10 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD10.png")
        self.CD11 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD11.png")
        self.CD12 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD12.png")
        self.CD13 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD11.png")
        self.CD14 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD10.png")
        self.CD15 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD9.png")
        self.CD16 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD8.png")
        self.CD17 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD7.png")
        self.CD18 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD6.png")
        self.CD19 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD5.png")
        self.CD20 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD4.png")
        self.CD21 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD3.png")
        self.CD22 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD2.png")
        self.CD23 = pygame.image.load("sprites/SpriteMujer1/CaminandoDerecha/CD1.png")
        
        

        self.CI1 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI1.png")
        self.CI2 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI2.png")
        self.CI3 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI3.png")
        self.CI4 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI4.png")
        self.CI5 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI5.png")
        self.CI6 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI6.png")
        self.CI7 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI7.png")
        self.CI8 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI8.png")
        self.CI9 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI9.png")
        self.CI10 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI10.png")
        self.CI11 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI11.png")
        self.CI12 = pygame.image.load("sprites/SpriteMujer1/CaminandoIzquierda/CI12.png")

        self.SD1=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD1.png")
        self.SD2=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD2.png")
        self.SD3=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD3.png")
        self.SD4=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD4.png")
        self.SD5=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD5.png")
        self.SD6=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD6.png")
        self.SD7=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD7.png")
        self.SD8=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD8.png")
        self.SD9=pygame.image.load("sprites/SpriteMujer1/SaltandoDerecha/SD9.png")
        self.rect = self.QUIETA.get_rect()
        self.listaSpritesOsoCaminando = [self.CD1,self.CD2,self.CD3,self.CD4,self.CD5,self.CD6,self.CD7,self.CD8,self.CD9,self.CD10,self.CD11,self.CD12]
        self.posimagen = 0
        self.imagenosocaminando = self.listaSpritesOsoCaminando[self.posimagen]
        self.rect = self.imagenosocaminando.get_rect()
        self.tiempocambio = 1

        self.posI = 0

        self.listaSpritesOsoCaminandov2 = [self.CI1,self.CI2,self.CI3,self.CI4,self.CI5,self.CI6,self.CI7,self.CI8,self.CI9,self.CI10,self.CI11,self.CI12]
        self.imagenosocaminandov2 = self.listaSpritesOsoCaminandov2[self.posimagen]
        self.listaSpritesOsoSaltando=[self.SD2]
        self.imageninicial = self.QUIETA

    def oso(self, ventana, posicionix, posicioniy ):
        pygame.event.pump()
        self.key = pygame.key.get_pressed()
   
        if self.key[pygame.K_RIGHT] and not(self.key[pygame.K_LEFT]):
            self.imagenoso = self.listaSpritesOsoCaminando[self.posimagen]
        if (self.key[pygame.K_LEFT])and not self.key[pygame.K_RIGHT]:
            self.imagenoso = self.listaSpritesOsoCaminandov2[self.posimagen]
        if(self.key[pygame.K_SPACE]):
            self.imagenoso = self.SD1
            if self.jugadorPosY != 385:
                self.imagenoso = self.SD2
        if not(self.key[pygame.K_RIGHT]) and not self.key[pygame.K_LEFT] and not self.key[pygame.K_SPACE]:
            self.imagenoso = self.imageninicial


        ventana.blit(self.imagenoso, (posicionix, posicioniy))



    def cambio(self, tiempo):


      repeticion = 111
      repeticion2 = 111

      pygame.key.set_repeat(repeticion, repeticion2)
     
      #if self.tiempocambio == tiempo:

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            
            exit()

          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and event.key != pygame.K_LEFT:

                self.posimagen += 1
                self.tiempocambio += 1

            if event.key == pygame.K_LEFT and event.key != pygame.K_RIGHT:
                    self.posimagen += 1
                    self.tiempocambio += 1
            if event.key == pygame.K_SPACE:
                     self.posimagen += 1
                     self.tiempocambio += 1



             
            if (self.posimagen > len(self.listaSpritesOsoCaminando)-1) or (self.posimagen > len(self.listaSpritesOsoCaminandov2)-1):
                
                self.posimagen = 1
    def movX(self,direccion):
       if direccion=='D': 
        self.jugadorPosX = self.jugadorPosX + 2
        return self.jugadorPosX
       elif direccion=='I':
            self.jugadorPosX = self.jugadorPosX - 2
            return self.jugadorPosX
    def colision(self, other):
        return self.rect.colliderect(other)




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
        #pygame.time.delay(30)
        pantalla.blit(self.actual,(0,0))
        if self.pos<7:
            self.pos+=1
        else:self.pos=0

class piso(pygame.sprite.Sprite):
    def __init__(self, x, y, largo, alto, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((largo, alto))
        self.rect = self.image.get_rect()
        self.rect.top=y
        self.rect.bottom=y+alto
        self.rect.right=largo
        self.rect.left=x
    def update(self,ventana):
        ventana.blit(self.image, self.rect)
 