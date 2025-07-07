n=int(input())
daylist=[]
for i in range(n):
    att = input().split()
    daylist.append(att)

count=0
for i in daylist:
    for j in i:
        if j=='1':
            count+=1
print(count)


jumin = input("주민등록번호 입력> ")

year = int(jumin[0:2])
gender_code = jumin[7]

if gender_code == '1' or gender_code == '2':
    year += 1900
elif gender_code == '3' or gender_code == '4':
    year += 2000

if gender_code == '1' or gender_code == '3':
    gender = "남자"
elif gender_code == '2' or gender_code == '4':
    gender = "여자"

print(f"{year}년 태어난 {gender}입니다.")