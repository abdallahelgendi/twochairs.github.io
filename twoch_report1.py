from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def myinit():                                 #for fixed things
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)


def drawchar(x,y,z):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(1, 0, 0)
    glTranslate(x, y, z)
    glTranslate(.5 * 3, -.5 * .5, .5 * 3)
    glScale(3, .5, 3)
    glutWireCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(1, 0, 0)
    glTranslate(x, y, z)
    glTranslate(.5 * 3, .5 * 3, .5 * .5)
    glScale(3, 3, .5)
    glutWireCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(1, 0, 0)
    glTranslate(x, y, z)
    glTranslate(2.75, -.5 * 3, .5 * .5)
    glScale(.5, 3, .5)
    glutWireCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(1, 0, 0)
    glTranslate(x, y, z)
    glTranslate(.25, -.5 * 3, .5 * .5)
    glScale(.5, 3, .5)
    glutWireCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(1, 0, 0)
    glTranslate(x, y, z)
    glTranslate(.25, -.5 * 3, 2.75)
    glScale(.5, 3, .5)
    glutWireCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(1, 0, 0)
    glTranslate(x, y, z)
    glTranslate(2.75, -.5 * 3, 2.75)
    glScale(.5, 3, .5)
    glutWireCube(1)
    glPopAttrib()
    glPopMatrix()


def draw1():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    drawchar(0,0,0)
    drawchar(6,0,0)
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Moving car")
    glutDisplayFunc(draw1)
    myinit()
    glutMainLoop()


main()