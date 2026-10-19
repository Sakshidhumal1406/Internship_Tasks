# Question 6: Pangrams
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    if len(set(s.lower()) - {" "}) >= 26:
        return "pangram"
    else:
        return "not pangram"