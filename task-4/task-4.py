inp=open("input4.txt","r")
out=open("output4.txt","w")

line1=int(inp.readline().strip())
lst=inp.readline().split()

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        left_subarr=find_max(lst[0:len(lst)//2])
        right_subarr=find_max(lst[len(lst)//2:len(lst)])
        
        return max(int(left_subarr),int(right_subarr))
        

store_max=find_max(lst)
out.write(f"{store_max}")

inp.close()
out.close()

#Here, we consider the divide and conquer method by dividing the list into two subarrays, and for the division, it takes the size of n/2.
#After that, we recursively approach the maximum element in that subarray.
# T(n)=2*T(n/2)
#So, we can say the time complexity of this divide and conquer method is O(nlogn).(There are logn levels in the recursion tree and multiplying with n it gets- nlogn)