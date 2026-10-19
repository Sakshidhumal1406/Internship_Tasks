# Question 18: Set Mutations
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
set_a = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    operation, length = input().split()
    other_set = set(map(int, input().split()))

    if operation == "intersection_update":
        set_a.intersection_update(other_set)

    elif operation == "update":
        set_a.update(other_set)

    elif operation == "symmetric_difference_update":
        set_a.symmetric_difference_update(other_set)

    elif operation == "difference_update":
        set_a.difference_update(other_set)

print(sum(set_a))