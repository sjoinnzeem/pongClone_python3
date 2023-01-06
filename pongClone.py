#!/usr/bin/env python3
""" Pong Clone made by sjoinnzeem with pygame"""
"""https://github.com/sjoinnzeem"""

import pygame
import random
from random import randint

class Field:
    """Holds the size and position of the field"""
    #Maybe it should be a function instead
    def __init__(self, gameDisplay,
                 fieldXPos, fieldYPos,
                 fieldWidth, fieldHeight,
                 fieldBorderSize):
        
        self.fieldXPos = fieldXPos
        self.fieldYPos = fieldYPos
        self.fieldWidth = fieldWidth
        self.fieldHeight = fieldHeight
        self.fieldBorderSize = fieldBorderSize
        self.gameDisplay = gameDisplay

    def draw(self):
        """Draws the field to the gameDisplay"""
        pygame.draw.rect(self.gameDisplay, (0, 0, 255),
                         [self.fieldXPos, self.fieldYPos,
                          self.fieldWidth, self.fieldHeight],
                        self.fieldBorderSize)

    def score(self, player1Score, player2Score):
        """Handels the score of the players"""
        self.player1Score = player1Score 
        self.player2Score = player2Score 

    def addScore(self, addScoreToPlayer):
        """Add a score to the current standing in the match"""
        if addScoreToPlayer == 1:
            self.player1Score += 1
        elif addScoreToPlayer == 2:
            self.player2Score += 1
    
    def drawScore(self):
        """Draws the score to the screen to the field"""
        font=pygame.font.Font(None, 100)
        scoretext=font.render(str(self.player1Score) + ' : '  + str(self.player2Score), 1, (255, 255, 255))
        self.gameDisplay.blit(scoretext, (350, 20))
        
class Paddle(object):
    """Holds size and position of the paddle also moves and draws it to the display"""
    def __init__(self, gameDisplay, paddleXPos, paddleYPos, paddleWidth, paddleHeight):
        self.paddleXPos = paddleXPos
        self.paddleYPos = paddleYPos
        self.gameDisplay = gameDisplay
        self.paddleWidth = paddleWidth
        self.paddleHeight = paddleHeight
        self.direction = 0

    def draw(self):
        """Draws the paddle to the display"""
        self.move(self.direction)
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), [self.paddleXPos, self.paddleYPos, self.paddleWidth, self.paddleHeight])

    def move(self, direction):
        """Moves the paddle according to direction"""
        self.direction = direction
        self.paddleYPos += self.direction
        if self.paddleYPos <= 100:
            self.paddleYPos = 100
            self.direction = 0
        if self.paddleYPos >= 490:
            self.paddleYPos = 488
            self.direction = 0
        
    @property
    def rect(self):
        return pygame.Rect(self.paddleXPos, self.paddleYPos, self.paddleWidth, self.paddleHeight)

class Ball(object):
    """Holds size and position"""
    def __init__(self, gameDisplay, ballXPos, ballYPos, xDirection, yDirection):
        self.ballXPos = self.ballStartXPos = ballXPos
        self.ballYPos = self.ballStartYPos = ballYPos
        self.gameDisplay = gameDisplay
        self.xDirection = xDirection
        self.yDirection = yDirection
        self.xSpeed = 5
        self.ySpeed = 5
        """Prepare fore scoring"""
        self.score = 0
        
    def draw(self):
        """Draws the ball to the screen"""
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), [self.ballXPos, self.ballYPos, 10, 10])

    def move(self, pointReset, xCollitionDetected, yCollitionDetected):
        """Direction and speed of the ball"""
        self.score = pointReset
        self.xCollitionDetected = xCollitionDetected
        self.yCollitionDetected = yCollitionDetected
        self.ballXPos = self.ballXPos + (self.xSpeed * self.xDirection * self.xCollitionDetected)
        self.ballYPos = self.ballYPos + (self.ySpeed * self.yDirection * self.yCollitionDetected)
        
        if self.ballXPos >= 780:
            self.xDirection = -self.xDirection
            self.score = 2
            self.reset()
        elif self.ballXPos <= 10:
            self.xDirection = -self.xDirection
            self.score = 1
            self.reset()
        if self.ballYPos >= 580:
            self.yDirection = -self.yDirection
        elif self.ballYPos <= 100:
            self.yDirection = -self.yDirection
        #if self.rect.colliderect(obstacles):
            #print('colliding')
            #sur_obj.fill((0,0,0)) 
     
        #if self.rect.collidelist(obstacles) != -1:
            """collition between ball and paddle"""
            """ NOT WORKING PROPERLY """
            """if self.ballXPos <= 50 or self.ballXPos >= 750:
                self.xDirection = self.xDirection
                self.yDirection = -self.yDirection
            elif self.ballXPos >= 51 or self.ballXPos <=751:
                self.xDirection = -self.xDirection"""
        
    def reset(self):
        """Resets the ball to start position"""
        self.ballXPos = self.ballStartXPos
        self.ballYPos = self.ballStartYPos

    @property
    def rect(self):
        return pygame.Rect(self.ballXPos, self.ballYPos, 10, 10,)

    def score(self):
        return self.score

    def direction(self):
       ballDir = [self.xDirection, self.yDirection] 
       return ballDir
           
