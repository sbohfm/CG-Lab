import glm
import math
import ctypes
from array import array
from OpenGL import GL
from PIL import Image

import setup

a = 0

def load_texture(filename):
    im = Image.open(filename)
    w, h = im.size
    if(im.mode == "RGBA"):
        modo = GL.GL_RGBA
        data = im.tobytes("raw", "RGBA", 0, -1)
    else:
        modo = GL.GL_RGB
        data = im.tobytes("raw", "RGB", 0, -1)
    textureId = GL.glGenTextures(1)
    GL.glBindTexture(GL.GL_TEXTURE_2D, textureId)
    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, modo, w, h, 0, modo,GL. GL_UNSIGNED_BYTE, data)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
    return textureId

def draw():
    global a
    a += 0.0002

    GL.glClearColor(0.7, 0.9, 0.9, 1.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

    projection = glm.perspective(math.pi/4,800/600,0.1,100)
    # rotate cube on y axis only making a sinoidal movement going and back
    camera = glm.lookAt(glm.vec3(0,0,20),glm.vec3(0,0,0),glm.vec3(0,1,0)) # 
    model = glm.rotate(glm.mat4(1.0),a,glm.vec3(1,0.2,0.5))
    mvp = projection * camera * model

    GL.glBindVertexArray(setup.cuboVAO)
    GL.glUseProgram(setup.progId)
    GL.glUniformMatrix4fv(GL.glGetUniformLocation(setup.progId, "mvp"),1,GL.GL_FALSE,glm.value_ptr(mvp))
    GL.glDrawArrays(GL.GL_TRIANGLES,0,36)

    
