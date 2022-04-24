import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
from pygame.locals import *

x = np.linspace(-10, 10, 10000)
s = np.sin(x)
sh = np.arcsinh(x)
t = np.cos(x)
r = np.arctan(x)
c = np.arctanh(x)
v = np.cosh(x)
myFunctions = {"f(x)=sin(x)": 0, "f(x)=arcsin(x)": 1, "f(x)=cos(x)": 2, "f(x)=arctan(x)": 3, "f(x)=arctanh(x)": 4,
               "f(x)=cosh(x)": 5}
ls = [s,c]

pygame.init()
pygameWindow = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Gizaw Dagne_UGR/6640/12_sec 2.py")


font = pygame.font.SysFont("Constantia", 20)
glClearColor(0.5, 0.4, 0.5, 1)
gluOrtho2D(-10.0, 10.0, -10.0, 10.0)
white=(1,0,0)


class Button():
    button_col = (255, 0, 0)
    b_col = (0,0,0)
    t_color = (1, 1, 0.4)
    button_width = 200
    button_height = 50

    def __init__(self, x, y, function_name):
        self.x = x
        self.y = y
        self.text = function_name

    def drawButton(self):
        position = pygame.mouse.get_pos()
        print(position)
        button_box = Rect(self.x, self.y, self.button_width, self.button_height)
        pygame.draw.rect(pygameWindow, self.button_col, button_box)

        text_img = font.render(self.text, True, self.t_color)
        text_len= text_img.get_width()
        pygameWindow.blit(text_img, (self.x + int(self.button_width // 2)-int(text_len//2), self.y + 5))
        pygame.draw.line(pygameWindow,white,(self.x,self.y),(self.x + self.button_width,self.y),40)


counter="something!"
red = (255, 0, 0)

def draw(m, c):
    glLineWidth(4)
    glPointSize(2)
    glColor3f(0.4, 1, 0.0)
    glBegin(GL_POINTS)
    for a, b in zip(x, m):
        glVertex2f(a, b)

    glEnd()
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.1, 0.5)
    for a, b in zip(x, c):
        glVertex2f(a, b)

    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_STRIP)

    glVertex2f(8, 0)
    glVertex2f(-8, 0)
    glEnd()
    glBegin(GL_LINE_STRIP)

    glVertex2f(0, 8)
    glVertex2f(0, -8)
    glEnd()

    glFlush()


def main():
    pygame.init()

    while True:
        glClear(GL_COLOR_BUFFER_BIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw(ls[0], ls[1])
        # glClear(GL_COLOR_BUFFER_BIT)
        # draw(v,r)
        # draw(sh,t)
        sinx=Button(100, 100, "sinx")
        sinx.drawButton()
        cos = Button(100, 200, "sinx")
        cos.drawButton()
        # counter_img = font.render(counter, True, red)
        # pygameWindow.blit(counter_img, (280, 450))
        pygame.display.flip()
        pygame.time.wait(1)

main()
