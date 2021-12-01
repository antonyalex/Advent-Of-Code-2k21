file=open("input.txt","r")
list=file.readlines()
c=0
list2 =[s.strip('\\n') for s in list] and [int(s) for s in list]
list3=[]
for j in range(len(list2)-2):
    a=list2[j]+list2[j+1]+list2[j+2]
    list3.append(a)
    a=0

for i in range(len(list3)-1):
    if(list3[i+1]>list3[i]):
        c+=1
print (c)