#!/usr/bin/python3
# Print a tree with height specified by the user
# This is the structure of the tree
"""
     #
    ###
   #####
  #######
 #########
###########
     #
"""

# Approach:
# We are going to use a while loop and 3 for loops
# How the structure of the tree is constructed

# 5 spaces: 1 hash
# 4 spaces: 3 hash
# 3 spaces: 5 hash
# 2 spaces: 7 hash
# 1 spaces: 8 hash
# 0 spaces: 9 hash

# Todo

# 1. Decrement the spaces by 1 each time through the loop
# 2. Increment the hash by 2 each time through the loop
# 3. Save space gotten from the calculation of tree_height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and hashes for each row
# 6. Print stump spaces and then 1 hash

# Get tree height from the user
tree_height = input("Enter the height of your tree: ")
# Convert tree height given by the user to integer
tree_height = int(tree_height)
# calculate the spaces for the top of the tree
spaces = tree_height - 1
# There is always one hash that get incremented by 2
hashes = 1
# Save stump spaces for later
# This gets used to determine the position of tree trunk
stump_space = tree_height - 1

# Loop and make sure that the right numbers of rows are printed
while tree_height != 0:
    # Print the spaces
    for i in range(spaces):
        print(' ', end="")
    # Print the hashes
    for i in range(hashes):
        print('#', end="")
    # Print newline after each row
    print()
    # Always decrement the space in the loop by 1
    spaces -= 1
    # Always increment the hash in the loop by 2
    hashes += 2
    # Decrement tree_height each time to jump out of the loop
    tree_height -= 1
# Print the spaces for the stump and the final hash
for i in range(stump_space):
    print(' ', end="")
print('#')
