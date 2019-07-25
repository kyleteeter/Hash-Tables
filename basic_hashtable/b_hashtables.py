

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
def hash(string, max):
  hash = 5381
  
  for character in string:
    hash = (( hash << 5) + hash) + ord(character)
   
  return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    #Throw an error if array is out of count
    if value > hash_table.count:
        print('')
    #Move elements to create a space at value 
    for i in range(hash_table.count, value, - 1):
        hash_table.elements[i] = hash_table.elements[i-1]
    #Add new element to array and update count.
    hash_table.elements[value] = key
    hash_table.count += 1
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
    


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
