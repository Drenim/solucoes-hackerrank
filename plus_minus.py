
def plus_minus(l):
    n = len(l)
    p, m, z = 0, 0, 0

    for i in l:
        if i > 0:
            p += 1
        elif i < 0:
            m += 1
        else:
            z += 1
    return (p / n, m / n, z / n)


if __name__ == '__main__':
    n = int(input())
    l = input().split(' ')
    l = [int(i) for i in l]

    for i in plus_minus(l):
        print(i)
