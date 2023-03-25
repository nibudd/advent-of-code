from dataclasses import dataclass
from queue import LifoQueue
import re


with open("data/day6.txt", "r") as f:
    data = f.read().splitlines()

def characters_are_different(text: str) -> bool:
    return len(text) == len(set(text))

def find_marker(line: str, characters: int) -> int:
    for i in range(characters, len(line)+1):
        sub = line[i-characters:i]
        if characters_are_different(sub):
            return i

for line in data:
    print(find_marker(line, 4))

for line in data:
    print(find_marker(line, 14))
