#List in mutable and we can add all kind of values in list and we can store same values in list
my_List = [1,2,3]
print(my_List)
print(len(my_List))
my_List = ['String' , 100 , 20.3]
print(my_List)
print(len(my_List))

my_List = ['One' , 'two' , 'three']

#Slicing in list
print(my_List[1:])

#Concatenate in string
another_List = ['four' , 'five']
new_list = my_List + another_List
print(new_list)

#Alter the list
new_list[0] = 'ONE ALL CAPS'
new_list[1] = 'ONE ALL CAPS'
print(new_list)

#Append in the list
new_list.append('Six')
print(new_list)

#Remove last element
print(new_list.pop())

print(new_list)

#Remove  element from particualr index
print(new_list.pop(0))

print(new_list)

print(new_list.sort())

num_list = [4,3,2,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)


