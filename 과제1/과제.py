weight=70
while weight>60:
    print("운동하자")
    weight-=1
print("목표 달성")

공사중='예'
while 공사중=='예':
    print('공사중')
    공사중=input("공사중입니까?(예/아니오)")
print("공사가 끝났네")

a=int(input('a:'))
while a >=0:
    print('실행')
    a=int(input('a:'))
print("정지")
a=5
while a >=0:
    print('실행')
    a=a-1
print('정지')
a=5
while a >=0:
    print('안녕하세요')
    a-=1
n=int(input('n:'))
while n>0:
    print('실행')
    n-=1
n=int(input('n:'))
while n>=0:
    print(n)
    n-=1
while 1:
    y=input("y 입력시 종료>")
    print(y)
    if y=='y':
        break
sum=0
a=1
while a<=10:
    sum=sum+a
    a+=1
print(sum)
sum=0
a=1
n=int(input("N값 입력:"))
while a<=n:
    sum=sum+a
    a+=1
print(sum)
a=1
while a<=100:
    if a%3==0:
        print("짝")
    else:
        print(a,end=' ')
    a=a+1
alist=[1,2,1,2]
while 2 in a:
    alist.remove(2)
    i
print(alist)

bts=['정국','뷔','지민','슈가','진','RM','제이홉']
i=0
while i<len(bts):
    print(bts[i])
    i+=1

dan=int(input("원하는 단은:"))
i=1
while i<10:
    print(dan,'*',i,'=',(dan*i))
    i+=1

import random
com = random.randint(1,100)
player=int(input("1부터 100사이의 숫자야 맞춰봐> "))
while com!=player:
    if com>player:
        print("up")
    else:
        print("down")
    player=int(input("1부터 100사이의 숫자야 맞춰봐> "))
print("정답!")

import random
import time
wlist=['cat','dog','fog','money','mouse','panda','frog','snake','wolf']
print('[타자게임]준비되면 엔터')
input()
start=time.time()
com=random.choice(wlist)
n=1
while n<=5:
    print(com)
    player=input()
    if com==player:
        print("통과!")
        n+=1
        com=random.choice(wlist)
    else:
        print('오타! 다시도전!')
end=time.time()
wt=end-start
print(f'타자시간:{wt:.2f} 초')