import ctypes
import OpenGL.GL as GL
from array import array

def cubo():

    A = (1.0, -1.0,  1.0)
    B = (1.0, 1.0,  1.0)
    C = (-1.0,  1.0,  1.0)
    D = (-1.0,  -1.0,  1.0)
    E = (1.0, -1.0, -1.0)
    F = (1.0, 1.0, -1.0)
    G = (-1.0,  1.0, -1.0)
    H = (-1.0,  -1.0, -1.0)

    posicao = array('f',[
        *A,*B,*D,*D,*B,*C, # f1 - frente
        *E,*F,*A,*A,*F,*B, # f2 - direita
        *H,*G,*E,*E,*G,*F, # f3 - tras
        *D,*C,*H,*H,*C,*G, # f4 - esquerda
        *B,*F,*C,*C,*F,*G, # f5 - cima
        *A,*E,*D,*D,*E,*H  # f6 - baixo
    ])
    
    f1 = (0/4, 1/3,     0/4, 2/3,       1/4, 1/3,       1/4, 1/3,       0/4, 2/3,       1/4, 2/3)
    f2 = (1/4, 1/3,     1/4, 2/3,       2/4, 1/3,       2/4, 1/3,       1/4, 2/3,       2/4, 2/3)
    f3 = (2/4, 1/3,     2/4, 2/3,       3/4, 1/3,       3/4, 1/3,       2/4, 2/3,       3/4, 2/3)
    f4 = (3/4, 1/3,     3/4, 2/3,       4/4, 1/3,       4/4, 1/3,       3/4, 2/3,       4/4, 2/3)
    
    f5 = (1/4, 2/3,     1/4, 3/3,       2/4, 2/3,       2/4, 2/3,       1/4, 3/3,       2/4, 3/3)
    f6 = (1/4, 0/3,     1/4, 1/3,       2/4, 0/3,       2/4, 0/3,       1/4, 1/3,       2/4, 1/3)

    texture = array('f',[
        *f1,
        *f2,
        *f3,
        *f4,
        *f5,
        *f6
    ])


    VAO = GL.glGenVertexArrays(1)
    
    GL.glBindVertexArray(VAO)
    GL.glEnableVertexAttribArray(0) # posicao
    GL.glEnableVertexAttribArray(1) # cor

    # VBO de posicao
    VBO_posicao = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_posicao)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, len(posicao)*posicao.itemsize,
                    ctypes.c_void_p(posicao.buffer_info()[0]), GL.GL_STATIC_DRAW)
    GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

    # VBO de textura
    VBO_textura = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO_textura)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, len(texture)*texture.itemsize,
                    ctypes.c_void_p(texture.buffer_info()[0]), GL.GL_STATIC_DRAW)
    GL.glVertexAttribPointer(1,2,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

    return VAO