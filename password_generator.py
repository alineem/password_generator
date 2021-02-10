import sys
import random


with open("wordlist", "r") as f:
    words = f.read().splitlines()

# print("Password generator")

length = int(sys.argv[1])

choices = random.sample(words, length)
password = ".".join(choices)
print(password)
