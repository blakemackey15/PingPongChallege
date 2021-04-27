import pygame

BLACK = (0, 0, 0)


# Class represents an obstacle block
class Block(pygame.sprite.Sprite):

    def __init__(self, color):
        # Call the Sprite constructor
        super().__init__()

        self.image = pygame.Surface([10, 70])
        self.image.fill(color)

        self.rect = self.image.get_rect()
