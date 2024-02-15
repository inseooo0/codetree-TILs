n, m = map(int, input().split())

nums = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        nums[b-1] = c
    elif a == 2:
        for i in range(b, c+1):
            if nums[i-1]:
                nums[i-1] = 0
            else:
                nums[i-1] = 1
    elif a == 3:
        for i in range(b, c+1):
            nums[i-1] = 0
    else:
        for i in range(b, c+1):
            nums[i-1] = 1

for i in nums:
    print(i, end=' ')