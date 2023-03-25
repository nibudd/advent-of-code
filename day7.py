import json


with open("data/day7.txt", "r") as f:
    data = f.read().splitlines()

class Node:
    def __init__(self, name: str, size: int=0):
        self.name = name
        self.children = []
        self.parent = None
        self.size = size
        

    def add_node(self, node: "Node") -> None:
        node.parent = self
        self.children.append(node)

    @classmethod
    def from_ls(cls, first: str, second: str) -> "Node":
        if first == "dir":
            return cls(name=second)
        return cls(name=second, size=int(first))

    def __repr__(self):
        return f"Node(name='{self.name}', size={self.size}, children={[c.name for c in self.children]})"

def build_tree(data: list[str]) -> Node:
    root = None
    cwd = None
    for i, line in enumerate(data):
        if i == 0 and line == "$ cd /":
            root = Node(line[-1])
            cwd = root

        elif line == "$ cd ..":
            cwd = cwd.parent

        elif line.startswith("$ cd"):
            name = line.split(" ")[-1]
            for node in cwd.children:
                if node.name == name:
                    cwd = node        

        elif line == "$ ls":
            pass

        else:
            first, second = line.split(" ")
            cwd.add_node(Node.from_ls(first, second))

    return root

def print_tree(root: Node) -> None:
    to_visit = [root]
    for node in to_visit:
        to_visit.extend(node.children)
        print(node)

def update_sizes(node: Node) -> dict[str, int]:
    if node.size:
        return node.size

    sizes = [update_sizes(child) for child in node.children]
    node.size = sum(sizes)
    return node.size

def gather_dir_sizes(node: Node) -> list[int]:
    to_visit = [root]
    dir_sizes = []
    for node in to_visit:
        to_visit.extend(node.children)
        if node.children:
            dir_sizes.append(node.size)

    return dir_sizes
        

root = build_tree(data)
update_sizes(root)
dir_sizes = gather_dir_sizes(root)
small_sizes = [size for size in dir_sizes if size <= 100000]
print(sum(small_sizes))
root_size = max(dir_sizes)
disk_size = 70000000
free_space = disk_size - root_size
update_size = 30000000
space_needed = update_size - free_space
usable_sizes = [size for size in dir_sizes if size >= space_needed]
print(min(usable_sizes))
