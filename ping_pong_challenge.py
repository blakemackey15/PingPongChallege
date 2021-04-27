# Blake Mackey
# Version Beta 1.0

# This game is a two player competitive game of pong. Use the up and down arrow
# to control the right paddle and the W and S keys to control the left paddle.
# The person who has the highest score when the timer (one minute) has run out
# wins. There are two power ups: speed up paddle, and slow down paddle. Speed
# up paddle power ups are represented by green blocks, while slow down power
# ups are represented by blue blocks.

# In this version, the second level has been implemented and the power ups have
# also been implemented. Furthermore, I redid a lot of my code from the
# previous version, since it became unorganized and hard to follow. As is, the
# obstacles linger for the duration of the game, and appear after 30 seconds.
# In addition, a power up will be given out at random at the 50 second mark.
# This allows for a last minute change of pace, and the power up will last
# until the game is over.

# Royalty free 8-bit music by sawsquarenoise. Sound effects downloaded from
# zapsplat.com

# Imports
import pygame
from paddle import Paddle
from ball import Ball
from block import Block
from power_up import SpeedUp
from power_up import SlowDown
import random

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 600
HEIGHT = 400

created_flag = True

# Create screen/game variables
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong Challenge")

# Create paddles
player1 = Paddle(WHITE, 10, 100)
player1.rect.x = 20
player1.rect.y = 200

player2 = Paddle(WHITE, 10, 100)
player2.rect.x = 670
player2.rect.y = 200

# Create ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# Create power ups
speed_upP1 = SpeedUp(GREEN, 10, 10, 1)
speed_upP1.rect.x = 20
speed_upP1.rect.y = 200

slow_downP1 = SlowDown(BLUE, 10, 10, 1)
slow_downP1.rect.x = 20
slow_downP1.rect.y = 200

speed_upP2 = SpeedUp(GREEN, 10, 10, 2)
speed_upP2.rect.x = 670
speed_upP2.rect.y = 200

slow_downP2 = SlowDown(BLUE, 10, 10, 2)
slow_downP2.rect.x = 670
slow_downP2.rect.y = 200

# Create lists
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
power_up_list = pygame.sprite.Group()

# Add sprites to lists
all_sprites_list.add(player1)
all_sprites_list.add(player2)
all_sprites_list.add(ball)
power_up_list.add(speed_upP1)
power_up_list.add(slow_downP1)
power_up_list.add(speed_upP2)
power_up_list.add(slow_downP2)

# Create obstacles
for i in range(10):
    block = Block(RED)
    block.rect.x = random.randrange(500)
    block.rect.y = random.randrange(700)
    block_list.add(block)

# Create movement pixels
p1_pixels = 8
p2_pixels = 8

# Initialize power up variables
p1_power_up = 0
p2_power_up = 0

carry_on = True

clock = pygame.time.Clock()

# Initialise player scores
score1 = 0
score2 = 0


# Renders text for game intro/outro screens
def text_objects(start_text, start_font):
    text_surface = start_font.render(start_text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()


# Creates game intro screen
def game_intro():
    intro = True
    while intro:
        for start_event in pygame.event.get():
            if start_event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if start_event.type == pygame.KEYDOWN:
                intro = False

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, WHITE, [200, 10, 10, 10], 0)
        pygame.draw.rect(screen, WHITE, [100, 10, 10, 70], 0)
        pygame.draw.rect(screen, WHITE, [590, 70, 10, 70], 0)
        pygame.draw.rect(screen, GREEN, [50, 460, 10, 10], 0)
        pygame.draw.rect(screen, BLUE, [100, 460, 10, 10], 0)
        pygame.draw.rect(screen, RED, [600, 400, 10, 70], 0)

        power_up_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surf4, text_rect4 = text_objects("Get Power Ups!", power_up_text)
        text_rect4.center = (100, 375)
        screen.blit(text_surf4, text_rect4)

        obstacle_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surf5, text_rect5 = text_objects("Avoid the Obstacles!",
                                              obstacle_text)
        text_rect5.center = (575, 375)
        screen.blit(text_surf5, text_rect5)

        start_text = pygame.font.Font('freesansbold.ttf', 40)
        text_surf, text_rect = text_objects("Ping Pong Challenge", start_text)
        text_rect.center = ((WIDTH / 2 + 50), (HEIGHT / 2))
        screen.blit(text_surf, text_rect)

        name = pygame.font.Font('freesansbold.ttf', 20)
        text_surf3, text_rect3 = text_objects("Player 1 "
                                              "Controls: W - Up"
                                              ", S - Down", name)
        text_rect3.center = ((WIDTH / 2 + 50), (HEIGHT / 2 + 40))
        screen.blit(text_surf3, text_rect3)

        second_name = pygame.font.Font('freesansbold.ttf', 20)
        text_surf4, text_rect4 = text_objects("Player 2 "
                                              "Controls: Up Key - "
                                              "Up, Down Key - Down",
                                              second_name)
        text_rect4.center = ((WIDTH / 2 + 50), (HEIGHT / 2 + 70))
        screen.blit(text_surf4, text_rect4)

        next_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surf2, text_rect2 = text_objects("Press any key to "
                                              "continue", next_text)
        text_rect2.center = ((WIDTH / 2 + 50), (HEIGHT / 2 + 140))
        screen.blit(text_surf2, text_rect2)
        pygame.display.update()
        clock.tick(15)


