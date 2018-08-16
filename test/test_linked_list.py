import unittest
from random import randint

from model.node import Node
from model.linked_list import LinkedList

SIZE = 5

class TestLinkedList(unittest.TestCase):
    def test_copy(self):

        nodes = []
        for i in range(SIZE):
            nodes.append(Node(i))

            if i:
                nodes[i - 1].next = nodes[i]

        for i in range(SIZE):
            number = randint(0, SIZE)
            if number < SIZE:
                nodes[i].random = nodes[number]

        if nodes:
            linked_list = LinkedList(nodes[0])
            linked_list_copy = linked_list.copy()

            loop = linked_list.head
            loop_copy = linked_list_copy.head

            while loop:
                self.assertEqual(loop.data, loop_copy.data)

                if loop.next:
                    self.assertEqual(loop.next.data, loop_copy.next.data)

                if loop.random:
                    self.assertEqual(loop.random.data, loop_copy.random.data)

                loop = loop.next
                loop_copy = loop_copy.next

            print('----------------------------------------')
            print('Original')
            print('----------------------------------------')
            print(linked_list)
            print('----------------------------------------')
            print('Copia')
            print('----------------------------------------')
            print(linked_list_copy)

if __name__ == '__main__':
    unittest.main()
