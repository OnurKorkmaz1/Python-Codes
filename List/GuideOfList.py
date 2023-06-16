thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# ACCESS PYTHON LIST ELEMENTS
print(thislist[0])
print(thislist[1])

# SLICING OF A PYTHON LIST

my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:5]) # items from index 2 to index 4
print(my_list[5:]) # items from index 5 to end
print(my_list[:]) # items beginning to end

# --- ADD ELEMENTS TO PYTHON LIST --- .append() // .extend() // .insert()

numbers = [21, 34, 54, 12]
print("Before Append:", numbers)

numbers.append(32) # using append method
print("After Append:", numbers)


my_list.extend(thislist)  # join two lists
print("Son hali:", my_list) 

my_list.insert(1,"karpuz") # insert items according to index
print(my_list)


# --- REMOVE AN ITEM FROM LIST ---


del my_list[1]  # delete second item in a list
print(my_list) 

my_list.remove("p")
print(my_list)

my_list.clear() # clear the list
print(my_list)

# --- LOOP THROUGH A LIST

newlist =[1,2,3,4,5,6]
print(newlist)

for i in newlist:
    print(i)

for i in range(len(newlist)):
    print(newlist[i])

# --- ► Check if an Item Exists in the Python List --

print("9" in newlist) # true/false olarak sonuç verir