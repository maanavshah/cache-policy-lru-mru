from lib.cache_policy import CachePolicy

class MRU(CachePolicy):

  def __init__(self):
    super().__init__()
    self.replace_at = self.cache_size - 1

  def insert(self, value):
    if len(self.cache) < self.cache_size:
      if value not in self.cache:
        self.cache.append(value)
    else:
      if value in self.cache:
        ind = self.cache.index(value)
        if ind > self.replace_at:
          self.cache.remove(value)
          self.cache.insert(self.replace_at+1, value)
        else:
          self.cache.remove(value)
          self.cache.insert(self.replace_at, value)
          self.replace_at = (self.replace_at - 1) % self.cache_size
      else:
        self.cache[self.replace_at] = value
        self.replace_at = (self.replace_at - 1) % self.cache_size

  def get(self):
    print(self.cache)
