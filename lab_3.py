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
    glClearColor(1.0, 1.0, 0.0, 0.1)
    # gluOrtho2D(-1.0, 1.0, -10.0, 1.0)
    # gluOrtho2D(-1.0, 1.0, 10.0, 1.0)
    # gluOrtho2D(10.0, 1.0, -1.0, 1.0)
    # gluOrtho2D(-10.0, 1.0, -1.0, 1.0)
    # gluOrtho2D(-1.0, 1.0, -10.0, 10.0)
    # gluOrtho2D(-1.0, 1.0, -10.0, -10.0)
    # gluOrtho2D(-1.0, 1.0, -10.0, 1.0)
    # gluOrtho2D(-1.0, 10.0, -10.0, 1.0)
    # gluOrtho2D(-1.0, -10.0, -10.0, 1.0)
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    # generate 100 points within -1 to 1 range
    x = np.linspace(-1, 1, 100)
    # rais every point in x by 2
    y = np.log(x)
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
# for every pair (a, b) of the numbers in x, y
    for a, b in zip(x, y):
        # give (a, b+3) to OpenGL to draw
        glVertex2f(a, b)
    glEnd()
    glFlush()

def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()