# Question 12: Making Anagrams
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)

    total = 0

    for char in set(s1 + s2):
        total += abs(count1[char] - count2[char])

    return total