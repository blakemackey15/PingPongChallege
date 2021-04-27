import pygame


# Class that represents a speed up power up in the game
# Speed up increases the movement speed of the paddle to 13 pixels
class SpeedUp(pygame.sprite.Sprite):

    def __init__(self, color, width, height, for_paddle):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.for_paddle = for_paddle


# Class that represents a slow down power up in the game
# Slow down decreases the movement speed of the paddle to 4 pixels
class SlowDown(pygame.sprite.Sprite):

    def __init__(self, color, width, height, for_paddle):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.for_paddle = for_paddle
