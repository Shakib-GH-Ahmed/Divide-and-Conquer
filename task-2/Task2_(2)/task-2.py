inp=open("input2.txt","r")
out=open("output2.txt","w")

size1=int(inp.readline().strip())
l1=inp.readline().split()
size2=int(inp.readline().strip())
l2=inp.readline().split()
i=0
j=0
run=size1+size2
lst=[]
for idx in range(run):
    if i==size1:
        lst.append(l2[j])
        j+=1
    else:
        if j==size2:
            lst.append(l1[i])
            i+=1
        else:
            if int(l1[i]) < int(l2[j]):
                lst.append(l1[i])
                i+=1
            elif int(l2[j]) < int(l1[i]):
                lst.append(l2[j])
                j+=1
            elif int(l2[j]) == int(l1[i]):
                lst.append(l1[i])
                i+=1
for i in range(len(lst)):
    if i==len(lst)-1:
        out.write(f"{lst[i]}")
    else:
        out.write(f"{lst[i]} ")
    
inp.close()
out.close()
                
        