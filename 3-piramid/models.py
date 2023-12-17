import ctypes
import OpenGL.GL as GL
from array import array

def cubo():
    
    A = (-1.0, -1.0,  1.0)
    B = ( 1.0, -1.0,  1.0)
    C = ( 1.0, -1.0, -1.0)
    D = (-1.0, -1.0, -1.0)
    E = ( 0.0,  1.0,  0.0)
    
    posicao = array('f', [
        *A, *B, *C, *D, *E
    ])
    
    cor = array('f', [
        1.0, 0.0, 0.0,  # A
        1.0, 1.0, 0.0,  # B
        0.0, 1.0, 0.0,  # C
        0.0, 1.0, 1.0,  # D
        0.0, 0.0, 1.0,  # E
    ])
    
    indices = array('H', [
        0, 4, 1, 1, 4, 2,
        2, 4, 3, 3, 4, 0,
        0, 3, 2, 0, 2, 1
    ])
    
    VAO = GL.glGenVertexArrays(1)
    
    GL.glBindVertexArray(VAO)
    GL.glEnableVertexAttribArray(0)  # posicao
    GL.glEnableVertexAttribArray(1)  # cor
    
    # VBO de posicao
    VBO_posicao = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_posicao)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, len(posicao)*posicao.itemsize,
                    ctypes.c_void_p(posicao.buffer_info()[0]), GL.GL_STATIC_DRAW)
    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, ctypes.c_void_p(0))
    
    # VBO de cor
    VBO_cor = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_cor)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, len(cor)*cor.itemsize,
                    ctypes.c_void_p(cor.buffer_info()[0]), GL.GL_STATIC_DRAW)
    GL.glVertexAttribPointer(1, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, ctypes.c_void_p(0))
    
    # VBO de indice
    VBO_indice = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, VBO_indice)
    GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, len(indices)*indices.itemsize,
                    ctypes.c_void_p(indices.buffer_info()[0]), GL.GL_STATIC_DRAW)
    
    return VAO