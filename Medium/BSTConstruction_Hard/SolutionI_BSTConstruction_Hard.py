# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Algorithmic Beauty Bless You - O(logn) average.time | O(1) space
    def insert(self, value):
        parent, new_node = self, BST(value)
        while True:
            if value < parent.value:
                if not parent.left:
                    parent.left = new_node
                    break
                parent = parent.left
            elif not parent.right:
                parent.right = new_node
                break
            else:
                parent = parent.right
        # Do not edit the return statement of this method.
        return self

    # Algorithmic Beauty Bless You - O(logn) average.time | O(1) space
    def contains(self, value):
        current = self
        while current:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    # Algorithmic Beauty Bless You - O(logn) average.time | O(1) space
    def remove(self, value):
        parent, current = None, self
        while current:
            if value == current.value:
                break
            parent = current
            current = current.left if value < current.value else current.right
        else:
            return self
        suc_parent, succession = current, current.right
        if succession:
            while succession.left:
                suc_parent, succession = succession, succession.left
            if suc_parent.left is succession:
                suc_parent.left = succession.right
            else:
                suc_parent.right = succession.right
            current.value = succession.value
        elif parent:
            if parent.left is current:
                parent.left = current.left
            else:
                parent.right = current.left
        elif current.left:
            current.value, current.left, current.right = current.left.value, current.left.left, current.left.right
        # Do not edit the return statement of this method.
        return self
