import time
import sys
sys.path.append('../binary_search_tree')
from binary_search_tree import BSTNode

start_time = time.time()


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure




# Replace the nested for loops below with your improvements

#print(set(names_1) & set(names_2))
#duplicates.append(set(names_1)&set(names_2))
#for x in (set(names_1) & set(names_2)):
#    duplicates.append(x)
# ^^^^this works in 0.035 seconds

#for x in set(names_1).intersection(names_2):
#    duplicates.append(x)

#^^^^^this works in .014 seconds, why is this faster?
#The previous version converted both to a set and compared each, I'm guessing it iterates over each
#set and checks all values against all values to see if they're true
#and this version makes one a set and just checks for duplicates against one set instead of two

#duplicates.append(x for x in names_1 if x in names_2)



#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
            #new_list.add_to_tail(name_1)

newTree = BSTNode("")

for name_1 in names_1:
    newTree.insert(name_1)
    
for name_2 in names_2:
    if newTree.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