# Creates game over screen and displays who won
def end_game(winner_string):
    end = True
    while end:
        for end_event in pygame.event.get():
            if end_event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if end_event.type == pygame.KEYDOWN:
                end = False

        screen.fill((0, 0, 0))
        end_text = pygame.font.Font('freesansbold.ttf', 40)
        text_surf, text_rect = text_objects("Game Over", end_text)
        text_rect.center = ((WIDTH / 2 + 50), (HEIGHT / 2))
        screen.blit(text_surf, text_rect)

        next_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surf2, text_rect2 = text_objects(winner_string, next_text)
        text_rect2.center = ((WIDTH / 2 + 50), (HEIGHT / 2 + 40))
        screen.blit(text_surf2, text_rect2)
        pygame.display.update()
        clock.tick(15)


game_intro()

# Set music
pygame.mixer.music.load('ping pong challenge music.mp3')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

# Start timer
start_tick = pygame.time.get_ticks()


# -------- Main Program Loop -----------
while carry_on:
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carry_on = False

    # Move Paddles: Player 1 (W: Up, S: Down) Player 2
    # (Up Arrow: Up, Down Arrow: Down)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move_up(p1_pixels)
    if keys[pygame.K_s]:
        player1.move_down(p1_pixels)
    if keys[pygame.K_UP]:
        player2.move_up(p2_pixels)
    if keys[pygame.K_DOWN]:
        player2.move_down(p2_pixels)

    # --- Game logic start
    seconds = (pygame.time.get_ticks() - start_tick) / 1000

    # Check if time is up, and declare winner if it is
    if seconds >= 60:
        if score1 > score2:
            winner = "Left Player Wins!"
            carry_on = False
            end_game(winner)
        elif score2 > score1:
            winner = "Right Player Wins!"
            carry_on = False
            end_game(winner)

    # Detect collision between the ball and obstacles
    if seconds > 30:
        for block in block_list:
            all_sprites_list.add(block)

        if pygame.sprite.spritecollide(ball, block_list, False):
            ball.bounce()
            hit = pygame.mixer.Sound('hit_paddle.wav')
            hit.set_volume(1)
            hit.play()

    if seconds > 50:
        # If random number = 1: speed up. If random number = 2: slow down
        while p1_power_up == 0 and p2_power_up == 0:
            p1_power_up = random.randrange(1, 3)
            p2_power_up = random.randrange(1, 3)

        while created_flag:
            if p1_power_up == 1 and p2_power_up == 1:
                all_sprites_list.add(speed_upP1)
                all_sprites_list.add(speed_upP2)
                created_flag = False

            if p1_power_up == 1 and p2_power_up == 2:
                all_sprites_list.add(speed_upP1)
                all_sprites_list.add(slow_downP2)
                created_flag = False

            if p1_power_up == 2 and p2_power_up == 1:
                all_sprites_list.add(slow_downP1)
                all_sprites_list.add(speed_upP2)
                created_flag = False

            if p1_power_up == 2 and p2_power_up == 2:
                all_sprites_list.add(slow_downP1)
                all_sprites_list.add(slow_downP2)
                created_flag = False

        # Power up collision detection
        if pygame.sprite.spritecollide(player1, power_up_list, True):

            # Speed up power up P1
            if p1_power_up == 1:
                p1_pixels = 13

            # Slow down power up P1
            if p1_power_up == 2:
                p1_pixels = 4

        if pygame.sprite.spritecollide(player2, power_up_list, True):

            # Speed up power up P2
            if p2_power_up == 1:
                p2_pixels = 13

            # Slow down power up P2
            if p2_power_up == 2:
                p2_pixels = 4

    all_sprites_list.update()

    # Check if the ball has hit any of the walls
    if ball.rect.x >= 690:
        score1 += 1
        ball.velocity[0] = -ball.velocity[0]
        goal = pygame.mixer.Sound('score.wav')
        goal.set_volume(1)
        goal.play()

    if ball.rect.x <= 0:
        score2 += 1
        ball.velocity[0] = -ball.velocity[0]
        goal = pygame.mixer.Sound('score.wav')
        goal.set_volume(1)
        goal.play()

    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
        hit = pygame.mixer.Sound('hit_paddle.wav')
        hit.set_volume(1)
        hit.play()

    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
        hit = pygame.mixer.Sound('hit_paddle.wav')
        hit.set_volume(1)
        hit.play()

    # Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, player1) or \
            pygame.sprite.collide_mask(ball, player2):
        ball.bounce()
        hit = pygame.mixer.Sound('hit_paddle.wav')
        hit.set_volume(1)
        hit.play()

    # --- Game logic end
    # --- Drawing start

    screen.fill(BLACK)

    all_sprites_list.draw(screen)

    # Display timer
    time = pygame.font.SysFont("Arial", 40)
    cur_time = time.render(str(seconds), True, YELLOW)
    screen.blit(cur_time, (310, 10))

    # Display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(score1), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(score2), 1, WHITE)
    screen.blit(text, (420, 10))

    # --- Drawing end
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
