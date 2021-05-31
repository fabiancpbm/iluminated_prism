from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math

h = int (sys.argv[1]) if len(sys.argv) > 1 else 1.7

vertices = (
    (1, -1, -1),
    (-1, -1, -1),
    (-1, -1, 1),
    (1, h, -1),
    (-1, h, -1),
    (-1, h, 1)
)

faces = (
    (2, 0, 1),
    (3, 5, 4),
    (0, 2, 3),
    (5, 3, 2),
    (1, 4, 2),
    (5, 2, 4),
    (0, 3, 1),
    (4, 1, 3)
)

def calculaNormalFace(face):
    x = 0
    y = 1
    z = 2
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]
    U = ( (v2[x]-v0[x]), (v2[y]-v0[y]), (v2[z]-v0[z]))
    V = ( (v1[x]-v0[x]), (v1[y]-v0[y]), (v1[z]-v0[z]))
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return (N[x]/NLength, N[y]/NLength, N[z]/NLength)

def prism():
    glBegin(GL_TRIANGLES)
    for face in faces:
        normal = calculaNormalFace(face)
        glNormal3fv(normal)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(3, 2, 4, 0)
    prism()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

def reshape(w, h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0) # cor do objeto no escuro
    mat_diffuse = (0.0, 1.0, 0.0, 1.0) 
    mat_specular = (0.0, 1.0, 0.0, 1.0) # luz de frente
    mat_shininess = (50,)
    light_position = (.0, .0, 10.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Prisma")
    glutReshapeFunc(reshape)
    glutDisplayFunc(draw)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()