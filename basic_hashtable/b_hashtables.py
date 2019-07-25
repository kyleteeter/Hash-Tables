

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = [None] * capacity
        self.count = 0


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string):
  hash = 5381
  
  for character in string:
    hash = (( hash << 5) + hash) + ord(character)
   
  return hash 


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    #Get hashed version of key
    key_hash = hash(key)
    #Form new key value pair
    # new_pair = Pair(key, value)
    #Find the index of pair
    index = key_hash % hash_table.capacity
    # Insert pair
    hash_table.storage[index].value = value

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    removed = False
    for i in range(hash_table.count):
        if removed:
            hash_table.elements[i-1] == hash_table.elements[i]
        elif hash_table.elements[i] == key:
            removed = True
        if removed:
            hash_table -=1
            hash_table[hash_table.count] = None
        else:
            print("Error")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    if hash_table.count <= 0:
        print("Empty")
    else:
        string = "["
        for i in range(hash_table.count):
            string += str(hash_table.elements[i])
            if i < hash_table.count - 1:
                string += ", "

        string += "]"
        print(string)


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
