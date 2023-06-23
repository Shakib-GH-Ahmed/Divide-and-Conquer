#O(n) solution

inp=open("input1.txt","r")
out=open("output1.txt","w")

line1=inp.readline().split()
run=int(line1[0])
target=int(line1[1])
line2=inp.readline().split()
pos_lst=[]
count=0
i=0
j=i+1
for idx in range(run):
    if i !=len(line2) and j!=len(line2):
        if int(line2[i]) + int(line2[j]) == target:
            pos_lst.append([i+1,j+1])
            i+=1
            j+=1
            count+=1
        else:
            j+=1
    
if count == 0:
    out.write("IMPOSSIBLE")
    
for i in range(len(pos_lst)):
    out.write(f"{pos_lst[i][0]} {pos_lst[i][1]}")
    break  #so that only the first value will show up in the output.

inp.close()
out.close()         