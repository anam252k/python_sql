'''f=open("demofile.txt","r")

print(f.readline())
print(f.readline())'''

'''f=open("demofile.txt","a")
f.write("more content")
f.close'''

'''import os
os.remove("demofile.txt")'''


'''f=open("file.txt","r")
f2=open("file2.txt","w")


j=1
for i in f:
    print(j,i)

    c=str(j) +i

    f2.write(c)
    j=j+1'''


f=open("file.txt","r")
f2=open("file2.txt","w")


j=['1\n','2\n','3\n','4\n']

for i in f:
    print(i)
    
    f2.write(i)
f2.writelines(j)
    #f2.writelines(j)
    #j=j+1



    



    


