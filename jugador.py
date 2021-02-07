import pygame

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
        if self.posimagen>= 6:
            self.posimagen=0
        if self.key[pygame.K_RIGHT]:
            self.imagenoso = self.listaSpritesOsoCaminando[self.posimagen]
            self.posimagen+=1

        else:
            if (self.key[pygame.K_LEFT]):
                 self.imagenoso = self.listaSpritesOsoCaminandov2[self.posimagen]
                 self.posimagen+=1
            else: self.imagenoso = self.imageninicial


        ventana.blit(self.imagenoso, (posicionix, posicioniy))



    def cambio(self, tiempo):

     if self.tiempocambio == tiempo:


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RIGHT or pygame.K_LEFT:
                    self.posimagen += 1
                    self.tiempocambio += 1



     if (self.posimagen > len(self.listaSpritesOsoCaminando)-1 or self.posimagen > len(self.listaSpritesOsoCaminandov2)-1):
                   self.posimagen = 0