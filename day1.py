with open("data/day1.txt", "r") as f:
    data = f.read().splitlines()

calories = [0]
for calory in data:
    if calory != "":
        calories[-1] += int(calory)
    else:
        calories.append(0)

print(max(calories))

first, second, third = 0, 0, 0
for calory in calories:
    if calory > first:
        third = second
        second = first
        first = calory

    elif calory > second:
        third = second
        second = calory

    elif calory > third:
        third = calory

print(sum((first, second, third)))
