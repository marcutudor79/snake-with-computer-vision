#OOP SNAKE GAME WITH HANDTRAKING
import pygame
from pygame.locals import *
import time
import random

# the size of the snake block
SIZE = 40

# do we need this?
# BACKGROUND_COLOR = (110, 110, 5)

# constant that helps with the movement of snek
# 0.5 min - 0.1 max
WAIT_TIME = 0.5  


class Apple:
    
    # constructing the first apple
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    
    # parent_screen is the surface on which we want the snek
    def __init__(self, parent_screen):
        
        # the surface on which we draw the snek
        self.parent_screen = parent_screen
        
        # a block of the snek's body
        self.image = pygame.image.load("resources/block.jpg").convert()
        
        # at first the snek goes down
        self.direction = 'down'

        self.time = 0
        self.length = 1
        
        #where the snake starts first
        self.x = [40]
        self.y = [40]

    #defines the movement of the head
    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    # changes the position of the blocks according to
    # the movement of the head
    def walk(self):
        
        # all the blocks move to the previous one's location
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # the head shall move itself according to the direction
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    # takes each block of the snek and updates it on the screen
    # according to the new position
    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    # x, y will become lists of coordinates for snek's blocks
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snek in the Metaverse")

        # this is the window of the game
        self.surface = pygame.display.set_mode((1000, 800))
        
        # snek is an attribute of the game (passing the surface)
        self.snake = Snake(self.surface)
        self.snake.draw()
        
        # apple is also an attribute of the game (passing the surface)
        self.apple = Apple(self.surface)
        self.apple.draw()

        # the way snek moves slower then the fps
        self.wait_time = WAIT_TIME

    # used when we restart the game
    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)
        self.wait_time = WAIT_TIME


    # if the snek hits the apple returns true otherwise returs false
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0,0))

    def render_bgwin(self):
        bg = pygame.image.load("resources/happypuppy.jpg")
        self.surface.blit(bg, (0,0))

    def render_bglose(self):
        bg = pygame.image.load("resources/sadpuppy.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        
        pygame.display.flip()

        # snek eating apple scenario (takes into consideration the
        # posibillity for the apple to not be eaten by the head)
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move()
                self.wait_time -= 0.0057

        # snek colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"

        # snek colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            raise "Hit the boundry error"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30, True)
        score = font.render(f"Score: {self.snake.length}", True, (200,200,200))
        self.surface.blit(score, (850,10))
        
        pygame.display.flip()

    def show_game_over(self):
        self.render_bglose()
        font = pygame.font.SysFont('arial', 30, True)
        
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (0, 0, 0))
        self.surface.blit(line1, (200, 300))
        
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (0, 0, 0))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()
    
    def show_game_win(self):
        self.render_bgwin()
        font = pygame.font.SysFont('arial', 30, True)    
        
        line1 = font.render("Congratulations! You won!", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))

        line2 = font.render(f"The snake reached its maximum length: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        
        line3 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line3, (200, 400))
        
        pygame.display.flip()

<<<<<<< Updated upstream
=======
    def can_play(self):
        
        if self.delay == False:
            time.sleep(0.2)
            self.delay = True
        
        if self.delay == True:
            return True
        if self.delay == False:
            return False
        
>>>>>>> Stashed changes
    # the function that runs the game
    def run(self):

        # to be running or not to be running
        # this is the question        
        running = True
        
        # variable for pausing the game
        pause = False

        while running:
            for event in pygame.event.get():
                
                # the spidey sense of the game wether we pressed a key
                # or not
                if event.type == KEYDOWN:
                    
                    # logic for pausing or exiting the game
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    # this is where we choose how the snek moves
                    if not pause:
                        if event.key == K_LEFT: # change this with sorin's module
                            self.snake.move_left()

                        if event.key == K_RIGHT: # change this with sorin's module
                            self.snake.move_right()

                        if event.key == K_UP: # change this with sorin's module
                            self.snake.move_up()

                        if event.key == K_DOWN: # change this with sorin's module
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            
            # snake reaches maximum length
            if self.snake.length == 5:
                self.show_game_win()
                pause = True
                self.reset()
                        
            try:

                if not pause:
                    
                    # continues the game (updating the blocks)
                    self.play()
                    
                    # snek will be slower then the game tick
                    time.sleep(self.wait_time)

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            
            # the game runs at 30 fps
            pygame.time.Clock().tick(30)

if __name__ == '__main__':
    game = Game()
    game.run()