
def diagonaldifference(m):
    n = len(m)
    dp = 0
    ds = 0

    for i in range(n):
        dp += m[i][i]
        ds += m[i][n - i - 1]

    return abs(dp - ds)


if __name__ == '__main__':
    n = int(input())
    l = []

    for i in range(n):
        ll = input().split(' ')
        l.append([int(j) for j in ll])

    print(diagonaldifference(l))
