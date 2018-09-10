# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
from pygame import init
from pygame.display import set_mode
from pygame.display import set_caption
from pygame.display import update
from pygame.image import load
from pygame.transform import smoothscale
from pygame.event import get
from pygame import MOUSEBUTTONDOWN
from pygame import KEYDOWN
from pygame.draw import line
from pygame.mouse import get_pos
from pygame import QUIT
from pygame import quit
from pygame.mixer import Sound
from sys import exit
from time import sleep

len_check = 35
len_frame = 20
num_raw = 15
num_line = 15
num_win = 5
num_player = 2
size_check = 0.925
size_aim = 0.3
size_win = 0.8
size_menu = 0.95


class myButton(object):
    def __init__(self, upimage, downimage,position):
        self.imageUp = load(upimage).convert_alpha()
        global len_menu
        self.imageUp = smoothscale(self.imageUp,(int(len_menu*size_menu),int(len_menu*size_menu)))
        self.imageDown = load(downimage).convert_alpha()
        self.imageDown = smoothscale(self.imageDown,(int(len_menu*size_menu),int(len_menu*size_menu)))
        self.position = position

    def isOver(self):
        point_x,point_y = get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y

    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            screen.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))

def initail():
    global flag
    flag=0
    global cnt
    cnt=0
    global premymatrix
    premymatrix=[]
    global mymatrix
    mymatrix=[[0 for i in range(num_line+5)]for i in range(num_raw+5)]


def check(x,y,player):
    #print(x,y,player)
    lens=[0]*10
    for i in range(8):
        for k in range(num_win):
            tx = int(x + (k+1)*xx[i])
            ty = int(y + (k+1)*yy[i])
            #print(k,tx,ty)
            if tx >= 0 and tx <num_line and ty>=0 and ty < num_raw:
                if mymatrix[ty][tx] == player:
                    lens[i]+=1
                else:
                    break
            else:
                break
    for i in range(4):
        #print(lens[i]+lens[i+4])
        if lens[i]+lens[i+4]>=num_win-1.5:
            return player
    return 0

def mydraw(tx,ty,player):
    
    screen.blit(background,(0,0))
    for i in range(num_line):
        #print(i," ",num_raw-1)
        line(screen,color_line,(pos_line[i],pos_raw[0]),(pos_line[i],pos_raw[num_raw-1]),width_line)
    for i in range(num_raw):
        line(screen,color_line,(pos_line[0],pos_raw[i]),(pos_line[num_line-1],pos_raw[i]),width_line)
    for i in range(num_raw):
        for j in range(num_line):
            cm_y = i*len_check + len_frame - int(len_cm/2)
            cm_x = j*len_check + len_frame - int(len_cm/2)
            if mymatrix[i][j] == 1:
                screen.blit(bcm,(cm_x,cm_y))
            if mymatrix[i][j] == 2:
                screen.blit(wcm,(cm_x,cm_y))
    #screen.blit(wcm,(cm_x,cm_y))
    if tx < num_line and ty < num_raw and flag==0:
        if mymatrix[ty][tx] == 0:
            if player == 1:
                screen.blit(bcm,(tcm_x,tcm_y))
            if player == 2:
                screen.blit(wcm,(tcm_x,tcm_y))
            screen.blit(aim,(aim_x,aim_y))
    if flag == 1:
        screen.blit(p1w,(pos_win_y,pos_win_x))
    if flag == 2:
        screen.blit(p2w,(pos_win_y,pos_win_x))
    button_restart.render()
    button_set.render()
    button_retract.render()
    update()

def call_set():
    root = Tk()
    root.title("Set")
    root.wm_attributes('-topmost',1)
    root.geometry('200x200')                 #是x 不是*
    l1 = Label(root, text="number of raw：")
    l1.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    xls_text = StringVar()
    xls = Entry(root, textvariable = xls_text)
    xls_text.set(" ")
    xls.pack()
    l2 = Label(root, text="number of line：")
    l2.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    sheet_text = StringVar()
    sheet = Entry(root, textvariable = sheet_text)
    sheet_text.set(" ")
    sheet.pack()
    l3 = Label(root, text="number of win：")
    l3.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    loop_text = StringVar()
    loop = Entry(root, textvariable = loop_text)
    loop_text.set(" ")
    loop.pack()
    def on_click():
        x = xls_text.get()
        s = sheet_text.get()
        l = loop_text.get()
        #string = str("xls名：%s sheet名：%s 循环次数：%s  " %(x, s, l, ))
        global num_line
        num_line=int(s)
        global num_raw
        num_raw=int(x)
        global num_win
        num_win=int(l)
        if num_raw<=3 :
            num_raw=3
        if num_raw>51:
            num_raw=50
        if num_line<=3 :
            num_line=3
        if num_line>51:
            num_line=50
        global len_check
        len_check=int(600/(1+max(num_raw,num_line)))
        global len_frame
        len_frame=int(len_check*0.55)
        root.destroy()
        #print("xls名：%s sheet名：%s 循环次数：%s  " %(x, s, l, ))
        #messagebox.showinfo(title='aaa', message = string)
    Button(root, text="confirm", command = on_click).pack()
    root.mainloop()


