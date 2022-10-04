# Tuple
    # Sequence type
    # Index-based
    # Immutable(can't modify)  | but member object may be mutable
    # Faster than list
    # Useful for fixed data

# Creating tuple
    # tuple constructor | tuple()
    # bracket or parenthesis | (1, 2, 3)
    # casting | tuple(list variable)


x = (1, 2, 3)
# del(x[1]) # fail | 'tuple' object doesn't support item deletion
# x[1] = 8 # fail | 'tuple' object does not support item assignment


# But member object may be mutable
x2 = ([1, 3], 3, 4)
# del(x2[0][1]) # ([1], 3, 4)

# Concatenation
# x2 += x # ([1, 3], 3, 4, 1, 2, 3)
print(x2)