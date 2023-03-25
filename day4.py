with open("data/day4.txt", "r") as f:
    data = f.read().splitlines()

class Range:
    def __init__(self, low: int, high: int):
        self.low = low
        self.high = high

    def contains(self, r: "Range") -> bool:
        return self.low <= r.low and r.high <= self.high

    def overlaps(self, r: "Range") -> bool:
        return (
        self.low <= r.low <= self.high or
        self.low <= r.high <= self.high
    )

    def __repr__(self) -> str:
        return f"Range({self.low}, {self.high})"

def build_ranges(pair: str) -> list[Range]:
    str_ranges = pair.split(",")
    ranges = []
    for str_range in str_ranges:
        low, high = [int(x) for x in str_range.split("-")]
        ranges.append(Range(low, high))
    return ranges

range_pairs = [build_ranges((pair)) for pair in data]
contained = []
for range_pair in range_pairs:
    first, second = range_pair
    contained.append(first.contains(second) or second.contains(first))

print(sum(contained))

overlapped = []
for range_pair in range_pairs:
    first, second = range_pair
    overlapped.append(first.overlaps(second) or second.overlaps(first))

print(sum(overlapped))