while(True):
    init()
    len_cm = int(size_check*len_check)
    len_aim = int(size_aim*len_check)
    global len_menu
    len_menu = int( (len_check*(num_raw-1) + 2*len_frame)*0.2 )
    
    maxn_x = len_check*(num_line-1) + 2*len_frame
    maxn_y = len_check*(num_raw-1) + 2*len_frame + len_menu
    
    screen = set_mode((maxn_x,maxn_y))
    set_caption("Wuziqi    Ver 0.1")
    
    background = load('bg.jpg').convert_alpha()
    background = smoothscale(background,(maxn_x,maxn_y))
    bcm = load('bcm.png').convert_alpha()
    bcm = smoothscale(bcm,(len_cm,len_cm))
    wcm = load('wcm.png').convert_alpha()
    wcm = smoothscale(wcm,(len_cm,len_cm))
    
    aim = load('aim_cm.png').convert_alpha()
    aim = smoothscale(aim,(len_aim,len_aim))
    
    p1w = load('p1win.png').convert_alpha()
    w,h = p1w.get_size()
    h = int(maxn_x*size_win*h/w)
    w = int(maxn_x*size_win)
    p1w = smoothscale(p1w,(w,h))
    
    p2w = load('p2win.png').convert_alpha()
    w,h = p2w.get_size()
    h = int(maxn_x*size_win*h/w)
    w = int(maxn_x*size_win)
    p2w = smoothscale(p2w,(w,h))
    
    sound = Sound("sound.wav") 
    sound.set_volume(1)
    BGM = Sound("BGM.wav")
    BGM.set_volume(0.3)
    
    button_restart = myButton('red_cm.png','blue_cm.png', (int(maxn_x/2),int(maxn_y-len_menu/2)))
    button_set = myButton('red_cm_set.png','blue_cm_set.png', (int(maxn_x/4),int(maxn_y-len_menu/2)))
    button_retract = myButton('red_cm_retract.png','blue_cm_retract.png', (int(3*maxn_x/4),int(maxn_y-len_menu/2)))
    
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
        
    print("pos:",pos_line)
    print(pos_raw)
        
    color_line = 0,0,0
    width_line = 3
    #premymatrix=[premymatrix,mymatrix]
    
    #mymatrix = zeros((num_raw,num_line))
    player = 1
    xx=[0,-1,-1,-1,0,1,1,1]
    yy=[1,1,0,-1,-1,-1,0,1]
    
    cnt=0   #cnt premymatrix
    ty=0
    tx=0
    flag=0  #1=p1 win   2=p2 win
    
    
    
    
    initail()
    BGM.play()
    on=1
    
    reset=0
    while True:
        
        if reset==1:
            break
        x,y = get_pos()
        
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
        
        for myevent in get():
            if button_restart.isOver() and myevent.type == MOUSEBUTTONDOWN:
                initail()
                continue
            if button_retract.isOver() and myevent.type == MOUSEBUTTONDOWN and cnt>0:
                tem=premymatrix[cnt-1]
                del premymatrix[cnt-1]
                
                #print(premymatrix)
                mymatrix[tem[0]][tem[1]]=0
                cnt-=1
                player=3-player
               # premymatrix=premymatrix[1:cnt-1]
                continue
            if myevent.type == KEYDOWN:
                if on == 1:
                    BGM.stop()
                    on=0
                else :
                    BGM.play()
                    on=1
            if myevent.type == MOUSEBUTTONDOWN and flag>0:
                initail()
                continue
            if myevent.type == QUIT:
                initail()
                quit()
                exit()
            if myevent.type == MOUSEBUTTONDOWN and mymatrix[ty][tx]==0:
                sound.play()
                #sleep(0.1)
                mymatrix[ty][tx] = player
                premymatrix=premymatrix+[(ty,tx)]
                cnt+=1
                #print("premymatrix cnt=",cnt)
                #print(premymatrix)
                flag = check(tx,ty,player)
                player = 3 - player
                #print(flag)
            if button_set.isOver() and myevent.type == MOUSEBUTTONDOWN:
                call_set()
                #num_raw=20
                #num_line=20
                BGM.stop()
                reset=1
                #initail()
                #break
            if reset==1:
                break
            mydraw(tx,ty,player)
    
    
