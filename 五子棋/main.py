# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pygame import init
from pygame import display
from pygame import image 
from pygame import transform
from pygame import event
from pygame import MOUSEBUTTONDOWN
from pygame import KEYDOWN
from pygame import draw
from pygame import mouse
from pygame import QUIT
from pygame import quit
from pygame import mixer
from sys import exit
from time import sleep



len_check = 30
len_frame = 20
num_raw = 15
num_line = 15
num_win = 5
num_player = 2

size_check = 0.90
size_aim = 0.3
size_win = 0.8

len_cm = int(size_check*len_check)
len_aim = int(size_aim*len_check)
maxn_x = len_check*(num_line-1) + 2*len_frame
maxn_y = len_check*(num_raw-1) + 2*len_frame

init()
mixer.init()

screen = display.set_mode((maxn_x,maxn_y))
display.set_caption("Wuziqi    Ver 0.1")

background = image.load('bg.jpg').convert_alpha()
background = transform.smoothscale(background,(maxn_x,maxn_y))
bcm = image.load('bcm.png').convert_alpha()
bcm = transform.smoothscale(bcm,(len_cm,len_cm))
wcm = image.load('wcm.png').convert_alpha()
wcm = transform.smoothscale(wcm,(len_cm,len_cm))

aim = image.load('aim_cm.png').convert_alpha()
aim = transform.smoothscale(aim,(len_aim,len_aim))

p1w = image.load('p1win.png').convert_alpha()
w,h = p1w.get_size()
h = int(maxn_x*size_win*h/w)
w = int(maxn_x*size_win)
p1w = transform.smoothscale(p1w,(w,h))

p2w = image.load('p2win.png').convert_alpha()
w,h = p2w.get_size()
h = int(maxn_x*size_win*h/w)
w = int(maxn_x*size_win)
p2w = transform.smoothscale(p2w,(w,h))

sound = mixer.Sound("sound.wav") 
sound.set_volume(1)
BGM = mixer.Sound("BGM.wav")
BGM.set_volume(0.3)

pos_win_x = int(maxn_x*(1-size_win)/2)
#pos_win_x -= int(w/2)
pos_win_y = int(maxn_y*0.1)
#pos_win_y -= int(h/2)
tcm_x = 1
tcm_y = 1
pos_line=[]
pos_raw=[]
for i in range(num_line):
    pos_line = [len_frame+len_check*i for i in range(num_line)]
for i in range(num_raw):
    pos_raw = [len_frame+len_check*i for i in range(num_raw)]
    
color_line = 0,0,0
width_line = 3

matrix=[[0 for i in range(num_line+5)]for i in range(num_raw+5)]

#matrix = zeros((num_raw,num_line))

player = 1;
xx=[0,-1,-1,-1,0,1,1,1]
yy=[1,1,0,-1,-1,-1,0,1]


def check(x,y,player):
    print(x,y,player)
    lens=[0]*10
    for i in range(8):
        for k in range(8):
            tx = int(x + (k+1)*xx[i])
            ty = int(y + (k+1)*yy[i])
            print(k,tx,ty)
            if tx >= 0 and tx <num_line and ty>=0 and ty < num_raw:
                if matrix[ty][tx] == player:
                    lens[i]+=1
                else:
                    break
            else:
                break
    
    for i in range(4):
        print(lens[i]+lens[i+4])
        if lens[i]+lens[i+4]>=num_win-1.5:
            return player
    return 0

def mydraw(tx,ty,player):
    screen.blit(background,(0,0))
    for i in range(num_line):
        draw.line(screen,color_line,(pos_line[i],pos_raw[0]),(pos_line[i],pos_raw[num_raw-1]),width_line)
    for i in range(num_raw):
        draw.line(screen,color_line,(pos_line[0],pos_raw[i]),(pos_line[num_line-1],pos_raw[i]),width_line)
    for i in range(num_raw):
        for j in range(num_line):
            cm_y = i*len_check + len_frame - int(len_cm/2)
            cm_x = j*len_check + len_frame - int(len_cm/2)
            if matrix[i][j] == 1:
                screen.blit(bcm,(cm_x,cm_y))
            if matrix[i][j] == 2:
                screen.blit(wcm,(cm_x,cm_y))
    #screen.blit(wcm,(cm_x,cm_y))
    if tx < num_line and ty < num_raw and flag==0:
        if matrix[ty][tx] == 0:
            if player == 1:
                screen.blit(bcm,(tcm_x,tcm_y))
            if player == 2:
                screen.blit(wcm,(tcm_x,tcm_y))
            screen.blit(aim,(aim_x,aim_y))
    if flag == 1:
        screen.blit(p1w,(pos_win_y,pos_win_x))
    if flag == 2:
        screen.blit(p2w,(pos_win_y,pos_win_x))
    display.update()

ty=0
tx=0
flag=0

BGM.play()
on=1

while True:
    x,y = mouse.get_pos()
    
    tx = int((x-len_frame+len_check/2)/(len_check))
    ty = int((y-len_frame+len_check/2)/(len_check))
    
    rx = tx*len_check + len_frame
    ry = ty*len_check + len_frame
    
    tcm_x = rx - int(len_cm/2)
    tcm_y = ry - int(len_cm/2)
    
    aim_x = rx - int(len_aim/2)
    aim_y = ry - int(len_aim/2)
    
    x-=int(len_cm/2)
    y-=int(len_cm/2)
    
    for myevent in event.get():
        if myevent.type == KEYDOWN:
            if on == 1:
                BGM.stop()
                on=0
            else :
                BGM.play()
                on=1
        if myevent.type == MOUSEBUTTONDOWN and flag>0:
            flag=0
            matrix=[[0 for i in range(num_line+5)]for i in range(num_raw+5)]
            continue
        if myevent.type == QUIT:
            quit()
            exit()
        if myevent.type == MOUSEBUTTONDOWN and matrix[ty][tx]==0:
            sound.play()
            sleep(0.2)
            matrix[ty][tx] = player
            flag = check(tx,ty,player)
            player = 3 - player
            print(flag)
    mydraw(tx,ty,player)


