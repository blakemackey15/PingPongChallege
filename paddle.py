import pygame
BLACK = (0, 0, 0)


# Class represents a paddle and is a subclass of sprite
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    # controls the paddle up
    def move_up(self, pixels):
        self.rect.y -= pixels
        # checks that you don't go off screen
        if self.rect.y < 0:
            self.rect.y = 0

    # controls the paddle down
    def move_down(self, pixels):
        self.rect.y += pixels
        # checks that you don't go off screen
        if self.rect.y > 400:
            self.rect.y = 400
