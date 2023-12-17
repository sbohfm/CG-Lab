import glm
import math
import ctypes
from array import array
from OpenGL import GL

import setup

a = 0

def draw():
    global a
    a += 0.0005

    cuboVAO = setup.cuboVAO
    progId = setup.progId

    GL.glClearColor(0.0, 0.0, 0.0, 1.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    projection = glm.perspective(math.pi/4, 800/600, 0.1, 100)
    camera = glm.lookAt(glm.vec3(0, 2, 8), glm.vec3(
        0, 0, 0), glm.vec3(0, 1, 0))
    model = glm.rotate(a, glm.vec3(0, 1, 0))
    mvp = projection * camera * model

    GL.glBindVertexArray(cuboVAO)
    GL.glUseProgram(progId)
    GL.glUniformMatrix4fv(GL.glGetUniformLocation(
        progId, "mvp"), 1, GL.GL_FALSE, glm.value_ptr(mvp))
    GL.glDrawElements(GL.GL_TRIANGLES, 36,
                      GL.GL_UNSIGNED_SHORT, ctypes.c_void_p(0))

    