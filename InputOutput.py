#Input and output with test.txt file
myfile = open('test.txt')
print(myfile.read()) #Read the complte file and print
#print(myfile.read())
print(myfile.readlines())
with open('test.txt', mode='r') as m:
    contents=m.read()

with open('test.txt', mode='a') as m:
    contents=m.write('\nFour ON Fourth11')
    print(myfile.read())