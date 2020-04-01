f = open('mydata.txt','r',encoding= 'utf-8 ')
data = f.read()
oa = ord('a')
oz = ord('z')
oA = ord('A')
oZ = ord('Z')
used = [0 for x in range(0, 1000000)]
k = []
s=[]
f2=open('字.txt','w',encoding= 'utf-8 ')
#s = {'wxid_rtxnj61vkzml12':'吕文昊','wxid_61vb22e6fhok32':'时光','wxid_5ou2qze5dp2l22':'肖恺','wxid_9835058350711':'都建祥','wxid_lya3xhon9t3e22':'段宇飞'}
for x in data :
    a = ord(x)
    if(x==';' or x=='&'or x=='@'or x==']'or x=='['or x=='/' or x=='='or x=='-' or x==' 'or x=='。' or x=='？'or x=='！' or x=='，' or x=='!' or x=='\n' or x=='：'  or x=='?'  or x=='.'or x=='《' or x=='》' or x=='；' or x=='(' or x==')' or x=='_' or x=='"' or x=='"' or x==':' or x=='）' or x=='<' or x=='>'):  
        continue
    if a >= oa and a <= oz :
        continue
    if a >=oA and a <= oZ :
        continue
    if x>='0' and x<='9':
        continue
    used[a]+=1
for x in data :
    a = ord(x)
    if(x=='@'or x=='\t'or x==']'or x=='['or x=='/' or x=='='or x=='-' or x==' 'or x=='。' or x=='？'or x=='！' or x=='，' or x=='!' or x=='\n' or x=='：'  or x=='?'  or x=='.'or x=='《' or x=='》' or x=='；' or x=='(' or x==')' or x=='_' or x=='"' or x=='"' or x==':' or x=='）' or x=='<' or x=='>'):  
        continue
    if a >= oa and a <= oz :
        continue
    if a >=oA and a <= oZ :
        continue
    if x>='0' and x<='9':
        continue
    if a>=ord('\U0001f001'):
        continue
    s.append(x)
    f2.write(x)
    if used[a]>50:
       # print(x ,used[a])
        k.append([used[a],x])
        used[a]=-1
k.sort()
k.reverse()
print (s)
#for i in k :
#    print (i[1],i[0])
