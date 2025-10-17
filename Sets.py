#Sets: Sets are unordered collections of unique elements
#Means ther can be only be one representative of the same object
#Example:

my_sets = set()
print(my_sets)
my_sets.add(1)
my_sets.add(2)
print(my_sets) #{1, 2}

#tring to add 2 again let's see?
my_sets.add(2)
print(my_sets) # {1, 2} Its not added again 2 its keep the value only one time

print(type(my_sets))
print(len(my_sets))

#Lest show type casting : Creating the list with repeated items and will change the type to sets
#Then will see the results

my_List = [1,1,1,2,2,2,3,3,3,4,4,4,4,4 ,0, 0 ,0 ,0] 
print(my_List) #[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]

#Changing the type 
print(set(my_List)) #{1, 2, 3, 4} Remove all repeating values its also follow order


#Booleans which return true and false based on condition

print(1>2)
print(type(1<2))
print(1 == 1)
