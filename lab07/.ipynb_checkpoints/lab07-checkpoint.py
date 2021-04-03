import random
from unittest import TestCase

################################################################################
# EXTENSIBLE HASHTABLE
################################################################################
class ExtensibleHashTable:

    def __init__(self, n_buckets=1000, fillfactor=0.5):
        self.n_buckets = n_buckets
        self.fillfactor = fillfactor
        self.buckets = [None] * n_buckets
        self.nitems = 0
        
        #when there is a collision, you just move it to the next open spot
        when storing key/value you have to store them as a tuple.
        fill factor requirement, you would have to extend the data. 
        first item is the key ([h][0])

        
    def find_bucket(self, key):
        # BEGIN_SOLUTION
        # END_SOLUTION

    def __getitem__(self, key): #HELP
        # BEGIN_SOLUTION
        h = self.hash(key) % self.n_buckets
        if self.buckets[h] != None:
            if self.buckets == h:
                return self.buckets[h][1]
            else:
                h = (h + 1) % self.n_buckets
        elif self.buckets[h] == None:
            raise KeyError("the key doesn't exist in the hashtable")
        #to find the item, you have to hash the key and then find what position it is in. That should give you the position and find the value of that position
        #keep in mind collisions keep moving it over until you find an empty spot
        #you cant hash it and find it there, if you move it over, you have to look for it and see if that is the same to your value. 
        #storing tuples have multiple items, is the first one equal to the key, and if not keep looking for it.
        # END_SOLUTION
        
    def extend(self, newn_buckets):
        self.
        make new table
        new list
        double buckets
        tranfer current buckets to a new list
        and set buckets equal to that new list
        
    def __setitem__(self, key, value): #HELP
        # BEGIN_SOLUTION
        #h = hash(key) % self.n_buckets
        #if self.buckets[h] and self.data[h][0] != key:
        #self.buckets[h] = (key, value)
        #h=h+1 % n_buckets
        pass
        #keep in mind collisions
        # END_SOLUTION

    def __delitem__(self, key):
        # BEGIN SOLUTION
        h = hash(key) % self.n_buckets
        if self.buckets[h] and self.buckets[h][0] == key:
            self.buckets[h] = None
        # END SOLUTION

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False

    def __len__(self):
        return self.nitems

    def __bool__(self):
        return self.__len__() != 0

    def __iter__(self):
        ### BEGIN SOLUTION
        for j in range self.buckets:
            if self.buckets[j] != None:
                yield self.buckets[j] 
            elif self.buckets == None:
                continue
        #yield the items, if it is a none, value you dont yield it
        ### END SOLUTION

    def keys(self):
        return iter(self)

    def values(self):
        ### BEGIN SOLUTION
        for j in range self.buckets:
            if self.buckets[j][1] != None:
                yield self.buckets[j][1]
            elif self.buckets[j][1] == None:
                continue
        #like iter, find values instead of the keys
        #go through list and if it isnt none, yield the second value
        ### END SOLUTION

    def items(self):
        ### BEGIN SOLUTION
        tuple = ()
        for j in range self.buckets:
            tkey = self.buckets[j]
            tvalue = self.buckets[j][1]
            if self.buckets[j] != None and self.buckets[j][1] != None:
                tuple = (tkey, tvalue)
                yield tuple
            elif self.buckets[j] == None and self.buckets[j][1] == None:
                continue
        #yield both keys and values
        ### END SOLUTION

    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'

    def __repr__(self):
        return str(self)

################################################################################
# TEST CASES
################################################################################
# points: 20
def test_insert():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100000)

    for i in range(1,10000):
        h[i] = i
        tc.assertEqual(h[i], i)
        tc.assertEqual(len(h), i)

    random.seed(1234)
    for i in range(1000):
        k = random.randint(0,1000000)
        h[k] = k
        tc.assertEqual(h[k], k)

    for i in range(1000):
        k = random.randint(0,1000000)
        h[k] = "testing"
        tc.assertEqual(h[k], "testing")

# points: 10
def test_getitem():
    tc = TestCase()
    h = ExtensibleHashTable()

    for i in range(0,100):
        h[i] = i * 2

    with tc.assertRaises(KeyError):
        h[200]


# points: 10
def test_iteration():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100)
    entries = [ (random.randint(0,10000), i) for i in range(100) ]
    keys = [ k for k, v in entries ]
    values = [ v for k, v in entries ]

    for k, v in entries:
        h[k] = v

    for k, v in entries:
        tc.assertEqual(h[k], v)

    tc.assertEqual(set(keys), set(h.keys()))
    tc.assertEqual(set(values), set(h.values()))
    tc.assertEqual(set(entries), set(h.items()))

# points: 20
def test_modification():
    tc = TestCase()
    h = ExtensibleHashTable()
    random.seed(1234)
    keys = [ random.randint(0,10000000) for i in range(100) ]

    for i in keys:
        h[i] = 0

    for i in range(10):
        for i in keys:
            h[i] = h[i] + 1

    for k in keys:
        tc.assertEqual(h[k], 10)

# points: 20
def test_extension():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100,fillfactor=0.5)
    nitems = 10000
    for i in range(nitems):
        h[i] = i

    tc.assertEqual(len(h), nitems)
    tc.assertEqual(h.n_buckets, 25600)

    for i in range(nitems):
        tc.assertEqual(h[i], i)


# points: 20
def test_deletion():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100000)
    random.seed(1234)
    keys = [ random.randint(0,1000000) for i in range(10) ]
    for k in keys:
        h[k] = 1

    for k in keys:
        del h[k]

    tc.assertEqual(len(h), 0)
    with tc.assertRaises(KeyError):
        h[keys[0]]

    with tc.assertRaises(KeyError):
        h[keys[3]]

    with tc.assertRaises(KeyError):
        h[keys[5]]

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "*" + "\n" + f.__name__)

def say_success():
    print("SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_insert,
              test_iteration,
              test_getitem,
              test_modification,
              test_deletion,
              test_extension]:
        say_test(t)
        t()
        say_success()

if __name__ == '__main__':
    main()
