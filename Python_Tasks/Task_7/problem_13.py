# Question 13: Sherlock and the Valid String
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

def isValid(s):
    freq = Counter(Counter(s).values())
    S
    if len(freq) == 1:
        return "YES"
    
    if len(freq) == 2:
        keys = list(freq.keys())
        
        if (keys[0] == 1 and freq[keys[0]] == 1) or (keys[1] == 1 and freq[keys[1]] == 1):
            return "YES"
        
        if abs(keys[0] - keys[1]) == 1:
            if (keys[0] > keys[1] and freq[keys[0]] == 1) or (keys[1] > keys[0] and freq[keys[1]] == 1):
                return "YES"
    
    return "NO"