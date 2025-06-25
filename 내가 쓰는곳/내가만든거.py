import math
ni,key=map(int,input().split())
sum=0
b=1
max=0
nikey=ni+key
oneofzero=[]
while nikey>=1:
    num=math. trunc(nikey%2)
    oneofzero.append(num)
    nikey/=2
oneofzero.reverse()
for i in oneofzero:
    if i==1:
        sum+=1
    else:
        if max<sum:
            max=sum
        sum=0
print(f'{max*13}%,{oneofzero[2]}')