def windowSetup():
    """Setting all initial variables and functions for start up"""
    pygame.display.set_caption('Pong Clone')
    windowWidth = 800
    windowHeight = 600
        
def texts(gameDisplay, score):
    font=pygame.font.Font(None,30)
    scoretext=font.render("Score:"+str(score), 1,(255,255,255))
    gameDisplay.blit(scoretext, (500, 457))

def collitionDetection():
    """Not implemented yet
    if ball.rect.colliderect(players[0]):
        print('colliding')
        if abs(ball.rect.right - players[0].rect.left) < 10:
            print('right edge')
            #ball.ballDir
        elif abs(ball.rect.bottom - players[0].rect.top) < 10:
            print('bottom edge')
        elif abs(ball.rect.top - players[0].rect.bottom) < 10:
            print('top edge')
        elif abs(ball.rect.left - players[0].rect.right) < 10:
            print('left edge') """


def main():
    """Pong Clone that uses pygame"""
    """Setup variabels, values and classes"""
    pygame.init()
    windowSetup()
    clock = pygame.time.Clock()
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))
    paddleWidth = 100
    paddleHeight = 100
    xPos = 400
    yPos = 300
    court = Field(gameDisplay, 8,98, 782, 492, 2)
    court.score(0, 0)
    player1 = Paddle(gameDisplay, 50, 250, paddleWidth, paddleHeight)
    player2 = Paddle(gameDisplay, 740, 250, paddleWidth, paddleHeight)
    ball0 = Ball(gameDisplay, 400, 295, 1, 1) #add random for direction
    players = [player1, player2]
    balls = [ball0]
    player1.draw()
    player2.draw()
    ball0.draw()
    xCollition = 1
    yCollition = 1

    """    Main game loop   """
    while not gameExit:
        for event in pygame.event.get():        #Event handler
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                elif event.key == pygame.K_LEFT:
                    print(len(balls))
                elif event.key == pygame.K_RIGHT:
                    randDir = random.choice([-2, -1, 1, 2])
                    balls.append(Ball(gameDisplay, 400, 295, randDir, random.choice([-1, 1])))
                elif event.key == pygame.K_UP:
                    player1.move(-5)
                    player2.move(-5)
                elif event.key == pygame.K_DOWN:
                    player1.move(5)
                    player2.move(5)
                elif event.key == pygame.K_s:
                    player1.move(-5)
                elif event.key == pygame.K_z:
                    player1.move(5)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player1.move(0)
                    player2.move(0)
                elif event.key == pygame.K_DOWN:
                    player1.move(0)
                    player2.move(0)
                elif event.key == pygame.K_s:
                    player1.move(0)
                elif event.key == pygame.K_z:
                    player1.move(0)
                
        gameDisplay.fill((0, 0, 0))
        court.draw()
        court.drawScore()

        for player in players:
            """Actions for all the players on the court"""
            player.draw()
           
        for ball in balls:
            """Actions for all the balls on the court"""

            #ballDir = ball.direction() #gets a list of xDirection and yDirection of the ball
            if ball.rect.colliderect(players[0]):
                print('colliding')
                if abs(ball.rect.left - players[0].rect.right) < 15:
                    print('right edge')
                    xCollition *= -1
                #elif abs(ball.rect.left - players[0].rect.right) < 10:
                #    print('left edge')
                #    collition *= -1 
                elif abs(ball.rect.bottom - players[0].rect.top) < 15:
                    print('bottom edge')
                    yCollition *= -1
                elif abs(ball.rect.top - players[0].rect.bottom) < 15:
                    print('top edge')
                    yCollition *= -1
            if ball.rect.colliderect(players[1]):
                print('colliding')
                #if abs(ball.rect.right - players[1].rect.left) < 10:
                #    print('right edge')
                #    collition *= -1
                if abs(ball.rect.right - players[1].rect.left) < 15:
                    print('left edge')
                    xCollition *= -1 
                elif abs(ball.rect.bottom - players[1].rect.top) < 15:
                    print('bottom edge')
                    yCollition *= -1
                elif abs(ball.rect.top - players[1].rect.bottom) < 15:
                    print('top edge')
                    yCollition *= -1
                
            if ball.score == 1:
                court.addScore(1)
            elif ball.score == 2:
                court.addScore(2)
            if ball.score > 0:
                if len(balls) > 1:
                    balls.remove(ball)
            else:
                ball.draw()
            ball.move(0, xCollition, yCollition)   
                           
            """if ball.rect.colliderect(players[0]) and ball.direction[0] > 0:
                if abs(ball.rect.right - players[0].rect.left) < 10:
                    #ball_speed_x *= -1
                    print('test')"""
            
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()
