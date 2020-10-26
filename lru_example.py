from lib.lru import LRU

lru = LRU()
lru.insert(1)
lru.get()
lru.insert(2)
lru.get()
lru.insert(3)
lru.get()
lru.insert(4)
lru.get()
lru.insert(5)
lru.get()
lru.insert(6)
lru.get()
lru.insert(4)
lru.get()
lru.insert(6)
lru.get()
lru.insert(7)
lru.get()
lru.insert(8)
lru.get()
lru.insert(5)
lru.get()
lru.insert(1)
lru.get()
lru.insert(5)
lru.get()

"""
OUTPUT ::

[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[6, 2, 3, 4, 5]
[6, 4, 2, 3, 5]
[4, 6, 2, 3, 5]
[4, 6, 7, 3, 5]
[4, 6, 7, 8, 5]
[4, 6, 7, 8, 5]
[1, 6, 7, 8, 5]
[1, 5, 6, 7, 8]
"""
