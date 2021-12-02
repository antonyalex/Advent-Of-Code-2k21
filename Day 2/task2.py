file = open("C:\\Users\\anton\\OneDrive\\Desktop\\input.txt", "r")
list = file.readlines()
forward,depth,aim=0,0,0
list2 = [s.strip('\n') for s in list] 
for l in list2:
    list3=l.split()
    if list3[0]=="forward":
        forward+=int(list3[1])
        depth+=aim*forward
    elif list3[0]=="down":
        aim+=int(list3[1])
    else:
        aim-=int(list3[1])
    list3=[]
print (forward*depth)
