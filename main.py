import pygame

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.image = pygame.image.load("square.png")
        self.rect = self.image.get_rect()
        self.rect.centery = ALTO / 2


    def move(self):
        new_x = self.rect.left + ((ANCHO-self.rect.width)/4)
        if new_x > ANCHO:
            new_x = 0
        self.rect.left = new_x



def game():
    pygame.init()
    pygame.key.set_repeat(1, 25)

    all_sprites = pygame.sprite.Group()

    square = Square()
    all_sprites.add(square)

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Game")
    fps_clock = pygame.time.Clock()

    # Creamos nuestro timer, que lanzará el evento cada segundo (1000 ms)
    pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # comprobamos si el timer ha lanzado el evento
            ## En caso afirmativo llamamos al método move del sprite.
            elif event.type == pygame.USEREVENT + 1:
                square.move()

        dt = fps_clock.tick(FPS) / 1000.0
        all_sprites.update(dt)
        ventana.fill(NEGRO)
        all_sprites.draw(ventana)
        pygame.display.flip()


if __name__ == "__main__":
    game()