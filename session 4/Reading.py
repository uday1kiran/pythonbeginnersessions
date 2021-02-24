f = open('myfile.txt','r')#r,w,a,r+
firstline = f.readline()
secondline = f.readline()
print(firstline,secondline,sep="")
f.close()
