def find_duplicate(all_items: str) -> str:
    n = len(all_items) // 2
    first_items = {x for x in all_items[:n]}
    for item in all_items[n:]:
        if item in first_items:
            return item

def get_priority(letter: str) -> int:
    is_lower = letter == letter.lower()
    if is_lower:
        return ord(letter) - 96

    return ord(letter) - 38

with open("data/day3.txt", "r") as f:
    data = f.read().splitlines()

repeated_items = [find_duplicate(items) for items in data]
priorities = [get_priority(item) for item in repeated_items]
print(sum(priorities))

def find_badge(item_lists: list[str]) -> str:
    item_sets = [set(item_list) for item_list in item_lists]
    badge = set.intersection(*item_sets)
    return badge

badges = [find_badge(data[i:i+3]) for i in range(0, len(data), 3)]
priorities = [get_priority(badge.pop()) for badge in badges]
print(sum(priorities))
