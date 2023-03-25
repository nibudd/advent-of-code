from copy import deepcopy
from dataclasses import dataclass
from queue import LifoQueue
import re


with open("data/day5.txt", "r") as f:
    data = f.read().splitlines()

def parse_raw_data(data: list[str]) -> tuple[list[str]]:
    stack_data, move_data = [], []
    fill_stack = True
    for line in data:
        if line == "":
            fill_stack = False

        elif fill_stack:
            stack_data.append(line)

        else:
            move_data.append(line)

    return stack_data, move_data

def build_queues(stack_data: list[str]) -> list[LifoQueue]:
    stack_data = stack_data[:-1]
    stack_data.reverse()
    stack_height = len(stack_data)
    queue_count = (len(stack_data[0]) + 1) // 4
    queues = [LifoQueue(maxsize=stack_height*queue_count) for _ in range(queue_count)]

    for level in stack_data:
        for queue_num in range(queue_count):
            level_index = 1 + queue_num*4
            item = level[level_index]
            queue = queues[queue_num]
            if level[level_index] != " ":
                queue.put(item)

    return queues

def print_queues(queues: list[LifoQueue]) -> None:
    for queue in queues:
        while not queue.empty():
            print(queue.get())
        print() 

@dataclass
class Move:
    source: int
    target: int

def build_moves(move_data: list[str]) -> list[Move]:
    moves = []
    digits = re.compile(r"\d+")
    for move_str in move_data:
        count, source, target = digits.findall(move_str)
        moves.extend([Move(int(source), int(target))] * int(count))

    return moves

def run_moves(queues: list[LifoQueue], moves: list[Move]) -> list[LifoQueue]:
    for move in moves:
        queues[move.target-1].put(queues[move.source-1].get())

    return queues

def get_tops(queues: list[LifoQueue]) -> str:
    tops = []
    for queue in queues:
        if not queue.empty():
            tops.append(queue.get())

    return "".join(tops)

@dataclass
class Move9001:
    count: int
    source: int
    target: int

def build_moves_9001(move_data: list[str]) -> list[Move9001]:
    moves = []
    digits = re.compile(r"\d+")
    for move_str in move_data:
        count, source, target = digits.findall(move_str)
        moves.append(Move9001(int(count), int(source), int(target)))

    return moves

def run_moves_9001(queues: list[LifoQueue], moves: list[Move]) -> list[LifoQueue]:
    temp = LifoQueue()
    for move in moves:
        count = move.count
        source = queues[move.source-1]
        target = queues[move.target-1]
        for _ in range(count):
            temp.put(source.get())

        for _ in range(count):
            target.put(temp.get())

    return queues

stack_data, move_data = parse_raw_data(data)
queues = build_queues(stack_data)
moves = build_moves(move_data)
queues = run_moves(queues, moves)
tops = get_tops(queues)
print(tops)

stack_data, move_data = parse_raw_data(data)
queues = build_queues(stack_data)
moves = build_moves_9001(move_data)
queues = run_moves_9001(queues, moves)
tops = get_tops(queues)
print(tops)
