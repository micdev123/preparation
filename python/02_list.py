# Lists 
    # Sequence Type
    # Sortable
    # Index-based
    # Mutable

# Creating a list
    # list constructor :: list()
    # square bracket :: []
    # casting :: list(tuple variable)
    # list comprehension

# List Constructor
myList1 = list()

# Square Bracket
myList2 = [1, 2, 3] # [1, 2, 3]

# Casting
myTuple = (4, 5, 6)

myList3 = list(myTuple) # [4, 5, 6]

# List Comprehension
myList4 = [m for m in range(8)] # [0, 1, 2, 3, 4, 5, 6, 7]
myList5 = [i**2 for i in range(10) if i>4] # [25, 36, 49, 64, 81]

print(myList5)

# List Operations
    # del() :: Delete a single item|element in a list or the entire list
        # del(x[1]) single item deleted
        # del(x) entire list deleted

    # append() :: Add an item to the end of the list
        # x.append(3)

    # extend() :: Basically appending a list to another list
        # x.extend(y) y is the other list
    
    # insert() :: Allow us to insert an item at a given index in a list
        # x.insert(1, 7) -- 1st param : index 2nd param element

    # pop() :: Pop off the last index in the list
        # x.pop()

    # remove() :: Remove the first instance of an item
        # x.remove(3)

    # reverse() :: Reverse the order of the list. It is an in-place sort, meaning it changes the original list
        # x.reverse()

    # sort() ::Sort the list in-place. 
        # x.sort()

    # Sorted() :: Returns a new list without changing the original list
        # sorted(x)

    
    # Reverse sort() :: Sort items descending
        # x.sort(reverse=True)

