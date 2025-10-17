#Tuples:
#Tuples are very similer to the list , However they have one key diff which is-Immutability
#Once an element is inside a tuple, it can not be reassigned
#Tuples use paraenthes (1,2,3)
#Data integrity is the main reason we used tuples

tuples = (1,2,3)
my_list =[1,2,3]
print(type(tuples))
print(type(my_list))

#Let's test the key diff with code
my_list[1] = 3
print(my_list) #Output is: [1,3,3]
#tuples[1] =4
#print(tuples) #Output is error:tuple' object does not support item assignment

print(len(tuples))
print(len(my_list))

#We can use slicing and indexing in tuples
#We can store diff type of datatype values in tuple
tuple2 = ('Prashant' , 26 , [1,2])
#INdexing
print(tuple2[0])
#Slicing
print(tuple2[::-1])

# Duplication and count concept
tuple3 = ('a','a','a',1,1,1,'b')
print(tuple3.count('a')) #3
print(len(tuple3)) # 7

#Let's check immutability
my_list[0] = 'new'
print(my_list) #['new', 3, 3] Its added becuase its mutable
tuple3[0] = 4
print(tuple3) # Return Error:'tuple' object does not support item assignment

