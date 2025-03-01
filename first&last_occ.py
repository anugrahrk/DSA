# Given a sorted array arr with possibly some duplicates, the task is to find the first and last occurrences of an element x in the given array.
# Note: If the number x is not found in the array then return both the indices as -1.

# Examples:

# Input: arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
# Output: [2, 5]
# Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5
def ocuurence(arr,x):
    fisrt=lb(arr,x)
    last=ub(arr,x)
    return [fisrt,last]
    
def ub(arr,x):
    ans=-1
    l,h=0,len(arr)
    while l<=h:
        mid=(l+h)//2
        if arr[mid]<=x:
            ans=mid
            l=mid+1
        else:
            h=mid-1
    return ans
def lb(arr,x):
    ans=-1
    l,h=0,len(arr)
    while l<=h:
        mid=(l+h)//2
        if arr[mid]>=x:
            ans=mid
            h=mid-1
        else:
            l=mid+1
    return ans
if __name__=="__main__":
    arr=list(map(int,input("Enter the array with spaces in between each number:").split()))
    x=int(input("enter the element:"))
    print(ocuurence(arr,x))