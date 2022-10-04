# Set
    # Store non-duplicate items
    # Very fast access compares to list |-| set hashes all of its item making it very easy and fast to access an element using the | it hash
    # Unordered

# Creating set
    # set constructor :: set()
    # set curly braces :: x = { 1, 2, 3}
    # casting :: x = set(list variable)

# Set operations
    # add() :: Add an item to a set
        # x.add(4)

    # remove() :: Remove an item from a set
        # x.remove(desire item) || x.remove(2)

    # in || not in :: Check membership in x
        # 3 in x || 2 not in x

    # pop() :: Pop random item from set
        # x.pop()

    # clear() :: Delete all item in the set
        # x.clear()

# Mathematical set operations
    # Intersection (AND) :: set1 & set2
    # Union (OR) :: set1 | set2
    # Symmetric difference (XOR) :: set1 ^ set2 difference (in set 1 but not set2) :: set1 - set2
    # Subset (set2 contains set1) :: set2 <= set1
    # Superset (set1 contains set1) :: set1 >= set1

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1 & set2)
print(set1 | set2)
print(set1 ^ set2)
print(set1 - set2)
print(set1 <= set2)
print(set1 >= set2)