#!/usr/bin/env python3
""" Pong Clone made by Me with pygame"""

import pygame
import random
from random import randint

class Field:
    """Holds the size and position of the field"""
    #Maybe it should be a function instead
    def __init__(self, gameDisplay, fieldXPos, fieldYPos, fieldWidth, fieldHeight, fieldBorderSize):
        self.fieldXPos = fieldXPos
        self.fieldYPos = fieldYPos
        self.fieldWidth = fieldWidth
        self.fieldHeight = fieldHeight
        self.fieldBorderSize = fieldBorderSize
        self.gameDisplay = gameDisplay

    def draw(self):
        """Draws the field to the gameDisplay"""
        pygame.draw.rect(self.gameDisplay, (0,0,255), [self.fieldXPos, self.fieldYPos, self.fieldWidth, self.fieldHeight], self.fieldBorderSize)

    def score(self, player1Score, player2Score):
        """Handels the score of the players"""
        self.player1Score = player1Score
        self.player2Score = player2Score

    def drawScore(self):
        """Draws the score to the screen to the field"""
        pass

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
        #self.paddleYPos += self.direction
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
            self.paddleYPos = 490
            self.direction = 0
        
    @property
    def rect(self):
        return pygame.Rect(self.paddleXPos, self.paddleYPos, self.paddleWidth, self.paddleHeight)

class Ball(object):
    """Holds size and position"""
    def __init__(self, gameDisplay, ballXPos, ballYPos, xDirection, yDirection):
        self.ballXPos = ballXPos
        self.ballYPos = ballYPos
        self.gameDisplay = gameDisplay
        self.xDirection = xDirection
        self.yDirection = yDirection

    def draw(self):
        """Draws the ball to the screen"""
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), [self.ballXPos, self.ballYPos, 10, 10])

    def move(self, obstacles):
        """Direction and speed of the ball"""
        self.ballXPos = self.ballXPos + (5 * self.xDirection)
        self.ballYPos = self.ballYPos + (5 * self.yDirection)
        if self.ballXPos >= 800:
            self.xDirection = -self.xDirection
        elif self.ballXPos <= 0:
            self.xDirection = -self.xDirection
        if self.ballYPos >= 580:
            self.yDirection = -self.yDirection
        elif self.ballYPos <= 100:
            self.yDirection = -self.yDirection
        if self.rect.collidelist(obstacles) != -1:
            self.xDirection = -self.xDirection

    @property
    def rect(self):
        return pygame.Rect(self.ballXPos, self.ballYPos, 10, 10)
    
def windowSetup():
    """Setting all initial variables and functions for start up"""
    
    pygame.display.set_caption('Pong Clone')
    
    windowWidth = 800
    windowHeight = 600

def score():
    pass

def main():
    """Pong Clone that uses pygame"""
    pygame.init()
    windowSetup()
    clock = pygame.time.Clock()
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))
    paddleWidth = 10
    paddleHeight = 100
    xPos = 400
    yPos = 300
    court = Field(gameDisplay, 8,98, 782, 492, 2)
    player1 = Paddle(gameDisplay, 50, 250, paddleWidth, paddleHeight)
    player2 = Paddle(gameDisplay, 750, 250, paddleWidth, paddleHeight)
    ball = Ball(gameDisplay, 300, 300, 1, 1)
    players = (player1, player2)
    player1.draw()
    player2.draw()
    ball.draw()

    print(randint(0, 10))
    
    while not gameExit:                 #Main game loop
        for event in pygame.event.get():        #Event handler
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xPos -= 5
                elif event.key == pygame.K_RIGHT:
                    xPos += 5
                elif event.key == pygame.K_UP:
                    yPos -= 5
                    player1.move(-5)
                    player2.move(-5)
                elif event.key == pygame.K_DOWN:
                    yPos += 5
                    player1.move(5)
                    player2.move(5)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    yPos -= 5
                    player1.move(0)
                    player2.move(0)
                elif event.key == pygame.K_DOWN:
                    yPos += 5
                    player1.move(0)
                    player2.move(0)
                

        gameDisplay.fill((0, 0, 0))
        court.draw()
        pygame.draw.rect(gameDisplay, (255, 0, 0), [xPos, yPos, 10, 10], 2)        

        for player in players:
            player.draw()
        ball.move(players)
        ball.draw()
        
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()

    
if __name__ == "__main__":
    main()
