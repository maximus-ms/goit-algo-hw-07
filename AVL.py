class AVL:
    class none:
        def __init__(self, *_, **__):
            self.height = 0

        def __bool__(self):
            return False

        def __str__(self, *_, **__):
            return ""

        def insert(self, key=None):
            return self if key is None else AVL.Node(key)

        def delete(self, *_, **__):
            return self

        def get_max_node(self):
            return None

        def sum(self):
            return 0

    class Node:
        def __init__(self, key=None):
            self.key = key
            self.height = 1
            self.left = AVL.none()
            self.right = AVL.none()

        def __getitem__(self):
            return self.key

        def __bool__(self):
            return self.height != 0

        def get_balance(self):
            return self.left.height - self.right.height

        def height_update(self):
            self.height = 1 + max(self.left.height, self.right.height)

        def left_rotate(self):
            node_new = self.right
            node_new.left, self.right = self, node_new.left
            self.height_update()
            node_new.height_update()
            return node_new

        def right_rotate(self):
            node_new = self.left
            node_new.right, self.left = self, node_new.right
            self.height_update()
            node_new.height_update()
            return node_new

        def __str__(self, level=0, prefix="Root:"):
            ret = f"{' '*5*level} {prefix} [{self.key}]\n"
            ret += self.left.__str__(level + 1, "L->")
            ret += self.right.__str__(level + 1, "R->")
            return ret

        def get_min_node(self):
            if (self.height > 1) and self.left:
                return self.left.get_min_node()
            return self

        def get_max_node(self):
            if (self.height > 1) and self.right:
                return self.right.get_max_node()
            return self

        def insert(self, key):
            if key < self.key:
                self.left = self.left.insert(key)
            elif key > self.key:
                self.right = self.right.insert(key)
            else:
                return self
            self.height_update()
            balance = self.get_balance()
            if balance > 1:
                if key < self.left.key:
                    return self.right_rotate()
                else:
                    self.left = self.left.left_rotate()
                    return self.right_rotate()
            elif balance < -1:
                if key > self.right.key:
                    return self.left_rotate()
                else:
                    self.right = self.right.right_rotate()
                    return self.left_rotate()
            return self

        def delete(self, key):
            if key < self.key:
                self.left = self.left.delete(key)
            elif key > self.key:
                self.right = self.right.delete(key)
            else:
                if not self.left:
                    return self.right
                elif not self.right:
                    return self.left
                temp = self.right.get_min_node()
                self.key = temp.key
                self.right = self.right.delete(temp.key)
            if not self:
                return self
            self.height_update()
            balance = self.get_balance()

            if balance > 1:
                if self.left.get_balance() >= 0:
                    return self.right_rotate()
                else:
                    self.left = self.left.left_rotate()
                    return self.right_rotate()
            elif balance < -1:
                if self.right.get_balance() <= 0:
                    return self.left_rotate()
                else:
                    self.right = self.right.right_rotate()
                    return self.left_rotate()
            return self

        def sum(self):
            return self.key + self.left.sum() + self.right.sum()

    def __init__(self, key=None):
        self.root = AVL.none().insert(key)

    def __str__(self):
        return str(self.root)

    def insert(self, key, verbose=False):
        self.root = self.root.insert(key)
        if not verbose:
            return
        print("Inserted:", key)
        print("AVL-tree:")
        print(tree)

    def insert_from(self, keys, verbose=False):
        for key in keys:
            self.insert(key, verbose)

    def delete(self, key, verbose=False):
        self.root = self.root.delete(key)
        if not verbose:
            return
        print("Deleted:", key)
        print("AVL-tree:")
        print(tree)

    def delete_from(self, keys, verbose=False):
        for key in keys:
            self.delete(key, verbose)

    def get_min_node(self):
        return self.root.get_min_node()

    def get_max_node(self):
        return self.root.get_max_node()

    def min(self):
        return self.get_min_node().key

    def max(self):
        return self.get_max_node().key

    def sum(self):
        return self.root.sum()


if __name__ == "__main__":
    from numpy import random

    keys = list(set(random.randint(100, size=16)))
    tree = AVL()
    tree.insert_from(keys, verbose=True)

    # Delete
    keys_to_delete = random.choice(keys, size=5)
    tree.delete_from(keys_to_delete, verbose=False)
    tree.delete(0)
    print(tree)

    print(f"Keys in were added to the AVL tree:  {sorted(keys)}")
    print(f"Keys were deleted from the AVL tree: {keys_to_delete}")
    expected_keys = list(set(keys) - set(keys_to_delete))
    print(f"Keys are in the AVL tree:            {sorted(expected_keys)}")
    print(f"Min key in the AVL tree:             {tree.min()}")
    print(f"Max key in the AVL tree:             {tree.max()}")
    print(f"Expected sum of keys:                {sum(expected_keys)}")
    print(f"Sum of keys in the AVL tree:         {tree.sum()}")
