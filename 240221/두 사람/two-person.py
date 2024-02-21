def check(n, s):
    if n >= 19 and s == 'M':
        return True
    else:
        return False
flag = 0
for _ in range(2):
    n, s = input().split()
    n = int(n)
    if check(n, s):
        flag = 1
        break

if flag:
    print('1')
else:
    print('0')