#import the glfw
import glfw
#Run Exception for initialization
if not glfw.init():
    raise Exception("glfw can't be initiated")

#Create window (width, height,Title, monitor, share )
window = glfw.create_window(1280, 720, "My OpenGLWindow",None,None)

#Run exception if window not created properly
if not window:
    glfw.terminate()
    raise Exception("glfw window can't be created")
#set window position
glfw.set_window_pos(window,400,200)
#Make context current
#Read about context here: https://open.gl/context
glfw.make_context_current(window)
#The main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()