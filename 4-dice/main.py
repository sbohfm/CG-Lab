from OpenGL import GL
from array import array
import glfw
import os

import setup, utils

title = "\"Dirt\" - Dado c/ Texura | Nicole e Lucas"

# shaders path
path = os.path.dirname(os.path.abspath(__file__))
VERTEX_SHADER = open(path + "/shaders/vertexshader.txt").read()
FRAGMENT_SHADER = open(path + "/shaders/fragmentshader.txt").read()

def main():

    if not glfw.init():
        return

    # glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    # glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    # glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE)
    # glfw.window_hint(glfw.SAMPLES, 4)

    # create a window
    window = glfw.create_window(800, 600, title, None, None)

    # check if the window was created
    if not window:
        glfw.terminate()
        return
    
    # set the window as the current context
    glfw.make_context_current(window)

    setup.init()

    while not glfw.window_should_close(window):
        utils.draw()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
