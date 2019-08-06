
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
        self.capacity = capacity 
        self.storage = [None] * capacity
        self.count = 0



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
    index = hash(key, hash_table.capacity)


    # if hash_table.count == hash_table.capacity:
    #     hash_table.resize
    # if hash_table.storage[index] == None:
    #     hash_table.storage[index] = LinkedPair(key, value)
    #     hash_table.count += 1
    # else:
    current_pair = hash_table.storage[index]
    
    while current_pair is not None and current_pair != key:
        current_pair = current_pair.next

    if current_pair is None:
        new_pair = LinkedPair(key, value)
        original = hash_table.storage[index]
        hash_table.storage[index] = new_pair
        new_pair.next = original
        # Insert pair

        if new_pair.next is None:
            hash_table.count += 1
    else: 
        current_pair.value = value

    # Insert pair
    


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]
    prev_pair = None
    
    # set previous node to equal current
    if current_pair is not None:
        while current_pair is not None and current_pair.key != key:
            prev_pair = current_pair
            current_pair = current_pair.next
    # once previous node is set override current node.
        if prev_pair is None and current_pair.key == key:
            hash_table.storage[index] = None
        else:
            prev_pair.next = None

    else:
        print('Error, no key')
# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]

    if current_pair is not None:
        while current_pair is not None and current_pair.key != key:
            current_pair = current_pair.next

        if current_pair is None:
            print('Key not found')
        else:
            return current_pair.value

    else:
        print('Key not found')




# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)
    new_hash_table.storage = [None] * new_hash_table.capacity
    for i in range(len(hash_table.storage)):
        new_hash_table.storage[i] = hash_table.storage[i]
        hash_table.storage[i] = None
    return new_hash_table


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
