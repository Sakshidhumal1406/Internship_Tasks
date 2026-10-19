# Question 2: The Captain's Room
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
room_numbers = list(map(int, input().split()))

rooms = set(room_numbers)
captain_room = (sum(rooms) * k - sum(room_numbers)) // (k - 1)

print(captain_room)