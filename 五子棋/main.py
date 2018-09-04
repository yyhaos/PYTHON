# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pygame
#print(pygame.ver)
from sys import exit

len_check = 30
len_frame = 20
num_raw = 15
num_line = 15
num_win = 5
num_player = 2

size_check = 0.90
size_aim = 0.3

len_cm = int(size_check*len_check)
len_aim = int(size_aim*len_check)
maxn_x = len_check*(num_line-1) + 2*len_frame
maxn_y = len_check*(num_raw-1) + 2*len_frame

pygame.init()
screen = pygame.display.set_mode((maxn_x,maxn_y))
pygame.display.set_caption("Hello, World!")

background = pygame.image.load('bg.jpg').convert_alpha()
background = pygame.transform.smoothscale(background,(maxn_x,maxn_y))
bcm = pygame.image.load('bcm.png').convert_alpha()
bcm = pygame.transform.smoothscale(bcm,(len_cm,len_cm))
wcm = pygame.image.load('wcm.png').convert_alpha()
wcm = pygame.transform.smoothscale(wcm,(len_cm,len_cm))

aim = pygame.image.load('aim_cm.png').convert_alpha()
aim = pygame.transform.smoothscale(aim,(len_aim,len_aim))

pos_line = np.linspace(len_frame,len_frame+len_check*(num_line),num_line,endpoint=False)
pos_raw = np.linspace(len_frame,len_frame+len_check*(num_raw),num_raw,endpoint=False)

color_line = 0,0,0
width_line = 3

matrix = np.zeros((num_raw,num_line))

player = 1;


def draw(tx,ty):
    screen.blit(background,(0,0))
    for i in range(num_line):
        pygame.draw.line(screen,color_line,(pos_line[i],pos_raw[0]),(pos_line[i],pos_raw[num_raw-1]),width_line)
    for i in range(num_raw):
        pygame.draw.line(screen,color_line,(pos_line[0],pos_raw[i]),(pos_line[num_line-1],pos_raw[i]),width_line)
    for i in range(num_raw):
        for j in range(num_line):
            cm_x = i*len_check + len_frame - int(len_cm/2)
            cm_y = j*len_check + len_frame - int(len_cm/2)
            if matrix[i][j] == 1:
                screen.blit(bcm,(cm_x,cm_y))
            if matrix[i][j] == 2:
                screen.blit(wcm,(cm_x,cm_y))
    #screen.blit(wcm,(cm_x,cm_y))
    if tx < num_raw and ty < num_line and matrix[tx][ty] == 0:
        screen.blit(aim,(aim_x,aim_y))
    pygame.display.update()


while True:
    x,y = pygame.mouse.get_pos()
    
    tx = int((x-len_frame+len_check/2)/(len_check))
    ty = int((y-len_frame+len_check/2)/(len_check))
    
    rx = tx*len_check + len_frame
    ry = ty*len_check + len_frame
    
    cm_x = rx - int(len_cm/2)
    cm_y = ry - int(len_cm/2)
    
    aim_x = rx - int(len_aim/2)
    aim_y = ry - int(len_aim/2)
    
    x-=int(len_cm/2)
    y-=int(len_cm/2)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            matrix[tx][ty] = player;
            player = 3 - player;
    
    draw(tx,ty)
