# Run main.py in python 3.6.5 myself
# Need pygame & tkinter

# Updates
## 18.9.17
### add ai : 
#### ai_num=0  P Vs P
#### ai_num=1  P Vs E
#### ai_num=2  E Vs E
### See Example_ai_1.png and Example_ai_2.png for new functions
![](https://raw.githubusercontent.com/yyhaos/PYTHON/master/五子棋/Example_ai_1.PNG)
![](https://raw.githubusercontent.com/yyhaos/PYTHON/master/五子棋/Example_ai_2.PNG)(E Vs E)
## 18.9.10
### add function ratract and restart and set (set the number of raws or lines and the least number of chessman needed to win).
### See Example.png and Example_2.png for new functions
![](https://raw.githubusercontent.com/yyhaos/PYTHON/master/五子棋/Example.PNG)
![](https://raw.githubusercontent.com/yyhaos/PYTHON/master/五子棋/Example_2.PNG)

# Problems :
### when using PyInstaller to package the main.py, the software size is about 667MB which is too huge.

### try to use " from ... import ...  " instead of just " import " , but it does not work. Still 667MB

### remove numpy and try " pyinstaller -F "  gets 225MB

# Going to do:
### 1 not need
a timer
### 2 Done
BGM & sound
### 3 Done
ai
### 4
Some titles
