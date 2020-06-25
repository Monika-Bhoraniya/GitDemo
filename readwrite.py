
#file = open('test.txt')   #read or write text file
#print(file.read(11))
#file.close()

#print(file.readline())
#print(file.readline())
#print(file.readline())


#line = file.readline()
#while line!= "":
 #   print(line)
  #  line = file.readline()

#for line in file.readlines():
  #    print(line)

  #write file.......
with open('test.txt', 'r')as reader:   #read mode file ' '
    content = reader.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)



