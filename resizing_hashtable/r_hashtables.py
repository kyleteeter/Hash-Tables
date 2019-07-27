

# '''
# Linked List hash table key/value pair
# '''
# Starting 
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        pass


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381

    for character in string:
        hash = (( hash << 5) + hash) + ord(character)

    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    #Get hashed version of key
    key_hash = hash(key)
    #Find the index of pair
    index = key_hash % hash_table.capacity
    current_pair = hash_table.storage[index]

    while current_pair is not None and current_pair.key != key:
      current_pair = current_pair.next
    if current_pair is None:
      new_pair = Pair(key, value)
      new_pair.next = hash_table.storage[index]
      hash_table.storage[index] = new_pair
    else:
      current_pair.value = value

    # Insert pair
    hash_table.storage[index] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
