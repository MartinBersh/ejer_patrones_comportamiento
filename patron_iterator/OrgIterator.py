from collections.abc import Iterator


class OrgIterator(Iterator):

    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        current = self.stack.pop()
        self.stack.extend(reversed(current.subordinates))
        return current