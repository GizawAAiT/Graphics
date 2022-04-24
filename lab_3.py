import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import  numpy as np
from math import *
def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-4,4,-4,4)
    glClearColor(1.0, 1.0, 0.0, 0.1)
    

def draw():
    glColor3f(1.0, 0.0, 0.0)
    # generate 100 points within -1 to 1 range
    x = np.linspace(0.0001, 1, 1000)
    # rais every point in x by 2
    y = np.log(x)
    glPointSize(100)
    glBegin(GL_LINES)
# for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # give (a, b+3) to OpenGL to draw
        glVertex2f(a, b)
    glEnd()
    glFlush()

def triangle():
    glColor3f(0,1,0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(-2, 0)
    glVertex2f(2, 0)
    glVertex2f(0, 2)
    glVertex2f(-2, 0)
    glEnd()

def main():
    init()
    glClear(GL_COLOR_BUFFER_BIT)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        glLineWidth(10)
        triangle()
        draw()
        pygame.display.flip()
        pygame.time.wait(1000)

main()