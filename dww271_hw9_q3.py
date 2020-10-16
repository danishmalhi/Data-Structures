#Question 3




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
        self.table=[]
        for i in range(self.N):
            self.table.append(None)
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        
        if isinstance(curr_bucket, tuple):
            return curr_bucket[0]
        
        else:
            return curr_bucket[key]
        

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
         
        if curr_bucket==None:
            curr_bucket  = (key,value)
            self.table[i]=curr_bucket
            self.n+=1
            if (self.n > self.N):
                self.rehash(2 * self.N)

                    
        elif isinstance(curr_bucket, tuple):
            tuple_curr_bucket_key=curr_bucket[0]
            tuple_curr_bucket_value=curr_bucket[1]
            curr_bucket=UnsortedArrayMap()
            curr_bucket[tuple_curr_bucket_key]=tuple_curr_bucket_value
            curr_bucket[key]=value
            self.table[i]=curr_bucket
            self.n+=1
            if (self.n > self.N):
                self.rehash(2 * self.N)

        
        else:
            if isinstance(curr_bucket, UnsortedArrayMap):
                old_size = len(curr_bucket)
                curr_bucket[key] = value
                self.table[i]=curr_bucket
                new_size = len(curr_bucket)
                if (new_size > old_size):
                    self.n += 1
                if (self.n > self.N):
                    self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        
        if isinstance(curr_bucket,UnsortedArrayMap):
            curr_bucket = None
            self.table[i]=curr_bucket
            
            self.n -= 1
            if (self.n < self.N // 4):
                self.rehash(self.N // 2)

        
        else:
            curr_bucket = None 
            self.table[i]=curr_bucket
            self.n -= 1
            if (self.n < self.N // 4):
                self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table: 
            
            if isinstance(curr_bucket, tuple):
                yield curr_bucket[0]
            
            elif isinstance(curr_bucket, UnsortedArrayMap):
                for key in curr_bucket:
                    yield key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def print_hash_table_self_table(ht):
    
    for i in range (len(ht.table)):
        curr_bucket=ht.table[i]
        if curr_bucket==None:
            print(i," : ", " None ")
            
        elif isinstance(curr_bucket, tuple):
            print(i, " : ", curr_bucket,"  TUPLE TYPE ")
            
        else:
            if isinstance(curr_bucket,UnsortedArrayMap):
                lst_key_val=[]
                for element in curr_bucket:
                    lst_key_val.append((element,curr_bucket[element]))
                print(i," : ", lst_key_val, "  UNSORTED ARRAY TYPE")
        print()

def print_hash_table(ht):
    count=0
    for bucket in ht:
        count+=1
        print("count=", count," ; ", bucket)
        #print(ht[bucket]) #checks getitems func

        
#def main():
##    hashtable = ChainingHashTableMap()
##    for i in range (100):
##        random_key=random.randint(10,99)
##        random_val=random.randint(100,999)
##        hashtable[random_key]=random_val
##    print_hash_table_self_table(hashtable)
##    print("################################################")
##    print("################################################")
##
##
##    print_hash_table(hashtable)
##    hashtable2 = ChainingHashTableMap()
##    for i in range (100):
##        hashtable2[i]=random.randint(0,9)
##
##    print_hash_table_self_table(hashtable2)
##    print("################################################")
##    #print_hash_table(hashtable2)
##
##    for i in range (5,len(hashtable2)):
##        
##        del hashtable2[i]
##
##    print_hash_table(hashtable2)
##
##    
##
##main()
        
