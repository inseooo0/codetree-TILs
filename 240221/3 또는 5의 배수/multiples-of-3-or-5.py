def say(a, n):
    if a % n == 0:
        print('YES')
    else:
        print('NO')

a = int(input())

say(a, 3)
say(a, 5)