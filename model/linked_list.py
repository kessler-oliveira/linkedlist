from model.node import Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        nodes = []
        loop = self.head
        while loop:
            nodes.append(str(loop))
            loop = loop.next
        return '\n'.join(nodes)

    def copy(self):
        nodes = {}
        loop = self.head
        prev_node = None

        while loop:
            new_node = Node(loop.data)
            nodes[loop] = new_node

            if prev_node:
                prev_node.next = new_node

            prev_node = new_node
            loop = loop.next

        for node in list(nodes.keys()):
            nodes.get(node).random = nodes.get(node.random)

        return LinkedList(nodes.get(self.head))
