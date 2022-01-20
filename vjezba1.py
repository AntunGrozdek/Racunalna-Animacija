import math
import time
import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *

obj = open('medo.obj', 'r')
br_vrhova = 0
br_poligona = 0
koord_vrh = []
index_pol = []

for line in obj:
    if line.startswith('#'):
        continue
    values = line.split()
    if not values:
        continue

    if values[0] == 'v':
        br_vrhova += 1
        koord_vrh.append(values[1:4])

    if values[0] == 'f':
        temp = []
        br_poligona += 1
        for v in values[1:4]:
            temp.append(int(v) - 1)
        index_pol.append(temp)

R = []
V1 = [0, 0, 0]
V2 = [0, 10, 5]
V3 = [10, 10, 10]
V4 = [10, 0, 15]
V5 = [0, 0, 20]
V6 = [0, 10, 25]
V7 = [10, 10, 30]
V8 = [10, 0, 35]
V9 = [0, 0, 40]
V10 = [0, 10, 45]
V11 = [10, 10, 50]
V12 = [10, 0, 55]
R.append([V1, V2, V3, V4])
R.append([V2, V3, V4, V5])
R.append([V3, V4, V5, V6])
R.append([V4, V5, V6, V7])
R.append([V5, V6, V7, V8])
R.append([V6, V7, V8, V9])
R.append([V7, V8, V9, V10])
R.append([V8, V9, V10, V11])
R.append([V9, V10, V11, V12])

B = np.array([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 0, 3, 0], [1, 4, 1, 0]])
B_tan = np.array([[-1, 3, -3, 1], [2, -4, 2, 0], [-1, 0, 1, 0]])

p = []
p_new = []
p_tan = []
p_tan_new = []
os = []
os_new = []
kutevi = []
kutevi_new = []

for R_i in R:
    t = 0
    p_i = []
    p_i_tan = []
    os_i = []
    kutevi_i = []
    s = [0, 0, 1]
    while t < 1:
        T = np.array([t * t * t, t * t, t, 1])
        T2 = np.array([t*t, t, 1])
        p_i.append(np.matmul(np.matmul(np.dot(T, 1/6), B), R_i))
        p_i_tan.append(np.matmul(np.matmul(np.dot(T2, 1/2), B_tan), R_i))
        # print(p_i[-1][0])
        os_i.append([(s[1]*p_i[-1][2]) - (p_i[-1][1]*s[2]),
                     -((s[0]*p_i[-1][2]) - (p_i[-1][0]*s[2])),
                     (s[0]*p_i[-1][1]) - (s[1]*p_i[-1][0])])
        cos_p = (np.dot(s, p_i_tan[-1]))/(np.linalg.norm(s)*np.linalg.norm(p_i_tan[-1]))
        kut_p = np.arccos(cos_p)
        kutevi_i.append(math.degrees(np.arccos(cos_p)))
        t += 0.05
        s = [x + y for (x, y) in zip(p_i_tan[-1], p_i[-1])]
    p.append(p_i)
    p_tan.append(p_i_tan)
    os.append(os_i)
    kutevi.append(kutevi_i)

for i in p:
    for j in i:
        p_new.append(j)

for i in p_tan:
    for j in i:
        p_tan_new.append(j)

for i in os:
    pom = []
    for j in i:
        os_new.append(j)

for i in kutevi:
    for j in i:
        kutevi_new.append(j)


def spirala():
    glBegin(GL_LINE_STRIP)
    for i in p_new:
        glVertex3fv(list(i))
    glEnd()


def tangente():
    glBegin(GL_LINES)
    for i in range(0, len(p_tan_new), 1):
        glVertex3fv(list(p_new[i]))
        glVertex3fv([k+j for k, j in zip(list(p_tan_new[i]), list(p_new[i]))])
    glEnd()


def objekt(pomak):
    glPushMatrix()
    glTranslatef(p_new[pomak][0], p_new[pomak][1], p_new[pomak][2])
    glRotatef(kutevi_new[pomak], os_new[pomak][0], os_new[pomak][1], os_new[pomak][2])
    glBegin(GL_LINES)
    for pol in index_pol:
        for vrh in pol:
            glVertex3f(float(koord_vrh[vrh][0])/10, float(koord_vrh[vrh][1])/10, float(koord_vrh[vrh][2])/10)
    glEnd()
    glPopMatrix()


pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glLoadIdentity()
glMatrixMode(GL_MODELVIEW)
gluPerspective(40.0, display[0]/display[1], 0.1, 75.0)

glTranslatef(-25.0, 0.0, -75.0)

glRotatef(45, 0.5, 1, 0.5)

t = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    spirala()
    tangente()
    objekt(t)

    pygame.display.flip()
    pygame.time.wait(10)
    t += 1
    if t == 180:
        t = 0
