from typing import List


def group_count(relations: List[str]) -> int:
    n = len(relations)
    relatives = [[] for x in range(n)]

    for i, relation in enumerate(relations):
        for j, val in enumerate(relation):
            if i == j:
                continue

            if val == "1":
                min_index = min(i, j)
                max_index = max(i, j)

                if max_index not in relatives[min_index]:
                    relatives[min_index].append(max_index)

    groups = n
    for members in relatives:
        groups -= len(members)

    return groups
    