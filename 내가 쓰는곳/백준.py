a=[]
for i in range(0,10):
    a.append(int(input()))
num=[]
sum=0
for i in a:
    if i%42 not in num:
        num.append(i%42)
        sum+=1
print(sum)