# open file and store file object in a variable
files = open('Codingal.txt')

#read the contents of file
print(files.read())

# close the file
files.close()

# write operation

files = open('Codingal.txt', 'w')

print(files.write('I am a gamer,'))

files.close()

# append operation

files = open('Codingal.txt','a')

print(files. write(' I like to play fortnite'))

files.close()

# counting lines

file = open("Codingal.txt","r")
Counter = 0

Content = file.read()

CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1
        
print("This is the number of lines in the file")
print(Counter)
files.close()