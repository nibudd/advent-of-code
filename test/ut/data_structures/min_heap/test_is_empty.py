from data_structures.min_heap import MinHeap


def test_instantiation_creates_empty_min_heap():
    min_heap = MinHeap()
    assert min_heap.is_empty()


def test_adding_node_makes_min_heap_not_empty():
    min_heap = MinHeap()
    min_heap.push(1)
    min_heap.is_empty() == False


def test_returns_false_after_emptying_heap():
    min_heap = MinHeap()
    min_heap.push(3)
    min_heap.push(2)
    min_heap.push(1)

    min_heap.pop()
    min_heap.pop()
    min_heap.pop()

    assert min_heap.is_empty()