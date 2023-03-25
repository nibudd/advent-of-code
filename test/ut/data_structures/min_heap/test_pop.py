from data_structures.min_heap import MinHeap

def test_returns_only_element_when_popped():
    min_heap = MinHeap()
    min_heap.push(1)
    assert min_heap.pop() == 1


def test_returns_elements_in_correct_order():
    min_heap = MinHeap()
    min_heap.push(1)
    min_heap.push(6)
    min_heap.push(3)
    min_heap.push(5)
    min_heap.push(0)
    min_heap.push(2)
    min_heap.push(4)

    assert min_heap.pop() == 0
    assert min_heap.pop() == 1
    assert min_heap.pop() == 2
    assert min_heap.pop() == 3
    assert min_heap.pop() == 4
    assert min_heap.pop() == 5
    assert min_heap.pop() == 6

def test_returns_none_when_heap_is_empty():
    min_heap = MinHeap()

    assert min_heap.pop() is None