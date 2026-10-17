# Question 1: Find the Runner-Up Score
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(arr)
    unique_score = sorted(set(scores), reverse=True)

    print(unique_score[1])