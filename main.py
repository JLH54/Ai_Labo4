# This Python file uses the following encoding: utf-8
import sys

import pygame
import random
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSlider,QLabel
from PySide6.QtCore import QTimer

from paddle import paddle

class Timer:
    _clock = None
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self._clock.tick(60)/1000

    def get_deltaTime(self):
        return self._dt

class Game:
    ballDirection_X:int
    ballDirection_Y:int
    ball_speed:int
    ball_positionX:int
    ball_positionY:int

    player_speed:int
    player_positionX:int
    player_positionY:int
    player_width:int
    player_height:int

    ai_speed:int
    ai_positionX:int
    ai_positionY:int
    ai_width:int
    ai_height:int
    ai_directionY:int

    up_key_pressed:bool
    down_key_pressed:bool

    difficulty:int

    def __init__(self):
        pygame.init()
        self.gameInit()
        self.timer = Timer()
        self.playerPoints = 0
        self.aiPoints = 0
        self.ai_speed = 4
        self.ball_speed = 6
        self.should_quit = False
        self.up_key_pressed = False
        self.down_key_pressed = False

    def changeDifficulty(self, Gamedifficulty):
        self.ai_speed += Gamedifficulty
    def changeBallSpeed(self, ballSpeed):
        self.ball_speed += ballSpeed
    def loop(self):
        self.timer.update()
        dt = self.timer.get_deltaTime()

        self.process_input()
        self.gameLogic(dt)
        self.render()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.up_key_pressed = True
                if event.key == pygame.K_s:
                    self.down_key_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.up_key_pressed = False
                if event.key == pygame.K_s:
                    self.down_key_pressed = False


    def gameInit(self):
        self.size = self.width, self.height = 640, 480
        self.black = 0,0,0

        #self.player = paddle(30, 240,10, 100, 5)
        #self.ai = paddle(600, 450, 10, 100, 5)
        #self.ball_speed= 6 - int(self.difficulty)

        self.ballDirection_X = 1
        self.ballDirection_Y = 1
        self.ball_positionX = 320
        self.ball_positionY = 240

        self.player_speed = 5
        self.player_positionX = 30
        self.player_positionY = 240
        self.player_width = 10
        self.player_height = 100


        self.ai_positionX = 600
        self.ai_positionY = 450
        self.ai_width = 10
        self.ai_height = 100
        self.ai_directionY = 1

        self.screen = pygame.display.set_mode(self.size)

        self.circle = pygame.Surface([self.ball_positionX,self.ball_positionY])
        self.circlerect = pygame.draw.circle(self.circle, pygame.Color(255,255,255),[self.circle.get_width()/2, self.circle.get_height()/2], 5)

        #self.player = pygame.Surface([self.player_positionX,self.player_positionY])
        self.rectangle = pygame.Rect(self.player_positionX,self.player_positionY, self.player_width, self.player_height)
        #self.playerrect = pygame.draw.rect(self.screen, pygame.Color(255,255,255), self.player.get_paddle())

        self.ai_rectangle = pygame.Rect(self.ai_positionX,self.ai_positionY, self.ai_width, self.ai_height)
        self.ai_rect = pygame.draw.rect(self.screen, pygame.Color(255,255,255), self.ai_rectangle)

    def gameLogic(self, dt):
        if self.ball_positionX < 10:
            self.aiPoints += 1
            print("ai points : " + str(self.aiPoints))
            self.ball_positionX = 320
            self.ball_positionY = 240
        elif self.ball_positionX > 640:
            self.playerPoints += 1
            print("player points : " + str(self.playerPoints))
            self.ball_positionX = 320
            self.ball_positionY = 240
        if self.ball_positionY < 10:
            self.ballDirection_Y = 1
        elif self.ball_positionY > 470:
            self.ballDirection_Y = -1
        self.ball_positionX += self.ball_speed * self.ballDirection_X
        self.ball_positionY += self.ball_speed * self.ballDirection_Y

        #the ai behaviour
        if self.ai_positionY + (self.ai_height / 2) < self.ball_positionY and self.ai_positionY < 470 - self.ai_height:
            self.ai_directionY = 1
        elif self.ai_positionY + (self.ai_height / 2) > self.ball_positionY and self.ai_positionY > 10:
            self.ai_directionY = -1
        self.ai_positionY += self.ai_speed * self.ai_directionY

        #collisions
        if self.ball_positionX - 5 < self.player_positionX + self.player_width and self.ball_positionX > self.player_positionX and self.ball_positionY < self.player_positionY + self.player_height and self.ball_positionY > self.player_positionY:
            self.ballDirection_X = 1

        #if self.ball_positionX - 5 < self.player.get_X() + self.player.get_width() and self.ball_positionX > self.player.get_X() and self.ball_positionY < self.player.get_Y() + self.player.get_height() and self.ball_positionY > self.player.get_Y():
            #self.ballDirection_X = 1

        if self.ball_positionX + 5 < self.ai_positionX + self.player_width and self.ball_positionX > self.ai_positionX and self.ball_positionY < self.ai_positionY + self.ai_height and self.ball_positionY > self.ai_positionY:
            self.ballDirection_X = -1
        if self.player_positionY < 480 - self.player_height and self.down_key_pressed == True:
            self.player_positionY += self.player_speed
        if self.player_positionY > 10 and self.up_key_pressed == True:
            self.player_positionY -= self.player_speed

        #if self.player.get_Y() < 480 - self.player.get_height() and self.down_key_pressed == True:
            #self.player_positionY += self.player_speed
            #self.player.set_Y(self.player.get_speed() + self.player.get_Y())

        #if self.player.get_Y() > 10 and self.up_key_pressed == True :
            #self.player_positionY -= self.player_speed
            #y = self.player.get_speed() - self.player.get_Y()
            #self.player.set_Y(y)

    def render(self):
        self.screen.fill(self.black)

        self.screen.blit(self.circle, self.circlerect)
        self.circle = pygame.Surface([self.ball_positionX,self.ball_positionY])
        self.circlerect = pygame.draw.circle(self.circle, pygame.Color(255,255,255),[self.circle.get_width()/2, self.circle.get_height()/2], 5)


        self.playerRectangle = pygame.Rect(self.player_positionX,self.player_positionY, self.player_width, self.player_height)
        self.playerrect = pygame.draw.rect(self.screen, pygame.Color(255,255,255), self.playerRectangle)
        #self.player.render(self.screen)

        self.ai_rectangle = pygame.Rect(self.ai_positionX,self.ai_positionY, self.ai_width, self.ai_height)
        self.ai_rect = pygame.draw.rect(self.screen, pygame.Color(255,255,255), self.ai_rectangle)

        pygame.display.flip()

