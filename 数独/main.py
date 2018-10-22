# -*- coding: utf-8 -*-
"""
Spyder Editor
yyhs 
"""
from math import floor
from numpy import *
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
import random
import time

hard=0.8
len_check = 50
len_frame = 20
num_raw = 10
num_line = 10
num_player = 2
size_check = 0.925
size_aim = 0.3
size_win = 0.8
size_menu = 0.95
ai = 2  # ai is always the player 2 (play white)
ai2 = 0 # 0-ai_num=1  1-ai_num=2
exlen_ai = 22

class Sudoku:
	'''
	数独生成器类， 调用Sudoku实例的 make_digits() 方法，尝试生成数独
	但，数独生成是随机的，那么，可能会成功，也许会失败
	因此，make_digits() 方法的返回值代表生成数独是否成功
	如果 make_digits() 返回 True，那么可以使用实例的 digits 属性，里面有生成的新数独
	'''
	def __init__(self):
		'''
		digits 属性里面保存着当前的数独矩阵
		'''
		self.digits = [[] for i in range(9)]
	def make_digits(self):
		'''
		尝试生成数独，返回值代表生成是否成功
		'''
		#  数独矩阵的列数组，即9个竖行
		col_lists = [[] for i in range(9)]
		#  数独矩阵的区域数组，即九宫格的几个区域
		area_lists = [[] for i in range(3)]
		#  1 - 9 的随机排列
		nine = self.random_nine()
		for i in range(9):
			col_lists[i].append(nine[i])
		area_lists[0] = nine[0:3]
		area_lists[1] = nine[3:6]
		area_lists[2] = nine[6:]
		for i in range(8):
			nine = self.random_nine()
			#  九宫格的当前格已变换，重置当前格的数字
			if i % 3 == 2:
				area_lists[0] = []
				area_lists[1] = []
				area_lists[2] = []
			for j in range(9):
				area_index = j // 3
				count = 0
				error = False
				while nine[0] in col_lists[j] or nine[0] in area_lists[area_index]:
					count += 1
					if count >= len(nine):
						error = True
						break
					nine.append(nine.pop(0))
				if error:
					return False
				first = nine.pop(0)
				col_lists[j].append(first)
				area_lists[area_index].append(first)
		self.digits = col_lists
		return True
	def random_nine(self):
		'''
		1 - 9 的随机排列
		'''
		nine = [i + 1 for i in range(9)]
		for i in range(5):
			nine.append(nine.pop(random.randint(0, 8)))
		return nine
    
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
    sudoku = Sudoku()
    while not sudoku.make_digits():
        1
    #mymatrix=[[0] for i in range(9)]
    #mymatrix=hstack((mymatrix,sudoku.digits))
    #mymatrix=vstack(([0 for i in range(10)],mymatrix))
    mymatrix=sudoku.digits
    for i in range(9):
        for j in range(9):
            if random.uniform(0,1)>hard:
                mymatrix[i][j]=0
    
def mydraw(tx,ty,player):
    
    screen.blit(background,(0,0))
    
    for i in range(9):
        screen.blit(bt[i+1],(pos_raw[i],len_frame+len_check*num_line-len_check/1.5))
        
    for i in range(num_raw-1):
        for j in range(num_line-1):
            cm_y = i*len_check + len_frame + int(len_cm/18)
            cm_x = j*len_check + len_frame + int(len_cm/18)
            if mymatrix[i][j] >= 1:
                screen.blit(bt[mymatrix[i][j]],(cm_x,cm_y))
                if mymatrix[i][j]==now:
                    screen.blit(sel,(cm_x,cm_y))
    
    if tx < num_line-1 and ty < num_raw-1 and flag==0:
        #print(tx,ty)
        if mymatrix[ty][tx] == 0 and now>=1 and now<=9:
            screen.blit(bt[now],(tcm_x,tcm_y))
            
    for i in range(num_line):
        #print(i," ",num_raw-1)
        line(screen,color_line,(pos_line[i],pos_raw[0]),(pos_line[i],pos_raw[num_raw-1]),width_line)
        if(i%3==0):
            line(screen,(0,0,0),(pos_line[i],pos_raw[0]),(pos_line[i],pos_raw[num_raw-1]),width_line)
        
    for i in range(num_raw):
        line(screen,color_line,(pos_line[0],pos_raw[i]),(pos_line[num_line-1],pos_raw[i]),width_line)
        if(i%3==0 ):
            line(screen,(0,0,0),(pos_line[0],pos_raw[i]),(pos_line[num_line-1],pos_raw[i]),width_line)
            #screen.blit(aim,(aim_x,aim_y))
    #screen.blit(wcm,(cm_x,cm_y))
    
    button_restart.render()
    button_set.render()
    button_retract.render()
    update()

