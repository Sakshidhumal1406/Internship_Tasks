# Question 7: Alphabet Rangoli
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        s = "-".join(alphabet[size - 1:i:-1] + alphabet[i:size])
        lines.append(s.center(4 * size - 3, "-"))

    print("\n".join(lines[:0:-1] + lines))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)