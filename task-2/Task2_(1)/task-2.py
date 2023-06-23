inp=open("input2.txt","r")
out=open("output2.txt","w")

num1=int(inp.readline().strip())
lst1=inp.readline().split()
num2=int(inp.readline().strip())
lst2=inp.readline().split()
lst3=lst1+lst2

def mergesort(lst3):
    if len(lst3) <= 1:
        return lst3
    else:
        left_sub=mergesort(lst3[0:len(lst3)//2])
        right_sub=mergesort(lst3[len(lst3)//2:len(lst3)])
        return merge(left_sub,right_sub)

def merge(l,r):
    new=[]
    i=0 #left sub index
    j=0 #right sub index
    while i < len(l) and j < len(r):
        if int(l[i]) < int(r[j]):
            new.append(l[i])
            i+=1
        else:
            new.append(r[j])
            j+=1
    new+=l[i:]+r[j:]
    return new

sort_lst=mergesort(lst3)

for i in range(len(sort_lst)):
    if i == len(sort_lst)-1:
        out.write(f"{sort_lst[i]}")
    else:
        out.write(f"{sort_lst[i]} ")
        
inp.close()
out.close()