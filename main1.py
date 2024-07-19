import pygame
import sys
import random


pygame.init()

# Set up display
window_size = (600, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake Game By Subrat')

# Define colors
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

# Define snake and food classes
class Snake:
    def __init__(self):
        self.size = 10
        self.body = [(100, 50), (90, 50), (80, 50)]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_dir(self, direction):
        if direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if direction == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if direction == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def move(self, food_pos):
        head = self.body[0]
        if self.direction == 'RIGHT':
            head = (head[0] + self.size, head[1])
        if self.direction == 'LEFT':
            head = (head[0] - self.size, head[1])
        if self.direction == 'UP':
            head = (head[0], head[1] - self.size)
        if self.direction == 'DOWN':
            head = (head[0], head[1] + self.size)

        self.body.insert(0, head)
        if head == food_pos:
            return True
        else:
            self.body.pop()
            return False

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= window_size[0] or head[1] < 0 or head[1] >= window_size[1]:
            print(head[0],head[1])
            return True
        for block in self.body[1:]:
            if head == block:
                return True
        return False

    def draw(self):
        for block in self.body:
            pygame.draw.rect(window, Green, pygame.Rect(block[0], block[1], self.size, self.size))

class Food:
    def __init__(self):
        self.size = 10
        self.position = self.random_position()

    def random_position(self):
        return (random.randrange(1, window_size[0]//self.size) * self.size,
                random.randrange(1, window_size[1]//self.size) * self.size)

    def draw(self):
        pygame.draw.rect(window, Red, pygame.Rect(self.position[0], self.position[1], self.size, self.size))
#main game loop 
def game_loop():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    score = 0 #initialising score 0 
    font = pygame.font.SysFont(None, 35)

    def display_score(score):
        score_text = font.render(f'Score: {score}', True, White)
        window.blit(score_text, [0, 0])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_dir('UP')
                if event.key == pygame.K_DOWN:
                    snake.change_dir('DOWN')
                if event.key == pygame.K_LEFT:
                    snake.change_dir('LEFT')
                if event.key == pygame.K_RIGHT:
                    snake.change_dir('RIGHT')

        if snake.move(food.position):
            score += 1
            while food.position in snake.body:
                food.position = food.random_position()

        if snake.check_collision():
            pygame.quit()
            sys.exit()
            

        window.fill(Black)
        snake.draw()
        food.draw()
        display_score(score)
        pygame.display.update()
        clock.tick(15)


if __name__ == '__main__':
    game_loop()
