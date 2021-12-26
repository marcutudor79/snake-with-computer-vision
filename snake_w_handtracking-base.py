# Example for using CvHand class:

import hand_tracking as ht
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Snake Game stolen from the internet')

game_over = False

x1 = 640
y1 = 360

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

# Initialize CvHand class and dynamic fps
my_hand = ht.CvHand()
# If using phone as Camera set to True (60 fps camera required for optimal performance)
my_hand.flip = False
# Initialize optimal_fps, irrelevant value
optimal_fps = 60

while not game_over:

    hand_side = my_hand.current_hand_side()

    if hand_side == 'a':
        x1_change = -5
        y1_change = 0
    elif hand_side == 'd':
        x1_change = 5
        y1_change = 0
    elif hand_side == 'w':
        y1_change = -5
        x1_change = 0
    elif hand_side == 's':
        y1_change = 5
        x1_change = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 20, 20])
    pygame.display.update()

    # Update optimal_fps
    optimal_fps = int(my_hand.fps_counter()) + 20

    clock.tick(optimal_fps)

pygame.quit()

# Release capture device at the end of the program
ht.release_capture()

quit()
