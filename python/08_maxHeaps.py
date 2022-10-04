# Heaps | MaxHeaps
    # Complete Binary Tree
    # Every node  <= its parent
    # Very Fast
    # Insert in O(log n)
    # Get Max O(1)
    # Remove Max in O(log n)
    # Easy to implement using a List
    # MaxHeap start at index 1

# Access an element using it index i if i = 4

# Accessing its parent : - : i/2 -: 4/2 = 2 at this index get parent item

# Accessing left child of the index 4 parent element : - : i * 2 :- 4 * 2 = 8 at index 8 get parent left child

# Accessing right child of index 4 parent element : - : i * 2 + 1 :-: 4 * 2 + 1 = 9 at index 9 get parent right child

# MaxHeap operations
    # push() | insert
    # peek() :: get max
    # pop() :: remove max


# push
    # add a value to the end of the array
    # float it up to its proper position || comparing which one is greater || parent and the item to added || swap if greater than

# peek
    # returns the top | max element of the heap


# pop
    # move top | max item to the end of the heap | array :-: swap it with the last element in the heap | array
    # Delete it
    # bubble down the new element at the max | top position to its correct position :-: do some comparison with child node to attain it correct position in the heap
    # return max | top element

