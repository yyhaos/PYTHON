# -*- coding: utf-8 -*-
"""
Spyder Editor
yyhs 
"""
from random import randint
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

#print(pygame.version.ver)
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
ai = 2  # ai is always the player 2 (play white)
ai2 = 0 # 0-ai_num=1  1-ai_num=2
exlen_ai = 22
xx=[0,-1,-1,-1,0,1,1,1]
yy=[1,1,0,-1,-1,-1,0,1]
    
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
    root.geometry('200x200')               
    l1 = Label(root, text="number of raw：")
    l1.pack()  
    xls_text = StringVar()
    xls = Entry(root, textvariable = xls_text)
    xls_text.set(" ")
    xls.pack()
    l2 = Label(root, text="number of line：")
    l2.pack()  
    sheet_text = StringVar()
    sheet = Entry(root, textvariable = sheet_text)
    sheet_text.set(" ")
    sheet.pack()
    l3 = Label(root, text="number of win：")
    l3.pack()  
    loop_text = StringVar()
    loop = Entry(root, textvariable = loop_text)
    loop_text.set(" ")
    loop.pack()
    l4 = Label(root, text="number of ai：")
    l4.pack()  
    aii_text = StringVar()
    aii = Entry(root, textvariable = aii_text)
    aii_text.set(" ")
    aii.pack()
    def on_click():
        x = xls_text.get()
        s = sheet_text.get()
        l = loop_text.get()
        a = aii_text.get()
        global num_line
        if s != ' ':
            num_line=int(s)
        global num_raw
        if x!=' ':
            num_raw=int(x)
        global num_win
        if l!=' ':
            num_win=int(l)
        global ai2,ai
        if a!=' ':
            global ai
            ai=int(a)
            if ai<=0:
                ai=0
                ai2=0
            else :
                if ai == 2:
                    ai2=1
                else:
                    ai=2
                    ai2=0
        if num_raw<=3:
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
    Button(root, text="confirm", command = on_click).pack()
    root.mainloop()

def ai_check(x,y,player,tar):
    #print(x,y,player)
    lens=[0]*10
    blocked=[0]*10
    for i in range(8):
        for k in range(num_win+2):
            tx = int(x + (k+1)*xx[i])
            ty = int(y + (k+1)*yy[i])
            #print(k,tx,ty)
            if x <=-1 or x >= num_line or y<=-1 or y >= num_raw:
                blocked[i]+=1
                break
            if tx >= 0 and tx <num_line and ty>=0 and ty < num_raw:
                if mymatrix[ty][tx] == player:
                    lens[i]+=1
                    continue
                if mymatrix[ty][tx] == 0:
                    break
                else :
                    blocked[i]+=1
                    break
            else:
                break
    for i in range(4):
        #print(lens[i]+lens[i+4])
        if lens[i]+lens[i+4]>=tar-1 and tar>=num_win:
            return player
        if lens[i]+lens[i+4]>=tar-1 and tar<num_win and blocked[i]==0:
            return player
    for i in range(4):
        #print(lens[i]+lens[i+4])
        if lens[i]+lens[i+4]>=tar-1 and tar>=num_win:
            return player
        if lens[i]+lens[i+4]>=tar-1 and tar<num_win and blocked[i]!=2:
            return player
    for i in range(4):
        #print(lens[i]+lens[i+4])
        if lens[i]+lens[i+4]>=tar-1 and tar>=num_win:
            return player
        if lens[i]+lens[i+4]>=tar-1 and tar<num_win :
            return player
    return 0

def ai_find(sx,sy):
    for tt in range(num_win+1):
        tmp=[]
        c=0
        tar=num_win-tt+1
        #print(tar)
        for i in range(num_win*2+exlen_ai):
            for j in range(num_win*2+exlen_ai):
                x=int(sx+num_win+exlen_ai/2-i)
                y=int(sy+num_win+exlen_ai/2-j)
                #print(x,y)
                global num_line
                global num_raw
                if x <=-1 or x >= num_line or y<=-1 or y >= num_raw:
                    continue
                if mymatrix[y][x]!=0:
                    continue
                if tar >= num_win-1:
                    if ai_check(x,y,ai,tar):
                        tmp.append((x,y))
                        c+=1
                else:
                    if ai_check(x,y,3-ai,tar):
                        tmp.append((x,y))
                        c+=1
        
        if c>0:
            #print( randint(0,c-1))
            return tmp[randint(0,c-1)]
        tmp=[]
        c=0
        for i in range(num_win*2+exlen_ai):
            for j in range(num_win*2+exlen_ai):
                x=int(sx-num_win-exlen_ai/2+i)
                y=int(sy-num_win-exlen_ai/2+j)
                if x <=-1 or x >= num_line or y<=-1 or y >= num_raw:
                    continue
                if mymatrix[y][x]!=0:
                    continue
                if tar >= num_win-1:
                    if ai_check(x,y,3-ai,tar):
                        tmp.append((x,y))
                        c+=1
                else:
                    if ai_check(x,y,ai,tar):
                        tmp.append((x,y))
                        c+=1
        if c>0:
            return tmp[ randint(0,c-1)]
    
    return (-1,-1)
                

