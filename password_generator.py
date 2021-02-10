import sys
import random

words = ["dog", "cat", "year", "python", "color", "phone", "park", "game", "horse", "beach", "travel", "correct", "battery", "staple"]

# print("Password generator")

length = int(sys.argv[1])

choices = random.sample(words, length)
password = ".".join(choices)
print(password)
