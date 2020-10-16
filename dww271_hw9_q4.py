#Question 4




import random
from UnsortedArrayMap import UnsortedArrayMap

class ChainingHashTableMap:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N


    def __init__(self, N=64):
        self.N = N
        self.table = [UnsortedArrayMap() for i in range(self.N)]
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)

        self.dictionary={} #theta(1)
        self.count=0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

        if key not in self.dictionary:
            self.count+=1
            self.dictionary[key]=self.count

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        del curr_bucket[key]
        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

        del self.dictionary[key]

    def __iter__(self):
        maximum=0
        for key,val in self.dictionary.items():
            if self.dictionary[key] >= maximum:
                maximum = self.dictionary[key]
                yield key               

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print("(", key, ", ", curr_bucket[key], ")", sep="", end=" ")
        print()

def main():
    hashtable = ChainingHashTableMap()
    for i in range (50):
        hashtable[i]=0

    for keys in hashtable:
        print(keys)

    del hashtable[45]
    
    for keys in hashtable:
        print(keys)
            
    #print_hash_table(hashtable)

#main()
