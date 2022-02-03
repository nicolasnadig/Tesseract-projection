import numpy as np
import time
import pygame
from graphics import *

#opening the window

WHITE =(255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("4D projection in pygame!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)


#np.array creates a matrix
#np.zero creates a matrix with only zeros
#np.identity creates identity matrix

def projection(A,dist):
    for i in range(0,16):
        factor = dist/(dist-A[i][3])
        for j in range(0,3):
            A[i][j]=factor*A[i][j]
        A[i][3]=0
    return A
def projection2(B,dist2):
    for i in range(0,16):
        factor = dist2/(dist2-B[i][2])
        for j in range(0,3):
            B[i][j]=factor*B[i][j]
        B[i][3]=0


def rotationx(A,increment):
    rot = np.identity(4)
    rot[1][1] = np.cos(increment)
    rot[1][2] = -np.sin(increment)
    rot[2][1] = np.sin(increment)
    rot[2][2] = np.cos(increment)
    return np.matmul(A,rot)
def rotationy(A,increment):
    rot = np.identity(4)
    rot[0][0] = np.cos(increment)
    rot[0][2] = np.sin(increment)
    rot[2][0] = -np.sin(increment)
    rot[2][2] = np.cos(increment)
    return np.matmul(A,rot)
def rotationz(A,increment):
    rot = np.identity(4)
    rot[0][0] = np.cos(increment)
    rot[0][1] = -np.sin(increment)
    rot[1][0] = np.sin(increment)
    rot[1][1] = np.cos(increment)
    return np.matmul(A,rot)

def rotationxy(A,increment):
    rot = np.identity(4)
    rot[0][0] = np.cos(increment)
    rot[0][1] = -np.sin(increment)
    rot[1][0] = np.sin(increment)
    rot[1][1] = np.cos(increment)
    return np.matmul(A,rot)
def rotationxz(A,increment):
    rot = np.identity(4)
    rot[0][0] = np.cos(increment)
    rot[0][2] = -np.sin(increment)
    rot[0][2] = np.sin(increment)
    rot[2][2] = np.cos(increment)
    return np.matmul(A,rot)
def rotationxw(A,increment):
    rot = np.identity(4)
    rot[0][0] = np.cos(increment)
    rot[0][3] = -np.sin(increment)
    rot[3][0] = np.sin(increment)
    rot[3][3] = np.cos(increment)
    return np.matmul(A,rot)
def rotationyz(A,increment):
    rot = np.identity(4)
    rot[1][1] = np.cos(increment)
    rot[1][2] = np.sin(increment)
    rot[2][1] = -np.sin(increment)
    rot[2][2] = np.cos(increment)
    return np.matmul(A,rot)
def rotationyw(A,increment):
    rot = np.identity(4)
    rot[1][1] = np.cos(increment)
    rot[1][3] = -np.sin(increment)
    rot[3][1] = np.sin(increment)
    rot[3][3] = np.cos(increment)  
    return np.matmul(A,rot)
def rotationzw(A,increment):
    rot = np.identity(4)
    rot[2][2] = np.cos(increment)
    rot[2][3] = -np.sin(increment)
    rot[3][2] = np.sin(increment)
    rot[3][3] = np.cos(increment)  
    return np.matmul(A,rot)

#def print(A):
    #blablabla


#dimension of cube
DimCube = 4
#number of vertices
vertices = 16
#define cube as matrix of its points as rows
cube = np.zeros((vertices,DimCube))
#initialize cube

counter=0
for i in range(1,3):
    for j in range(1,3):
        for s in range(1,3):
            for t in range(1,3):
                cube[counter][0] = (-1)**i
                cube[counter][1] = (-1)**j
                cube[counter][2] = (-1)**s
                cube[counter][3] = (-1)**t
                counter=counter+1
print(cube)
#Stereographic projection
#viewpoint
dist = 5
v = np.array([0,0,0,dist])

edges=np.zeros((64,2))
#find edges
same=0
edge=0
for i in range (16):
    for k in range (16):
        if cube[i,0] == cube[k,0]:
            same +=1
        if cube[i,1] == cube[k,1]:
            same +=1
        if cube[i,2] == cube[k,2]:
            same +=1
        if cube[i,3] == cube[k,3]:
            same +=1
        if same == 3:
            edges[edge,0]=i
            edges[edge,1]=k
            edge+=1
        same=0
print(edges)


CubeProjected = np.zeros((vertices,DimCube))
CubeProjected2 = np.zeros((vertices,DimCube))


clock = pygame.time.Clock()
#rotation
while True:

    cube = rotationxy(cube,0.01)
    cube = rotationzw(cube,0.01)
    
    
    #projection
    
    for i in range (16):
        for j in range (4):
            CubeProjected[i][j]= cube[i][j]
            
    projection(CubeProjected,dist)
    CubeProjected = rotationx(CubeProjected,-np.pi/2)
    
    
    for i in range (16):
        for j in range (4):
            CubeProjected2[i][j]= CubeProjected[i][j]
    #print()


    projection2(CubeProjected2,dist)
    
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    screen.fill(WHITE)
    for point in range (16):
        pygame.draw.circle(screen,BLACK , ((CubeProjected2[point,0]*100+WIDTH/2), (CubeProjected2[point,1]*100+HEIGHT/2)), 5)
    for j in range (64):
        startpoint=int(edges[j,0])
        
        endpoint=int(edges[j,1])
        
        pygame.draw.line(screen,BLACK, ((CubeProjected2[startpoint,0]*100+WIDTH/2), (CubeProjected2[startpoint,1]*100+HEIGHT/2)), ((CubeProjected2[endpoint,0]*100+WIDTH/2), (CubeProjected2[endpoint,1]*100+HEIGHT/2)) )
    pygame.display.update()




