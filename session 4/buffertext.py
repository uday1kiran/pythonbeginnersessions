inputFile = open('myfile.txt','r')
outputFile = open('myoutput-file.txt','w')

msg = inputFile.read(10)#10 bytes

while len(msg):#non-zero value check
    outputFile.write(msg+"\n")
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()