class Window(QWidget):
    started:bool
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.initUi()



    def init_pygame(self, game):
        self.game = game
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)

    def pygame_loop(self):
        if self.game.loop():
            self.close()

    def initUi(self):
        self.setWindowTitle("Py pong")
        self.setGeometry(0,400,300,200)

        self.button = QPushButton("Start Game", self)
        self.button.move(100, 150)
        self.button.clicked.connect(self.OnClick)

        #settings for ball
        self.label1 = QLabel("Ball speed", self)
        self.label1.move(1, 85)

        self.slider = QSlider(self)
        self.slider.sliderReleased.connect(self.OnSlider)
        self.slider.setRange(1, 3)
        self.slider.setSingleStep(1)
        self.slider.move(15, 1)

        #settings for ai
        self.label1 = QLabel("AI difficulty", self)
        self.label1.move(80, 85)

        self.aislider = QSlider(self)
        self.aislider.sliderReleased.connect(self.OnAiSlider)
        self.aislider.setRange(1, 3)
        self.aislider.setSingleStep(1)
        self.aislider.move(100, 1)

        self.show()

    def OnClick(self):
        self.init_pygame(self.game)
        pass

    def returnStart(self):
        return self.started

    def returnDifficulty(self):
        return self.slider.TickPosition

    def OnSlider(self):
        slider:QSlider = self.sender()
        self.game.changeBallSpeed(slider.value())
        print(slider.value())

    def OnAiSlider(self):
        slider:QSlider = self.sender()
        self.game.changeDifficulty(slider.value())
        print(slider.value())

def main():
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)

    app.setActiveWindow(exe)
    # ...
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
