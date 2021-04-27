import pygame
from random import randint

BLACK = (0, 0, 0)


# Class represents a ball and is a subclass of sprite
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call sprite constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    # Updates the ball's velocity
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # Bounce when a ball hits something
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
