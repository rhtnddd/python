def avg(m,s,i):
    average=(m+s+i)/3
    return average

def sum(a,b):
    return a+b
print(sum(10,5))
mat = int(input('수학 점수 입력:'))
sci = int(input('과학 점수 입력:'))
info = int(input('정보 점수 입력:'))
result = avg(mat,sci,info)
print("평균:",result)