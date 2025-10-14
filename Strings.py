#Strings Index to indicate positions of what you wish to grab
# Character: H e l l o
#Index:      0 1 2 3 4
#Reverse In: 0 -4 -3 -2 -1

#Slicing allows you to grab a subsection of multiple charachters a "Slice"
#Syntx: [Start:Stop:step]

#Code
print('Hello')
print("Hello")
print(len('This is my pc'))
print(len('Hello'))

mystring = 'Hello World'
print(mystring)

#Let's start indexing
print(mystring[8])

#Reverse string
print(mystring[::-1])
myString = "tinker"
print(len(myString))
print(myString[1:4])

#Strings properties and methods
#Immutability - String are immutable in python

letter = 'z'
print(letter*10)

print('2'+'3')

print(myString.upper()) #In capital letter
print(mystring.split('l'))

#String interpolation
#there are multiple ways to format strings for printing variables in them 
#Two Methods are there:
#.format()
#f-strings(formatted string literals)

#.Format method syntax:
#'String here{} then aslo{}' .format('String1','String2')
# {} we can put that braces where we want to add our string and format our string.

print('This is my name {}'.format('Prashant'))
print('The {2} {1} {0} is my charachter place and name'.format('Intelligent','Gangoh', "Prashant"))



