print("hello world")
print("hi")
print("hey")
print("bye")
import re
file_open=open("input.txt", 'rt')
content=file_open.read()
#print(len(content))
n = input()
t = re.findall(n, content, re.M|re.I)
i = 0
r = []
m=0
#print(len(t))
while i < len(t):
    if i == 0:
        f=re.search(t[i],content)
        i+=1
        k=f.span()
        m=k[1]
        r.append(content[k[0]-10:k[0]]+' '+n+' '+content[k[1]+1:k[1]+10])
    else:
        f=re.search(t[i],content[m+1:])
        i+=1
        k=f.span()
        m=k[1]
        r.append(content[k[0]-10:k[0]]+' '+n+' '+content[k[1]+1:k[1]+10])
ma=[]
ma.append(str(len(t)))
for y in range(1, len(r)+1):
    ma.append(str(y)+": "+r[y-1].strip())

#print(len(r))
#print(len(k))
#for s in range(len(r)):
    #print(str(s+1)+": ",r[s])
x = n+".txt"
with open(x,'a') as a:
    #a.writelines(str(len(t))
    a.writelines('\n'.join(ma))


    #k=re.search(n,content,re.M|re.I)
    #t=k.span()
    #print(t[1])
    #print(content[125:140])
    #print(k)i = 1
'''for n in t:
    print(str(i)+':',n)
    i+=1
print(len(t))'''
'''with open("out.txt", "a") as f:
    f.writelines('\n'.join(t))
    #f.write(t)'''

