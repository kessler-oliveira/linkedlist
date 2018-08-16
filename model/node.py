class Node:
    def __init__(self, data=None, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random

    def __str__(self):
        return '[data: {0} <{1}>, random: {2} <{3}>]'.format(
            self.data,
            hex(id(self)),
            self.random.data if self.random else None,
            hex(id(self.random)) if self.random else None
        )