while(True):
    initail()
    init()
    len_cm = int(size_check*len_check)
    len_aim = int(size_aim*len_check)
    global len_menu
    len_menu = int( (len_check*(num_raw-1) + 2*len_frame)*0.2 )
    
    maxn_x = len_check*(num_line-1) + 2*len_frame
    maxn_y = len_check*(num_raw-1) + 2*len_frame + len_menu
    
    screen = set_mode((maxn_x,maxn_y))
    set_caption("Wuziqi    Ver 0.3")
    
    background = load('resource/bg.jpg').convert_alpha()
    background = smoothscale(background,(maxn_x,maxn_y))
    bcm = load('resource/bcm.png').convert_alpha()
    bcm = smoothscale(bcm,(len_cm,len_cm))
    wcm = load('resource/wcm.png').convert_alpha()
    wcm = smoothscale(wcm,(len_cm,len_cm))
    
    aim = load('resource/aim_cm.png').convert_alpha()
    aim = smoothscale(aim,(len_aim,len_aim))
    
    p1w = load('resource/p1win.png').convert_alpha()
    w,h = p1w.get_size()
    h = int(maxn_x*size_win*h/w)
    w = int(maxn_x*size_win)
    p1w = smoothscale(p1w,(w,h))
    
    p2w = load('resource/p2win.png').convert_alpha()
    w,h = p2w.get_size()
    h = int(maxn_x*size_win*h/w)
    w = int(maxn_x*size_win)
    p2w = smoothscale(p2w,(w,h))
    
    sound = Sound('sound.wav') 
    sound.set_volume(1)
    BGM = Sound('BGM.wav')
    BGM.set_volume(0.3)
    
    button_restart = myButton('resource/red_cm.png','resource/blue_cm.png', (int(maxn_x/2),int(maxn_y-len_menu/2)))
    button_set = myButton('resource/red_cm_set.png','resource/blue_cm_set.png', (int(maxn_x/4),int(maxn_y-len_menu/2)))
    button_retract = myButton('resource/red_cm_retract.png','resource/blue_cm_retract.png', (int(3*maxn_x/4),int(maxn_y-len_menu/2)))
    
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
        
    #print("pos:",pos_line)
   # print(pos_raw)
        
    color_line = 0,0,0
    width_line = 3
    #premymatrix=[premymatrix,mymatrix]
    
    #mymatrix = zeros((num_raw,num_line))
    player = 1
    
    
    cnt=0   #cnt premymatrix
    ty=0
    tx=0
    flag=0  #1=p1 win   2=p2 win
    
    
    
    
    
    BGM.play()
    on=1
    
    reset=0
    
    if player == ai and flag==0 and ai2==0: #ai play first
        sound.play()
        #sleep(0.1)
        tx=int(num_raw/2)
        ty=int(num_line/2)
        mymatrix[ty][tx] = player
        premymatrix=premymatrix+[(ty,tx)]
        cnt+=1
        #print("premymatrix cnt=",cnt)
        #print(premymatrix)
        flag = check(tx,ty,player)
        player = 3 - player
    
    sx=int(num_raw/2)
    sy=int(num_line/2)
    #print("ai2=",ai2)
    if ai2==1:
        mymatrix[sy][sx] = player
        player=2
        tx,ty=(sx,sy)

    while True:
        if reset==1:
            break
        if player == ai and flag==0 and ai2==0: #ai play
            sleep(0.2)
            if cnt==0 :
                tx,ty=sx,sy
            else:
                tx,ty=ai_find(tx,ty)
            sound.play()
            #sleep(0.1)
            mymatrix[ty][tx] = player
            premymatrix=premymatrix+[(ty,tx)]
            cnt+=1
            #print("premymatrix cnt=",cnt)
            #print(premymatrix)
            flag = check(tx,ty,player)
            player = 3 - player
            mydraw(tx,ty,player)
        
        
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
                if ai2==1:
                    mymatrix[sy][sx] = 1
                    player=2
                    tx,ty=(sx,sy)
                continue
            if button_retract.isOver() and myevent.type == MOUSEBUTTONDOWN and cnt>0:
                tem=premymatrix[cnt-1]
                del premymatrix[cnt-1]
                
                #print(premymatrix)
                mymatrix[tem[0]][tem[1]]=0
                cnt-=1
                player=3-player
                if ai==player:
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
            if tx >=0 and tx < num_line and ty>=0 or ty < num_raw:
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
            if flag==0 and ai2>=1: #2 ai play
                #print(ai)
                sleep(0.02)
                tx,ty=ai_find(tx,ty) 
                #sound.play()
                mymatrix[ty][tx] = player
                premymatrix=premymatrix+[(ty,tx)]
                cnt+=1
                #print("premymatrix cnt=",cnt)
                #print(premymatrix)
                flag = check(tx,ty,player)
                player = 3 - player
                ai=3-ai    
                mydraw(sx,sy,player)
                break
            mydraw(tx,ty,player)
    
    
