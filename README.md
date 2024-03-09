# GoITNeo Algo HW-7

## Task 1
Write an algorithm (function) that finds the maximum value in a binary search tree or an AVL tree. Take any implementation of the tree from your notes or another source.
## Task 2
Write an algorithm (function) that finds the minimum value in a binary search tree or an AVL tree. Take any implementation of the tree from your notes or another source.
## Task 3
Write an algorithm (function) that finds the sum of all values in a binary search tree or an AVL tree. Take any implementation of the tree from your notes or another source.

## Solution
I prepared AVL class with methods:
 - insert - to add a key
 - insert_from - to add keys from iterable
 - delete - to delete a need key
 - delete_from - to delete keys from iterable
 - get_min_node - find a node with the minimum key
 - get_max_node - find a node with the maximum key
 - min - get a minimum key
 - max - get a maximum key
 - sum - calculate a sum af all keys

## How to use
```python
from AVL import AVL

tree = AVL()
tree.insert(5)
tree.insert_from([4, 6, 1, 7])
tree.insert(0, verbose=True)

print("Min key:", tree.min())
print("Max key:", tree.max())

tree.delete(6)
tree.delete_from([4,7])

print(tree)
print("Sum of keys:", tree.sum())
```
As result we will get such output:
```
Inserted: 0
AVL-tree:
 Root: [5]
      L-> [1]
           L-> [0]
           R-> [4]
      R-> [6]
           R-> [7]

Min key: 0
Max key: 7
 Root: [1]
      L-> [0]
      R-> [5]

Sum of keys: 6
```
