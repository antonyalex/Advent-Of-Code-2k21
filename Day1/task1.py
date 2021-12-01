file=open("input.txt","r")
list=file.readlines()
c=0
list2 =[s.strip('\n') for s in list] and [int(s) for s in list]
for i in range(len(list2)-1):
    if(list2[i+1]>list2[i]):
        c+=1
print (c)
