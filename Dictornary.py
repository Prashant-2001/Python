#Dictionaries are unordered mapping for storing objects. Dictionaries use a key-value pairing
#instead.
#This key-value pair allows users to quickly grab objects without needing to known an index location

#Syntax
#{'key1':'value1','key2':'value2'}
#Diff between list and Dictionary
#List: Object retrived by location. Ordered sequecne can be indexed or sliced
#Dictonary: Objects retrived by key name. Unordered and can not be sorted

my_dict = {'key1':'Hello','key2':'Prashant'}
print(my_dict)
print(my_dict['key1'])
marks_lookup = {'Prashant':100,'Vishal':88.5,'Ujjwal':'89.66'}
print(marks_lookup)
print(marks_lookup['Ujjwal'])
print(type(marks_lookup['Prashant']))
print(type(marks_lookup['Vishal']))
print(type(marks_lookup['Ujjwal']))

#Will show Dict which having list in that dic and nested dict

nested_Dict = {'Number':123, 'List':[0,1,2,3] , 'Nested_dict':{'inside_dict':100}}
print(nested_Dict)
print(nested_Dict['List'])
print(nested_Dict['Nested_dict']['inside_dict'])

#Add new key value in dict
nested_Dict['String'] = 'Prashant'
print(nested_Dict)

#Change the value of any key in Dict
nested_Dict['Number'] = 10000
print(nested_Dict)

#To get all values() and keys() and itmes()
print(nested_Dict.values())
print(nested_Dict.keys())
print(nested_Dict.items())

