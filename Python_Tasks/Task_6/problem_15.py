# Question 15: Set .difference() Operation
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
english_students = set(map(int, input().split()))

m = int(input())
french_students = set(map(int, input().split()))

result = english_students.difference(french_students)

print(len(result))