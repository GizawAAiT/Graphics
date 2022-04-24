import tkinter
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from pygame.locals import *
from tkinter import *

x = np.linspace(-10, 10, 1000000)
sin = np.sin(x)
inverse_sin = np.arcsinh(x)
cos = np.cos(x)
inverse_tan = np.arctan(x)
inverse_tan_hyperbolic = np.arctanh(x)
cos_hyperbolic = np.cosh(x)
functions = {"f(x)=sin(x)": sin, "f(x)=arcsin(x)": inverse_sin, "f(x)=cos(x)": cos,
             "f(x)=arctan(x)": inverse_tan, "f(x)=arctanh(x)": inverse_tan_hyperbolic, "f(x)=cosh(x)": cos_hyperbolic}

button_tuple = ("sign_button", "arcsin_butotn", "cos_button", "arctan_button", "arctanh_button", "cosh_button")
selected_functions = []

# tkinter.

input_window = Tk()
input_window.geometry('400x500')
input_window.title("Just Select 2 functions to be drown!")

error_box = Text(input_window, bg="black", fg="red", width=40, height=3)

def destroy_tkinter():
    try:
        if len(selected_functions) != 2:
            raise ValueError
        input_window.destroy()
    except ValueError:
        error_msg = ""
        if len(selected_functions) > 2:
            error_msg = f"Extra Input:\nOnly 2 functions supported\n but {len(selected_functions)} given. "
        elif len(selected_functions) < 2:
            error_msg = f"Atleast 2 functions requered"
        error_box.insert(tkinter.END, error_msg)
        error_box.pack()

def onPressed(btn, func):
    error_box.delete("1.0", "end")
    error_box.forget()
    if func not in selected_functions:
        btn["bg"] = "green"
        selected_functions.append(func)
    else:
        btn["bg"] = "grey"
        selected_functions.remove(func)

sinx = Button(input_window, text="f(x)=sin(x)", command=lambda: onPressed(sinx, "f(x)=sin(x)"),
      activebackground="green", width=20, justify="left", background="grey")
sinx.pack()
arcsinx = Button(input_window, text="f(x)=arcsin(x)", command=lambda: onPressed(arcsinx, "f(x)=arcsin(x)"),
                 activebackground="green", width=20, justify="left", background="grey")
arcsinx.pack()
cosx = Button(input_window, text="f(x)=cos(x)", command=lambda: onPressed(cosx, "f(x)=cos(x)"),
              activebackground="green", width=20, justify="left", background="grey")
cosx.pack()
arctanx = Button(input_window, text="f(x)=arctan(x)", command=lambda: onPressed(arctanx, "f(x)=arctan(x)"),
                 activebackground="green", width=20, justify="left", background="grey")
arctanx.pack()
arctanhx = Button(input_window, text="f(x)=arctanh(x)", command=lambda: onPressed(arctanhx, "f(x)=arctanh(x)"),
                  activebackground="green", width=20, justify="left", background="grey")
arctanhx.pack()
coshx = Button(input_window, text="f(x)=cosh(x)", command=lambda: onPressed(coshx, "f(x)=cosh(x)"),
               activebackground="green", width=20, justify="left", background="grey")
coshx.pack()
draw_now = Button(input_window, text="DROW", command=destroy_tkinter, pady=20, padx=25, background="green",
                  activebackground="blue")
draw_now.place(x=40,y=60)
draw_now.pack()

input_window.mainloop()

# pygame and opengl.

pygame.init()

pygameWindow = pygame.display.set_mode((600, 700), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Gizaw Dagne_UGR/6640/12_sec 2.py")
font = pygame.font.SysFont("Arial", 20)
glClearColor(0.5, 0.4, 0.5, 1)
gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def draw(m, c):
    glLineWidth(4)
    glPointSize(2)
    
    # x-y coordinate.
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_STRIP)

    glVertex2f(8, 0)
    glVertex2f(-8, 0)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(0, 8)
    glVertex2f(0, -8)
    glEnd()
    # first function.
    glColor3f(0.4, 1, 0.0)
    glBegin(GL_POINTS)
    for a, b in zip(x, functions[m]):
        glVertex2f(a, b)
    glEnd()
    
    # second function.
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.1, 0.5)
    for a, b in zip(x, functions[c]):
        glVertex2f(a, b)
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

        draw(selected_functions[0], selected_functions[1])
        pygame.display.flip()
        pygame.time.wait(1)

main()
