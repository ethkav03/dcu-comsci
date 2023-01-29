class HashTable:
    """Create a hash map backed by a Python list"""
    store = []
    number_elements = 0

    def __init__(self, n: int = 1):
        """
        Create storage for a HashTable with `n` entries.
        """
        if n > 0:
            self.store = [None] * n
        else:
            self.store = [None]

    def getindex(self, key) -> int:
        """Get the index corresponding to the given `key`"""
        #_hash = HashTable.num_shift(key, 5, 'l')
        _hash = hash(key)
        p = self.get_prime(len(self.store))
        a = 3
        b = 7
        return (((_hash * a) + b) % p) % len(self.store)

    def get_prime(self, table):
        p = table
        while True:
            p += 1
            for i in range(2, (p // 2) + 1):
                if p % i == 0:
                    break
            return p
            

    def bit_rep(s):
        bit = bin(ord(s[0]))
        for c in s[1:]:
            bit += bin(ord(c))
        return bit

    def poly_hash(s):
        total = 0
        for i in range(0, len(s)):
            a = 2
            total += ord(s[i]) * a
        return str(total)

    def num_shift(n, p, d):
        t = ''
        if d == 'l':
            for c in n:
                m = format(ord(c), '08b')
                m = str(m)
                m = f"{n[8-p:].zfill(8)}"
                t += int(m)
        else:
            for c in n:
                m = format(ord(c), '08b')
                m = str(m)
                m = f"{n[8-p:].ljust(8)}"
                m = format(m, '08b')
                t += (m)
            
        return t

    def put(self, key, value):
        """
        Store the `value` at the index given by `key`, growing the underlying storage if necessary.
        """
        number_store = len(self.store)
        if self.number_elements + 1 == number_store:
            self.store = self.store + ([None] * number_store)

        index = self.getindex(key)
        self.number_elements += 1
        self.store[index] = value

    def get(self, key):
        """
        Retrieve the value at the index given by `key`, or `None`.
        """
        index = self.getindex(key)
        return self.store[index]

    def delete(self, key):
        """
        Remove the data at the index `key`, if it exists.
        """
        index = self.getindex(key)
        if self.store[index] is not None:
            self.number_elements -= 1
            self.store[index] = None


h = HashTable(1000)
h.put('DCU', 'D9')
h.put('TCD', 'D2')
h.put('UCD', 'D4')

print(h.get('DCU'))
print(h.get('TCD'))

h.delete('UCD')
print(h.get('UCD'))
print(h.get('DCU'))