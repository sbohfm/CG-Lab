import math
from array import array
import ctypes

from OpenGL import GL

sphereIndexSize = 0
  
def sphere():
  
  global sphereIndexSize

  M, N = 100, 100

  posicao = array('f')
  textura = array('f')
  indices = array('H')
  normal = array('f')
  for i in range(M):
    u = i / (N - 1)
    for j in range(N):
      v = j / (M - 1)
      
      theta = (u * math.pi) - math.pi / 2
      phi = v * 2 * math.pi
      r1 = 2
      r2 = 1.9
      x = r1 * math.cos(theta) * math.cos(phi)
      y = r2 * math.sin(theta)
      z = r1 * math.cos(theta) * math.sin(phi)
  
      posicao.append(x)
      posicao.append(y)
      posicao.append(z)
      
      normal.append(x)
      normal.append(y)
      normal.append(z)
      
      # flip vertical
      textura.append(1 - v)
      textura.append(u)
      
      indices.append(i * M + j)
      indices.append((i + 1) * M + j)

  sphereIndexSize = len(indices)
  VAO = GL.glGenVertexArrays(1)

  GL.glBindVertexArray(VAO)
  GL.glEnableVertexAttribArray(0)  # posicao
  GL.glEnableVertexAttribArray(1)  # textura
  GL.glEnableVertexAttribArray(2)  # normal

  # VBO de posicao
  VBO_posicao = GL.glGenBuffers(1)
  GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_posicao)
  GL.glBufferData(GL.GL_ARRAY_BUFFER, len(posicao) * posicao.itemsize,
                  ctypes.c_void_p(posicao.buffer_info()[0]), GL.GL_STATIC_DRAW)
  GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, ctypes.c_void_p(0))

  # VBO de textura
  VBO_Textura = GL.glGenBuffers(1)
  GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_Textura)
  GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textura) * textura.itemsize,
                  ctypes.c_void_p(textura.buffer_info()[0]), GL.GL_STATIC_DRAW)
  GL.glVertexAttribPointer(1, 2, GL.GL_FLOAT, GL.GL_FALSE, 0, ctypes.c_void_p(0))

  # VBO de normal
  VBO_Normal = GL.glGenBuffers(1)
  GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_Normal)
  GL.glBufferData(GL.GL_ARRAY_BUFFER, len(normal) * normal.itemsize,
                  ctypes.c_void_p(normal.buffer_info()[0]), GL.GL_STATIC_DRAW)
  GL.glVertexAttribPointer(2, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, ctypes.c_void_p(0))

  # VBO de indices
  VBO_indice = GL.glGenBuffers(1)
  GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, VBO_indice)
  GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, len(indices) * indices.itemsize,
                  ctypes.c_void_p(indices.buffer_info()[0]), GL.GL_STATIC_DRAW)

  return VAO