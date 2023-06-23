inp=open("input3.txt","r")
out=open("output3.txt","w")

line1=int(inp.readline().strip())
lst=inp.readline().split()

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid=len(lst)//2
        left_subarray=mergesort(lst[0:mid])
        right_subarray=mergesort(lst[mid:])
        return merge(left_subarray,right_subarray)  

def merge(l,r):
    new=[]
    i=0
    j=0
    while i < len(l) and j < len(r):
        if int(l[i]) < int(r[j]):
            new.append(l[i])
            i+=1
        else:
            new.append(r[j])
            j+=1
    new=new+l[i:]+r[j:]
    return new
        
    
sorted_lst=mergesort(lst)

for i in range(len(sorted_lst)):
    if i == len(sorted_lst)-1:
        out.write(f"{sorted_lst[i]}")
    else:
        out.write(f"{sorted_lst[i]} ")
           
inp.close()
out.close()