from lib.mru import MRU

mru = MRU()

mru.insert(1)
mru.get()
mru.insert(2)
mru.get()
mru.insert(3)
mru.get()
mru.insert(4)
mru.get()
mru.insert(5)
mru.get()
mru.insert(6)
mru.get()
mru.insert(4)
mru.get()
mru.insert(1)
mru.get()
mru.insert(6)
mru.get()
mru.insert(8)
mru.get()
mru.insert(5)
mru.get()
mru.insert(1)
mru.get()
mru.insert(5)
mru.get()

"""

OUTPUT ::

[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 6]
[1, 2, 3, 4, 6]
[2, 3, 1, 4, 6]
[2, 3, 6, 1, 4]
[2, 8, 6, 1, 4]
[5, 8, 6, 1, 4]
[5, 8, 6, 4, 1]
[8, 6, 4, 5, 1]

"""
