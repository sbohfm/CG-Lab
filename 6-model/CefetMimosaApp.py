from numpy import indices
from GLAPP import GLAPP
from OpenGL import GL
import glm
import math
from CefetMimosa import *
a = 0

class CefetMimosaApp(GLAPP):

    def setup(self):
        # Window setup
        self.title("\"CEFET Mimosa\" - Modelo PLY | Nicole e Lucas")
        self.size(800,600)

        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)
        GL.glEnable(GL.GL_BLEND)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA);

        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("IntensityForBunny")
        GL.glUseProgram(self.pipeline)

        self.bunny = StanfordBunny()

    def draw(self):
        global a
        # clear screen and depth buffer
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        projection = glm.perspective(glm.radians(45),1,0.1,1000)
        camera = glm.lookAt(glm.vec3(0,0,200),glm.vec3(0,15,1),glm.vec3(0,1,0)) # eye, center, up
        model = glm.rotate(a,glm.vec3(0,1,0))
        mvp = projection * camera * model
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        self.bunny.draw()
        a += 0.0005

CefetMimosaApp()
