from pygame import *
from random import randrange
SCREEN_W, SCREEN_H = 800,800
screen = display.set_mode((SCREEN_W, SCREEN_H))

WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x,y
    def draw(self):
        draw.circle(screen, WHITE, (self.x, self.y), 10, 4)

class Line:
    def __init__(self, m=1, b=0):
        self.m, self.b = m,b
    def f(self, x):
        return self.m*x + self.b
    def draw(self):
        p1, p2 = (0,SCREEN_H-self.f(0)), (SCREEN_W, SCREEN_H-self.f(SCREEN_W))
        draw.line(screen, RED, p1, p2)

numPoints = 100
points = [Point(randrange(0,SCREEN_W), randrange(0,SCREEN_H)) for _ in range (numPoints)]
line = Line(1,100)

def drawPoints():
    for p in points:
        p.draw()

run = True
while run:
    drawPoints()
    line.draw()
    
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.flip()
quit()