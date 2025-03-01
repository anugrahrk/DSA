# Given a sorted array arr[] (with unique elements) and an integer k, find the index (0-based) of the largest element in arr[] that is less than or equal to k. This element is called the "floor" of k. If such an element does not exist, return -1.

# Examples

# Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 0
# Output: -1
# Explanation: No element less than 0 is found. So output is -1.

def floor(arr,k):
    if k==0:
        return -1
    l,h=0,len(arr)
    while l<=h:
        mid=(l+h)//2
        if arr[mid]<=k:
            l=mid+1
        else:
            h=mid-1
    return arr[h]
if __name__=="__main__":
    arr=list(map(int,input("Enter the elements in an array:").split()))
    k=int(input("enter the element:"))
    print(floor(arr,k))