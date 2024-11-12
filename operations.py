coding = open("codingal.txt")

# print(coding.read())
print(coding.readlines())

coding.close()

#removing the lines starting with coding

file1 = open('Codingal.txt','r')
file2 = open('new.txt', 'w')

for line in file1.readlines():
    
    if not (line.startswith('Coding')):
        
        print(line)
        
        file2.write(line)
        
file2.close()
file1.close()