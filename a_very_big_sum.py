def sum(v):
    s = 0
    for i in v:
        s += i

    return s


if __name__ == '__main__':
    n = input()
    l = input().split(' ')
    l = [int(i) for i in l]
    print(sum(l))
