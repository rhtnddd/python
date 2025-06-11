f1 = open("복호화/암호표.txt", "r")
m = []
for i in range(3):
    m.append(list(f1.readline().split()))
f1.close()
print(m)

pw = input("암호문: ").split()
print("원문:", end=" ")
for n in range(0, len(pw), 2):
    r = int(pw[n])
    c = int(pw[n + 1])
    print(m[r][c], end="")
print()
