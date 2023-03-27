import pygame, sys, random, time

    #initialize constants
BLACK = (27, 27, 27)
WHITE = (250, 235, 215)
BLUE = (102, 102, 153)
GREEN =  (3, 192, 60)
RED = (255, 99, 71)
SCREEN_X, SCREEN_Y = 720, 480
FRAMES_PER_SECOND = 60
SNAKE_SPEED = 4


#initialize game settings
pygame.init()
pygame.display.set_caption("Snake")
window = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)
def snake():

    #set up snake and fruit
    #snake
    snake_body = 12
    snake_pos = [320, 240]
    snake = [
            [320, 240],
            [305, 240],
            [290, 240],
            [275, 240]
            ]

    direction = 'RIGHT'
    count = 3
    collision = False
    #fruit
    fruit_body = 15
    fruit_max_x = SCREEN_X - fruit_body
    fruit_max_y = SCREEN_Y - fruit_body
    fruit_x = random.randrange(fruit_max_x)
    fruit_y = random.randrange(fruit_max_y)
    fruit_rect = pygame.Rect(fruit_x, fruit_y, fruit_body, fruit_body)


    score = 0

    #create forever game loop
    while True:
        for event in pygame.event.get():
            
            #Check for quit request 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Check for keyboard input from user
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    direction = 'UP'
                if event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                if event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
            
            #change path of snake
        if direction == 'UP':
            snake_pos[1] -= SNAKE_SPEED
        if direction == 'DOWN':
            snake_pos[1] += SNAKE_SPEED
        if direction == 'LEFT':
            snake_pos[0] -= SNAKE_SPEED
        if direction == 'RIGHT':
            snake_pos[0] += SNAKE_SPEED
        

        
        
        
        
        #clear screen
        window.fill(BLACK)

        #display score
        score_text = font.render(f'Player score: {score}', True, WHITE)
        window.blit(score_text, (300, 10))
        
        #draw snake and fruit
        snake.insert(0, list(snake_pos))
        for pos in snake:
            snake_rect = pygame.Rect(pos[0], pos[1], snake_body, snake_body)
            pygame.draw.rect(window, GREEN, snake_rect)
        pygame.draw.rect(window, RED, fruit_rect)

        #create boundries
        if snake_pos[0] < -15 or snake_pos[0] > SCREEN_X  or snake_pos[1] < -15 or snake_pos[1] > SCREEN_Y:
            game_over(score)
            break

        #collision with snake and fruit
        if ((snake_pos[0] < fruit_x + 15 and snake_pos[0] > fruit_x) and (snake_pos[1] < fruit_y + 15 and snake_pos[1] > fruit_y) or 
        (snake_pos[0] + 10 < fruit_x + 15 and snake_pos[0] + 10 > fruit_x) and (snake_pos[1] + 10 < fruit_y + 15 and snake_pos[1] + 10 > fruit_y)):

            snake.insert(0, [fruit_x, fruit_y])
            fruit_x = random.randrange(fruit_max_x)
            fruit_y = random.randrange(fruit_max_y)
            fruit_rect = pygame.Rect(fruit_x, fruit_y, fruit_body, fruit_body)
            score += 5
            count += 1
        else:
            snake.pop()
        
        #snake collision with its self
        if len(snake) >= 4: 
            for y in range(11):
                if collision == True:
                    break
                for pos in snake[3:]:
                    if collision == True:
                        break
                    if ((snake_pos[0] >= pos[0]) and (snake_pos[0] + y <= pos[0] + y) and (snake_pos[1] >= pos[1]) and (snake_pos[1] + y <= pos[1] + y)):
                        game_over(score)
                        collision = True
                        break

        if collision == True:
            break
                
                    
        pygame.display.update()

        clock.tick(FRAMES_PER_SECOND)

def game_over(score):
     #creating end game, first message
    window.fill(BLUE)
    game_over_text  = font.render(f'Game Over', True, WHITE)
    window.blit(game_over_text, (300, 240))
    pygame.display.update()
    time.sleep(2)

    #creating end game, second message
    window.fill(BLUE)
    game_over_text = font.render(f'Player Score: {score}', True, WHITE)
    window.blit(game_over_text, (300, 240))
    pygame.display.update()
    time.sleep(2)

if __name__ == '__main__':
    snake()


