# Question 13: Nested Lists
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_lowest = sorted(set(
        score for name, score in records
    ))[1]

    names = sorted(
        name for name, score in records
        if score == second_lowest
    )

    for name in names:
        print(name)