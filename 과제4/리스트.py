# alist = [11,22,33,44]
# sum=0
# for i in alist:
#     sum+=i
# print(sum)

# a=["사과","바나나","포도","수박"]
# print(a[0:2])
# print(a[1:])
# print(a[1:3])
# print(a)

# friend=[]
# name=input('친구 이름 입력: ')
# friend.append(name)
# name=input('친구 이름 입력: ')
# friend.append(name)
# name=input('친구 이름 입력: ')
# friend.append(name)
# name=input('친구 이름 입력: ')
# friend.append(name)
# name=input('친구 이름 입력: ')
# friend.append(name)
# print(friend)

# menu=[]
# menu.append("치킨")
# menu.append("피자")
# menu.append("샐러드")
# menu.append("스테이크")
# print(menu)

# menu=[]
# menu.append("치킨")
# menu.append("피자")
# menu.append("샐러드")
# menu.append("스테이크")
# print(menu)
# menu.remove("스테이크")
# menu.append("감자튀김")
# print("변경=>",menu)

# menu=[]
# menu.append("치킨")
# menu.append("피자")
# menu.append("샐러드")
# menu.append("스테이크")
# print(menu)
# menu.remove("스테이크")
# menu.append("감자튀김")
# print("변경=>",menu)
# menu.remove('샐러드')
# print("삭제=>",menu)
# print("샐러드 매뉴가 삭제 되었습니다.")

# import random
# number = [10, 20,33,40,55,60,77,80,90,100]
# num1=number[random.randrange(1,10)]
# num2=number[random.randrange(1,10)]
# a=int(input(f"{num1} + {num2} = ?"))
# if a==num1+num2:
#     print("맞았습니다.")
# else:
#     print("틀렸습니다.")

# a=[7,6,5,4]
# b=[1,2,3]
# print(b+a)
# print(a+b*2)
# print(b[0:2]+a[0:2]*3)

# a=[1,2,3,4,5]
# if 1 in a:
#     print('1이 존재 합니다.')
# else:
#     print('1이 존재하지 않습니다.')

# a=[1,2,3,4,5]
# if 0 not in a:
#     print('0이 존재하지 않습니다.')
# else:
#     print('0이 존재 합니다.')

# import random
# alist = []
# num = random.randint(1,100)
# for i in range (5):
#     alist.append(num)
#     num = random.randint(1,100)
# if 50 in alist:
#     print("50이 존재 합니다.")
# else:
#     print("50이 존재하지 않습니다.")
# print("리스트 숫자:",alist)