from ting_file_management.priority_queue import PriorityQueue
import pytest

data = [
    {
        "nome_do_arquivo": "file_1.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["dodo", "dodo", "dodo", "dodo"]
    },
    {
        "nome_do_arquivo": "file_1.txt",
        "qtd_linhas": 8,
        "linhas_do_arquivo": [
            "dodo", "dodo", "dodo", "dodo",
            "dodo", "dodo", "dodo", "dodo"
        ]
    },
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(data[0])
    priority_queue.enqueue(data[1])

    assert len(priority_queue) == 2

    deq = priority_queue.dequeue()
    assert len(priority_queue) == 1
    assert deq == data[0]
    deq = priority_queue.dequeue()
    assert len(priority_queue) == 0
    assert deq == data[1]

    priority_queue.enqueue(data[0])
    priority_queue.enqueue(data[1])

    assert priority_queue.search(0) == data[0]
    assert priority_queue.search(1) == data[1]

    priority_queue.dequeue()
    priority_queue.dequeue()

    priority_queue.enqueue(data[1])

    assert priority_queue.is_priority(data[0]) is True

    priority_queue.enqueue(data[0])

    assert priority_queue.is_priority(data[1]) is False

    with pytest.raises(IndexError):
        priority_queue.search(15)
