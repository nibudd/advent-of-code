from data_structures.min_heap import MinHeap

def test_returns_smallest_element_of_2_when_added_out_of_order():
    min_heap = MinHeap()
    min_heap.push(2)
    min_heap.push(1)

    assert min_heap.peek() == 1


def test_returns_smallest_element_of_many_added_out_of_order():
    min_heap = MinHeap()
    min_heap.push(4)
    min_heap.push(9)
    min_heap.push(6)
    min_heap.push(8)
    min_heap.push(3)
    min_heap.push(5)
    min_heap.push(7)

    assert min_heap.peek() == 3


def test_returns_none_when_heap_is_empty():
    min_heap = MinHeap()

    assert min_heap.peek() is None