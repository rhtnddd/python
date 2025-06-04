n=[]
while True:
    a=int(input())
    if a == 0:
        break
    n.append(a)
n.remove(3)
print(n)