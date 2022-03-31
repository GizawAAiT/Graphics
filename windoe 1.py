import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos


# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 600, 200)

# make the context current
glfw.make_context_current(window)

vertices = [-0.1, -0.5, 0.0,
             0.5, -0.9, 0.0,
             0.0,  0.001, 0.1]

colors = [0.3, 0.0, 0.0,
          0.0, 0.2, 0.0,
          0.0, 0.0, 0.1]

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)

glClearColor(0.0, 0.2, 0.3, 0.001)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    ct = glfw.get_time()  # returns the elapsed time, since init was called

    glLoadIdentity()
    glScale((cos(ct)), abs(sin(ct)), 1)
    glRotatef(sin(ct) * 3, 0, 0, 1)
    glTranslatef(sin(ct),  sin(ct), 0)

    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()