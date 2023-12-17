import OpenGL.GL as GL
import os

import models, utils

path = os.path.dirname(os.path.abspath(__file__))
VERTEX_SHADER = open(path + "/shaders/vertexshader.txt").read()
FRAGMENT_SHADER = open(path + "/shaders/fragmentshader.txt").read()

progId = None
cuboVAO = None

def compileshaders():

    progId = GL.glCreateProgram()

    for type, source in [(GL.GL_VERTEX_SHADER, VERTEX_SHADER), (GL.GL_FRAGMENT_SHADER, FRAGMENT_SHADER)]:

        # create shader
        shaderId = GL.glCreateShader(type)
        GL.glShaderSource(shaderId, [source])
        GL.glCompileShader(shaderId)
        
        GL.glAttachShader(progId, shaderId)

    GL.glLinkProgram(progId)
    return progId

def init():
    global progId, cuboVAO
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_MULTISAMPLE)
    progId = compileshaders()
    cuboVAO = models.cubo()
    GL.glUseProgram(progId)
    GL.glActiveTexture(GL.GL_TEXTURE0)
    utils.load_texture("./textures/dirt-block.jpg")
    GL.glUniform1i(GL.glGetUniformLocation(progId, "textureSlot"),0)