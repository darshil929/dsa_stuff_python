# hash function that uses aski values of the char in input, adds them and mods them with 100
# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index] 
    
t = HashTable()
t['march 6'] = 50
t['october 2'] = 92
t['march 17'] = 100
print(t['march 6'])
print(t['march 17'])
del t['march 17']
print(t.arr)