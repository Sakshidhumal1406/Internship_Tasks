# Question 15: Collections - Counter
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter

if __name__ == '__main__':
    n = int(input())
    words = []

    for _ in range(n):
        words.append(input().strip())

    counts = Counter(words)

    print(len(counts))
    print(*counts.values())