def ok(x,y,num):
    print(x,y,num)
    for i in range(9):
        if mymatrix[y][i]==num and x!=i:
            return False
        if mymatrix[i][x]==num and y!=i:
            return False
    xx=int (x/3.0)
    yy=int (y/3.0)
    #print(xx,yy)
    xx=xx*3
    yy=yy*3
    #print(xx,yy)
    for i in range(3):
        for j in range(3):
            if mymatrix[i+yy][j+xx]==num and (i+yy!=y or j+xx!=x):
                return False
    return True

def over():
    for i in range(9):
        for j in range(9):
            if mymatrix[i][j]==0:
                return False
    #Finish=[]
    global now
    now=0
    Finish=[[0,0],[1,1],[0,2],[2,1],[3,1],
           [3,3],[4,4],[3,5],[5,4],[6,4],
           [5,6],[6,6],[7,6],[8,6],[6,6],[6,7],[7,8],[8,8]]
    for i in range(9):
        for j in range(9):
            mymatrix[i][j]=0%10
    for i in Finish:
        sleep(0.15)
        mymatrix[i[0]][i[1]]=(4)%10
        mydraw(1,1,1)
    for i in Finish:
        sleep(0.1)
        mymatrix[i[0]][i[1]]=(0)%10
        mydraw(1,1,1)
    for th in range(10):
        if(th==4):
            continue
        sleep(0.5)
        for i in range(9):
            for j in range(9):
                mymatrix[i][j]=0
        for i in Finish:
            mymatrix[i[0]][i[1]]=(th+1)%10
        mydraw(1,1,1)
    global reset
    reset=1
    return True

def call_set():
    root = Tk()
    root.title("Set")
    root.wm_attributes('-topmost',1)
    root.geometry('200x200')               
    l1 = Label(root, text="Degree of difficulty(1~9)：")
    l1.pack()  
    xls_text = StringVar()
    xls = Entry(root, textvariable = xls_text)
    xls_text.set(" ")
    xls.pack()
    def on_click():
        x = xls_text.get()
        global hard
        #print(x)
        if x != ' ':
            hard=float(x)
        if hard<=2.0:
            hard=2.0
        if hard>9.5:
            hard=9.5
        hard=hard/10
        root.destroy()
    Button(root, text="confirm", command = on_click).pack()
    root.mainloop()
    
