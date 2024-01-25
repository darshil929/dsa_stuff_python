# hash function that uses aski values of the char in input, adds them and mods them with 100
# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    
t = HashTable()
t['march 15'] = 50
t['october 2'] = 92
print(t['march 15'])
print(t.arr)
del t['october 2']
print(t.arr)