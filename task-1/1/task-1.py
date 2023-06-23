#O(n^2) solution

inp=open("input1.txt","r")
out=open("output1.txt","w")

line1=inp.readline().split()
run=int(line1[0])
target=int(line1[1])
line2=inp.readline().split()
pos_lst=[]
count=0

for i in range(run):
    for j in range(i+1,run):
        if int(line2[i]) + int(line2[j]) == target:
            pos_lst.append([i+1,j+1])
            count+=1
if count == 0:
    out.write("IMPOSSIBLE")
for i in range(len(pos_lst)):
    out.write(f"{pos_lst[i][0]} {pos_lst[i][1]}")
    break

inp.close()
out.close()            