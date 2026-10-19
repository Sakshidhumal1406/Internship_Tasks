# Question 16: Check Subset
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/py-check-subset/problem

T = int(input())

for _ in range(T):
    n = int(input())
    set_a = set(map(int, input().split()))

    m = int(input())
    set_b = set(map(int, input().split()))

    print(set_a.issubset(set_b))