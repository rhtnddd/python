# 1113
# a,b=input().split()
# print(b,a)

# 1114
# a,b=input().split()
# print(int(b)+int(a))

# 1115
# a,b=input().split()
# print(int(b)+int(a))

# 1116
# a,b=input().split()
# print(f'{a}+{b}={int(a)+int(b)}')
# print(f'{a}-{b}={int(a)-int(b)}')
# print(f'{a}*{b}={int(a)*int(b)}')
# print(f'{a}/{b}={int(a)//int(b)}')

# 1117
# a,b=input().split()
# print(round(float(a)*float(b),2))

# 1118
# a,b=input().split()
# print(round(float(a)*float(b)/2,1))

# 1119
# a=input()
# print(int(a)*24)

# 1120
# a,b,c=map(int,input().split())
# print(f"{(a+b+c)/3:.2f}")

# 1121
# a,b=map(int,input().split())
# print(a%b)

# 1122
# a=int(input())
# print(a//60,a%60)

# 1123
# a=int(input())
# print(f"{9/5*a+32:.3f}")

# 1125
# a=int(input())
# print("%o %X"%(a,a))

# 1131
# a=input()
# print(a)

# 1132
# a=input()
# print(a)

# 1133
# a=input()
# print(a)

# 1135
# a,b=map(int,input().split())
# print((a>=b)*1)

# 1495
# a,b,c=map(int,input().split())
# n = [[0] * b for _ in range(a)]
# s = [[0] * b for _ in range(a)]
# for i in range(c):
#     x1,y1,x2,y2,u=map(int,input().split())
#     n[x1][y1] += u
#     if x2 + 1 < a and y2 + 1 < b:
#         n[x2+1][y2+1] = n[x2+1][y2+1]+u
#     if y2 + 1 < b:
#         n[x1][y2+1] = n[x1][y2+1]-u
#     if x2 + 1 < a:
#         n[x2+1][y1] = n[x2+1][y1]-u
# for i in range(a):
#     for j in range(b):
#         print(n[i][j],end=' ')
#     print()

# for i in range(a):
#     for j in range(b):
#         s[i][j] = n[i][j]
#         if i > 0:
#             s[i][j] += s[i-1][j]
#         if j > 0:
#             s[i][j] += s[i][j-1]
#         if i > 0 and j > 0:
#             s[i][j] -= s[i-1][j-1]
# print()
# for i in range(a):
#     for j in range(b):
#         print(s[i][j],end=' ')
#     print()
# 1138
# a=int(input())
# print((not a)*1)
# 1139
# a,b=map(int,input().split())
# print((a and b)*1)
# 1140
# a,b=map(int,input().split())
# print((a or b)*1)
# 1143
# a, b = map(int, input().split())
# print(a & b)
# 1144
# a, b = map(int, input().split())
# print(a | b)
# 1147
# a, b = map(int, input().split())
# print(a << b)
# 1148
# a, b = map(int, input().split())
# print(a >> b)
# 1149
# a,b=map(int,input().split())
# print(a if a > b else b)
# 1150
# a, b, c = map(int, input().split())
# print(min(a, b, c))
# 1151
# a=int(input())
# if a<10:
#     print("small")
# 1152
# a=int(input())
# if a<10:
#     print("small")
# else:
#     print("big")
# 1153
# a,b=map(int,input().split())
# if a < b:
# 	print("<")
# if a > b:
# 	print(">")
# if a == b:
# 		print("=")
# 1154
# a,b=map(int,input().split())
# print(max(a,b)-min(a,b))
# 1155
# a=int(input())
# if a%7==0:
#     print("multiple")
# else:
#     print("not multiple")
# 1156
# a=int(input())
# if a%2==0:
#     print("even")
# else:
#     print("odd")
# 1157
# a=float(input())
# if 50<=a and a<=60:
#     print("win")
# else:
#     print("lose")
# 1158
# a=int(input())
# if 30<=a and a<=40:
#     print("win")
# elif 60<=a and a<=70:
#     print("win")
# else:
#     print("lose")
# 1159
# a=int(input())
# if 50<=a and a<=70:
#     print("win")
# elif a%6==0:
#     print("win")
# else:
#     print("lose")
# 1160
# a=int(input())
# if a==1 or a==3 or a==5 or a==7:
#     print("oh my god")
# else:
#     print("enjoy")
# 1161
# a, b = map(int, input().split())

# if a % 2 == 0:
#     if b % 2 == 0:
#         print("짝수+짝수=짝수")
#     else:
#         print("짝수+홀수=홀수")
# else:
#     if b % 2 == 0:
#         print("홀수+짝수=홀수")
#     else:
#         print("홀수+홀수=짝수")
# 1162
# y, m, c = map(int, input().split())

# if (y - m + c) % 10 == 0:
#     print("대박")
# else:
#     print("그럭저럭")
# 1163
a, b, c = map(int, input().split())

if ((a + b + c) // 100) % 2 == 0:
    print("대박")
else:
    print("그럭저럭")