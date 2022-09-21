# This Python file uses the following encoding: utf-8
import sys

import pygame

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSlider
from PySide6.QtCore import QTimer

class Timer:
    _clock = none
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self_clock.tick(60)/1000

    def get_deltaTime(self):
        return self.__dt

class Game:
    def __init__(self):
        pygame.init()
        self.gameInit()
        self.timer = Timer()
        self.should_quit = False
        pass

    def loop(self):
        self.timer.update()
        dt = self.timer.get_deltaTime()

        self.process_input()

        self.render()
        return False

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == 119:

            elif event.type == pygame.KEYUP:
        pass
    def gameInit(self):
        self.size = self.width, self.height = 640, 480
        self.black = 0,0,0

        self.screen = pygame.display.set_mode(self.size)

        self.circle = pygame.Surface([111,111])
        self.circlerect = pygame.draw.circle(self.circle, pygame.Color(255,255,255),[self.circle.get_width()/2, self.circle.get_height()/2], 50)
        pass
    def render(self):
        self.screen.fill(self.black)

        self.screen.blit(self.circle, self.circlerect)

        pygame.display.flip()

class Window(QWidget,):
    def __init__(self, game):
        super().__init__()
        self.initUi()
        self.init_pygame(game)
        pass
    def init_pygame(self, game):
        self.game = game
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)
        pass

    def pygame_loop(self):
        if self.game.loop():
            self.close()
        pass
    def initUi(self):
        self.setWindowTitle("Py pong")
        self.setGeometry(0,400,300,200)


        self.button = QPushButton("Stop right there", self)
        self.button.setToolTip("You criminal scum!")
        self.button.move(100, 70)
        self.button.clicked.connect(self.OnClick)

        self.slider = QSlider(self)
        self.slider.sliderReleased.connect(self.OnSlider)
        self.slider.setRange(500, 1500)
        self.slider.setSingleStep(10)


        self.show()
        pass

    def OnClick(self):
        pass

    def OnSlider(self):
        slider:QSlider = self.sender()
        print(slider.value())
        pass
def main():
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)
    app.setActiveWindow(exe)
    # ...
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
