import ctypes
import math

import glm
from OpenGL import GL
from PIL import Image

import setup, models

a = 0

def load_texture(filename):
  
  image = Image.open(filename)
  width, height = image.size
  image = image.tobytes("raw", "RGB", 0, -1)
  texture = GL.glGenTextures(1)
  
  GL.glBindTexture(GL.GL_TEXTURE_2D, texture)
  GL.glPixelStorei(GL.GL_UNPACK_ALIGNMENT, 1)
  
  GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB, width, height, 0, GL.GL_RGB, GL.GL_UNSIGNED_BYTE, image)
  
  GL.glGenerateMipmap(GL.GL_TEXTURE_2D)
  
  GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
  GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
  GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR_MIPMAP_LINEAR)
  GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
  
  return texture

def draw():
  
  global a
  a += 0.0001
  
  malhaVAO = setup.malhaVAO
  progId = setup.progId
  
  GL.glClearColor(0, 0, 0, 0)  # background
  GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

  projection = glm.perspective(math.pi / 4, 800 / 600, 0.1, 100)
  camera = glm.lookAt(glm.vec3(0, 0, 12), glm.vec3(0, 0, 0), glm.vec3(0.2, 1, 0)) # first param is the camera position, second is the point to look at, third is the up vector

  model = glm.rotate(a, glm.vec3(0, -1, 0))
  mvp = projection * camera * model

  GL.glBindVertexArray(malhaVAO)
  GL.glUseProgram(progId)
  GL.glUniformMatrix4fv(GL.glGetUniformLocation(progId, "mvp"), 1, GL.GL_FALSE, glm.value_ptr(mvp))
  GL.glUniformMatrix4fv(GL.glGetUniformLocation(progId, "model"), 1, GL.GL_FALSE, glm.value_ptr(model))
  GL.glDrawElements(GL.GL_TRIANGLE_STRIP, models.sphereIndexSize, GL.GL_UNSIGNED_SHORT, ctypes.c_void_p(0))

def color_map(u, v):
  r = u
  g = v
  b = 1 - u
  return r, g, b