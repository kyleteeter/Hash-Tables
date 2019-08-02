

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
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
  index = hash(key, hash_table.capacity)
  if hash_table.storage[index] == None:
    hash_table.storage[index] = Pair(key, value)
    hash_table.count += 1
  else:
    if key == hash_table.storage[index].key:

    else:
      hash_table.storage[index].value = value
      duplicate = False
  # while current_pair.next is not None:
  #   if current_pair.key == key:
  #           current_pair.value = value
  #           duplicate = True
  #           break
  #         current_pair = current_pair.next
  #       if not duplicate:
  #         hash_table.storage[index] = Pair(key, value)
  #         hash_table.count += 1
      # Insert pair
    

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    #Hash Key
    # key_hash = hash(key)
    # #Get index
    # index = key_hash % hash_table.capacity
    index = hash(key, hash_table.capacity)
    #Remove value by setting it to None
    if hash_table.storage[index] != None:
        hash_table.storage[index] = None
    else:
      print(f"{key} not found.")

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # key_hash = hash(key)

    # index = key_hash % hash_table.capacity
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is not None:
        
        if hash_table.storage[index].key == key:

            return hash_table.storage[index].value
    return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
