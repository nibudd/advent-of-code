choices = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2
}

def outcome(them: int, me: int) -> int:
    result = (me - them) % 3
    if result == 1:
        return 6
    if result == 2:
        return 0
    return 3

with open("data/day2.txt", "r") as f:
    data = f.read().splitlines()

matches = []
for match in data:
    them, me = match.split(" ")
    matches.append((choices[them], choices[me]))

def total_points(matches: list[tuple[int]]) -> int:
    points = [outcome(*match) + match[1] + 1 for match in matches]
    return sum(points)

print(total_points((matches)))

directions = {
    "X": 2,
    "Y": 0,
    "Z": 1
}

def my_choice(them: int, direction: int) -> int:
    return (them + direction) % 3

matches = []
for match in data:
    them, direction = match.split(" ")
    them = choices[them]
    direction = directions[direction]
    me = my_choice(them, direction)
    matches.append((them, me))

print(total_points((matches)))
