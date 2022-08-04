import pygame
import time
import random 

# This is an introductory Pygame project that recreates "AimLab", a popular game used by FPS (first-person shooter) gamers.

# driver code
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Aim Trainer')

screen_width = 800
screen_height = 600

white = (255, 255, 255)
blue = (0, 255, 255)
red = (255, 0, 0)

screen.fill(white) 

font_style = pygame.font.SysFont("bahnschrift", 25)

# randomizes the placement of the projectile to be shot  
def newProjectile():
    xCoord = round(random.randrange(20, screen_width - 20) / 10) * 10
    yCoord = round(random.randrange(20, screen_height - 30) / 10) * 10
    return [xCoord, yCoord]

# returns true if the click is within range of the current location
def isWithinRange(currentLocation, xPos, yPos):
    correctX = currentLocation[0]
    correctY = currentLocation[1]
    result = True
    
    if (xPos <= correctX + 20 and xPos >= correctX - 20):
        if (yPos <= correctY + 20 and yPos >= correctY - 20):
            result = True
    else:
        result = False
    return result    

# prints the score to the screen
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, red)
    screen.blit(value, [0, 0])   

# prints a message to the screen
def message(msg, color):
    text = font_style.render(msg, True, color)
    screen.blit(text, [screen_width / 6, screen_height / 3])    

# driver code
def gameStart():
    # new try driver code
    screen.fill(white)
    currentLocation = newProjectile()
    pygame.draw.circle(screen, blue, currentLocation, 20)
    currentScore = 0
    failedTries = 0
    gameOver = False
    gameClosed = False
    Your_score(currentScore)
    
    while not gameOver:

        # loss screen
        while gameClosed == True:
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(currentScore)
            pygame.display.update()

            # revise this code
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClosed = False
                    if event.key == pygame.K_c:
                        gameStart()

        # main event handling 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if failedTries == 3:
                gameClosed = True    
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                xPos = pos[0]
                yPos = pos[1]

                if isWithinRange(currentLocation, xPos, yPos):
                    currentScore += 1
                    pygame.display.update()
                    pygame.draw.circle(screen, white, currentLocation, 20)
                    currentLocation = newProjectile()
                    screen.fill(white)
                    Your_score(currentScore)
                    pygame.draw.circle(screen, blue, currentLocation, 20)
                else:
                    screen.fill(white)
                    Your_score(currentScore)
                    failedTries += 1 
                    message("Miss! " + str(3 - failedTries) + " tries remaining.", red)   
                    pygame.draw.circle(screen, blue, currentLocation, 20)
            pygame.display.update()        
    pygame.quit()
    quit()

gameStart()     