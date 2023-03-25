def max_frequency_deviation(s: str) -> int:
    n = len(s)
    max_deviation = 0

    for start in range(n):
        tallies = {}
        deviation = 0``
        for end in range(start, n):
            char = s[end]

            if char not in tallies.keys():
                tallies[char] = 0
            tallies[char] += 1

            deviation = max(tallies.values()) - min(tallies.values())
            if deviation > max_deviation:
                max_deviation = deviation

    return max_deviation
