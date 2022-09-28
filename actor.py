# This Python file uses the following encoding: utf-8


class actor:
    def __init__(self, x,y,width,height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.directionX:int
        self.directionY:int

    def get_X(self):
        return self.x

    def set_Y(self, y):
        self.y = y

    def get_Y(self):
        return self.y

    def get_speed(self):
        return self.speed

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
