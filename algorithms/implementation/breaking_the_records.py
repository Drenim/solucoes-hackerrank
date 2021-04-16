#!/bin/python3


def breakingRecords(score):
    higher = score[0]
    lower = score[0]

    high_records = 0
    low_records = 0

    for i in score:
        if i > higher:
            higher = i
            high_records += 1
        if i < lower:
            lower = i
            low_records += 1

    return high_records, low_records


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print(" ".join(map(str, result)))
