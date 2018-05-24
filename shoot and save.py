from random import choice
import time
s_y = 0
s_c = 0
sleep_time=1
print 'input rounds number you wanna play\n'
k = raw_input()
for i in range(int(k)):
    if s_c==k:
        break
    print '\n=== round %d You kick! ===\n=== choice one side to shoot ===\n=== left,center,right ===' % (i+1)
    you = raw_input()
    print 'you kicked '+ you
    time.sleep(sleep_time)
    com= choice(['left','center','right'])
    print 'com saved '+com
    time.sleep(sleep_time)
    if you == com:
        print 'Oops...'
    else:
        print 'Goal !!!'
        s_y += 1
    time.sleep(sleep_time)
    print 'Score: %d(you) --- %d(com)' %(s_y,s_c)
    print '\n=== round %d You save! ===\n=== choice one side to save ===\n=== left,center,right ===' % (i+1)
    you = raw_input()
    time.sleep(sleep_time)
    print 'you saved '+ you
    com= choice(['left','center','right'])
    time.sleep(sleep_time)
    print 'com shoot '+com
    time.sleep(sleep_time)
    if you == com:
        print 'You Succeed !!!'
    else:
        print 'You Missed.'
        s_c += 1
    time.sleep(sleep_time)
    print 'Score: %d(you) --- %d(com)' %(s_y,s_c)
    
if s_y>s_c:
    print 'You Win !!! Score : %d --- %d' %(s_y,s_c)
else :
    if s_y<s_c:
        print ' You Lose !!! Score : %d --- %d' %(s_y,s_c)
    else:
        print 'It is a tie !!! Score : %d --- %d' %(s_y,s_c)