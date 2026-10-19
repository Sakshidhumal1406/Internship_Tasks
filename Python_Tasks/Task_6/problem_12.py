# Question 12: Set .discard(), .remove() & .pop()
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    for _ in range(int(input())):
        command = input().split()

        if command[0] == 'pop':
            s.pop()
        elif command[0] == 'remove':
            s.remove(int(command[1]))
        elif command[0] == 'discard':
            s.discard(int(command[1]))

    print(sum(s))