import numpy as np
with open("input.txt") as f:
    input = f.read()
input_lines = input.split('\n')
lines = [line.split(' -> ') for line in input_lines]
sea_bed = np.zeros([1000, 1000])
for line in lines:
    x1,y1=map(int,line[0].split(','))
    x2,y2=map(int,line[1].split(','))
    if x1 == x2:
        if y1 < y2:
            y_range = range(y1, y2+1)
        else: 
            y_range = range(y2, y1+1)
        for y in y_range:
            sea_bed[y][x1] += 1
    elif y1==y2:
        if x1>x2:
            x_range=range(x2,x1+1)
        else:
            x_range=range(x1,x2+1)
        for x in x_range:
            sea_bed[y1][x]+=1
    else:
        if x1<x2 and y1<y2:
            x_range=range(x1,x2+1)
            y_range=range(y1,y2+1)
        elif x1<x2 and y1>y2:
            x_range=range(x1,x2+1)
            y_range=range(y1,y2-1,-1)
        elif x1>x2 and y1>y2:
            x_range=list(range(x2,x1+1))
            y_range=range(y2,y1+1)
        else:
            x_range=range(x1,x2-1,-1)
            y_range=range(y1,y2+1)
        for index,x in enumerate(x_range):
            sea_bed[y_range[index]][x]+=1


print(np.count_nonzero(sea_bed > 1))
   


    