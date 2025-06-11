num=list(map(int,input().split()))
sum=0
for i in num:
    if i%2==0:
        sum+=1
print(sum)