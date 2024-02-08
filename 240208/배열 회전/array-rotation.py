n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def rotate():
    check = min(n, m) // 2

    for cnt in range(check):
        n_max = n - cnt - 1
        m_max = m - cnt - 1

        tmp = matrix[cnt][cnt]

        for i in range(cnt, m_max):
            matrix[cnt][i] = matrix[cnt][i+1]
        
        for i in range(cnt, n_max):
            matrix[i][m_max] = matrix[i+1][m_max]

        for i in range(m_max, cnt, -1):
            matrix[n_max][i] = matrix[n_max][i-1]
        
        for i in range(n_max, cnt, -1):
            matrix[i][cnt] = matrix[i-1][cnt]

        matrix[cnt+1][cnt] = tmp

for _ in range(k):
    rotate()

for r in matrix:
    for n in r:
        print(n, end=' ')
    print()