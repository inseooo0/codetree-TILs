a = int(input())
nums = list(map(int, input().split()))

def cp(a, b):
    if a > b:
        print('1')
    else:
        print('0')

for i in nums:
    cp(a, i)