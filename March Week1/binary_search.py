# Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 6], k = 6
# Output: true
# Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.
def BS(arr,k):
    low,high=0,len(arr)-1
    while low<=high:
        mid=low+high//2
        if arr[mid]==k:
            return True
        elif arr[mid]<k:

            low=mid+1
        else:
            high=mid-1
    return False
if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    k=int(input("enter the element to be searched:"))
    print(BS(arr,k))