while(True):
    init()
    len_cm = int(size_check*len_check)
    len_aim = int(size_aim*len_check)
    global len_menu
    len_menu = int( (len_check*(num_raw-1) + 2*len_frame)*0.2 )
    
    maxn_x = len_check*(num_line-1) + 2*len_frame
    maxn_y = len_check*(num_raw-1) + 2*len_frame + len_menu + len_check
    
    screen = set_mode((maxn_x,maxn_y))
    set_caption("shudu    Ver 0.1")
    
    background = load('resource/bg.jpg').convert_alpha()
    background = smoothscale(background,(maxn_x,maxn_y))
    
    button_restart = myButton('resource/red_cm.png','resource/blue_cm.png', (int(maxn_x/2),int(maxn_y-len_menu/2)))
    button_set = myButton('resource/red_cm_set.png','resource/blue_cm_set.png', (int(maxn_x/4),int(maxn_y-len_menu/2)))
    button_retract = myButton('resource/red_cm_retract.png','resource/blue_cm_retract.png', (int(3*maxn_x/4),int(maxn_y-len_menu/2)))
    
    bt=['1']
    bt_name=['0','1','2','3','4','5','6','7','8','9']
    for i in range (1,10):
        #print(i)
        bt= bt+[load('resource/botton'+bt_name[i]+'.png').convert_alpha()]
        bt[i]= smoothscale(bt[i],(len_cm,len_cm))
    bt1 = bt[9]
    
    sel=load('resource/select.png').convert_alpha()
    sel = smoothscale(sel,(len_check,len_check))
    
    #bt2 = load('botton2.png').convert_alpha()
    
    pos_win_x = int(maxn_x*(1-size_win)/2)
    #pos_win_x -= int(w/2)
    pos_win_y = int(maxn_y*0.1)
    #pos_win_y -= int(h/2)
    tcm_x = 1
    tcm_y = 1
    pos_line=[]
    pos_raw=[]
    #for i in range(num_line):
    pos_line = [len_frame+len_check*i for i in range(num_line)]
    #for i in range(num_raw):
    pos_raw = [len_frame+len_check*i for i in range(num_raw)]
        
    
        
    #print("pos:",pos_line)
   # print(pos_raw)
        
    color_line =122,122,122
    width_line = 4
    #premymatrix=[premymatrix,mymatrix]
    
    #mymatrix = zeros((num_raw,num_line))
    player = 1
    xx=[0,-1,-1,-1,0,1,1,1]
    yy=[1,1,0,-1,-1,-1,0,1]
    
    cnt=0   #cnt premymatrix
    ty=0
    tx=0
    flag=0  #1=p1 win   2=p2 win
    
    
    
    now=0
    initail()
    on=1
    
    reset=0
    
    sx=int(num_raw/2)
    sy=int(num_line/2)
    #print("ai2=",ai2)

    while True:
        
        if reset==1:
            break
        x,y = get_pos()
        
        tx = int((x-len_frame)/(len_check))
        ty = int((y-len_frame)/(len_check))
        
        rx = tx*len_check + len_frame
        ry = ty*len_check + len_frame
        
        tcm_x = rx +int(len_check/18)
        tcm_y = ry +int(len_check/18)
        
        aim_x = rx - int(len_aim/2)
        aim_y = ry - int(len_aim/2)
        
        x-=int(len_cm/2)
        y-=int(len_cm/2)
        
        #now=0
        
        for myevent in get():
            over()
            if button_restart.isOver() and myevent.type == MOUSEBUTTONDOWN:
                initail()
                if ai2==1:
                    mymatrix[sy][sx] = 1
                    player=2
                    tx,ty=(sx,sy)
                continue
            if button_set.isOver() and myevent.type == MOUSEBUTTONDOWN:
                call_set()
                #num_raw=20
                #num_line=20
                #BGM.stop()
                reset=1
                #initail()
                #break
            if button_retract.isOver() and myevent.type == MOUSEBUTTONDOWN and cnt>0:
                tem=premymatrix[cnt-1]
                del premymatrix[cnt-1]
                #print(premymatrix)
                mymatrix[tem[0]][tem[1]]=0
                cnt-=1
               # premymatrix=premymatrix[1:cnt-1]
                continue
            if tx<9 and ty<9:
                if myevent.type == MOUSEBUTTONDOWN and mymatrix[ty][tx]==0:
                    #premymatrix=premymatrix+[(ty,tx)]
                    #cnt+=1
                    #if(y>=len_frame+len_check*num_line-len_check+5 and y<=len_frame+len_check*num_line+5):
                    #sound.play()
                    #sleep(0.1)
                    if(now>0 ):
                        if ok(tx,ty,now):
                            mymatrix[ty][tx] = now
                            premymatrix=premymatrix+[(ty,tx)]
                            cnt+=1
                        
                    #print("premymatrix cnt=",cnt)
                    #print(premymatrix)
                    #flag = check(tx,ty,player)
                    #player = 3 - player
                    #print(flag)
            if myevent.type == MOUSEBUTTONDOWN and y>=len_frame+len_check*num_line-len_check and y<=len_frame+len_check*num_line+5:
                #print(x,y,tx,now)
                now=tx+1
                #print(x,y,tx,now)
            if myevent.type == MOUSEBUTTONDOWN and flag>0:
                initail()
                continue
            if myevent.type == QUIT:
                initail()
                quit()
                exit()
            
            if reset==1:
                break
            
            mydraw(tx,ty,player)
    
    
