abc=[[1,2,3],[4,5,6],[7,8,9]]
for row in abc:
    print(row)
abc=[[1,2,3],[4,5,6],[7,8,9]]
for row in abc:
    print(row[0])
abc=[[1,2,3],[4,5,6],[7,8,9]]
for row in abc:
    for col in row:
        print(col, end='')
    print()

Scores = [[92,80,87],[94,82,86],[74,65,69],[87,89,81]]
m_total = 0
for row in Scores:
    m_total=m_total+row[0]
print(m_total)

Scores = [[92,80,87],[94,82,86],[74,65,69],[87,89,81]]
m_total = 0
for row in Scores:
    m_total=m_total+row[0]
avg = m_total/len(Scores)
print(avg)

Scores = [[92,80,87],[94,82,86],[74,65,69],[87,89,81]]
for row in Scores:
    s_total = 0
    for col in row:
        s_total=s_total+col
    print(s_total)

Scores = [[92,80,87],[94,82,86],[74,65,69],[87,89,81]]
for row in Scores:
    s_total = 0
    for col in row:
        s_total=s_total+col
    avg=s_total/3
    print(round(avg,2))

Scores = [['김정호',92,80,87],['박문수',94,82,86],['이사부',74,65,69],['장영실',87,89,81]]
for row in Scores:
    s_total = 0
    for i in range(1,4):
        s_total=s_total+row[i]
    avg=s_total/3
    print(row[0],round(avg,2))

medal=[[6,4,10],[38,32,19],[26,14,17]]
en=0
gm=0
do=0
for row in medal:
    en+=row[1]
    gm+=row[0]
    do+=row[2]
print("금:",gm)
print("은:",en)
print("동:",do)

medal=[["대한민국",6,4,10],['중국',38,32,19],['일본',26,14,17]]
for row in medal:
    sum=0
    for col in range(1,4):
        sum+=row[col]
    print(row[0],sum)

daylist = [[0,1,0,0,1],[0,0,1,0,0],[0,1,0,1,0],[0,0,0,1,0],[0,0,0,0,0]]
count=0
for col in daylist[2]:
        if col!=0:
            count+=1
print(count)

n=int(input())
daylist=[]
for i in range(n):
    att = input().split()
    daylist.append(att)
count=0
for row in daylist:
    for col in row:
        if col=='1':
            count+=1
print(count)