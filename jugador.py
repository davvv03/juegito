import pygame

class Jugador(pygame.sprite.Sprite):

    #awqa
    def __init__(self):
        super().__init__()
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
        


        self.Caminando1v2 = pygame.image.load("sprites/OsoCaminando1.2.png")
        self.Caminando2v2 = pygame.image.load("sprites/OsoCaminando2.1.png")
        self.Caminando3v2 = pygame.image.load("sprites/OsoCaminando3.1.png")
        self.Caminando4v2 = pygame.image.load("sprites/OsoCaminando4.1.png")
        self.Caminando5v2 = pygame.image.load("sprites/OsoCaminando5.1.png")
        self.Caminando6v2 = pygame.image.load("sprites/OsoCaminando6.1.png")

        self.listaSpritesOsoCaminando = [self.CD1,self.CD2,self.CD3,self.CD4,self.CD5,self.CD6,self.CD7,self.CD8,self.CD9,self.CD10,self.CD11,self.CD12]
        self.posimagen = 0
        self.imagenosocaminando = self.listaSpritesOsoCaminando[self.posimagen]
        self.rect = self.imagenosocaminando.get_rect()
        self.tiempocambio = 1

        self.posI = 0

        self.listaSpritesOsoCaminandov2 = [self.Caminando1v2, self.Caminando2v2, self.Caminando3v2, self.Caminando4v2,
                                           self.Caminando5v2, self.Caminando6v2]
        self.imagenosocaminandov2 = self.listaSpritesOsoCaminandov2[self.posimagen]

        self.imageninicial = self.QUIETA

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


      repeticion = 100
      repeticion2 = 100

      pygame.key.set_repeat(repeticion, repeticion2)
     

      #if self.tiempocambio == tiempo:

     
    
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            
            exit()

          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                self.posimagen += 1
                self.tiempocambio += 1

            else:  
                if event.key == pygame.K_LEFT:

                    self.posimagen += 1
                    self.tiempocambio += 1

             
            if (self.posimagen > len(self.listaSpritesOsoCaminando)-1) or (self.posimagen > len(self.listaSpritesOsoCaminandov2)-1):
                
                self.posimagen = 0