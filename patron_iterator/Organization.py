from collections.abc import Iterable
from OrgIterator import OrgIterator


class Organization(Iterable):

    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return OrgIterator(self.root)
