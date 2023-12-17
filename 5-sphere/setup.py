from OpenGL import GL
from array import array
from PIL import Image
import os
import ctypes

import models, utils

# shaders path
path = os.path.dirname(os.path.abspath(__file__))
VERTEX_SHADER = open(path + '/shaders/vertexshader.txt').read()
FRAGMENT_SHADER = open(path + '/shaders/fragmentshader.txt').read()

# variaveis globais
progId = None
malhaVAO = None
projection_matrix = None


def compileshader():

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

  global progId, malhaVAO

  GL.glEnable(GL.GL_DEPTH_TEST)
  GL.glEnable(GL.GL_MULTISAMPLE)

  progId = compileshader()
  malhaVAO = models.sphere()

  GL.glUseProgram(progId)
  GL.glActiveTexture(GL.GL_TEXTURE0)

  utils.load_texture(path + '/textures/earth.jpg')
  GL.glUniform1i(GL.glGetUniformLocation(progId, "textureSlot"), 0)