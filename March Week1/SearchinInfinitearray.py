# Problem statement
# You are given an infinite array consisting of only ones and zeroes, in sorted order. You have to find the index of the first occurrence of 1.

# Example:
# If the array is 0 0 0 0 1 1 1 1… then, the first occurrence of 1 will be at index 4 therefore the answer here is 4.
# Note:
# As the array size is infinite, the actual array won’t be given to you. Instead, you will be able to access the array elements by calling a method named ‘get’.

# get(i) : returns the value present at index I.

# Indexing is 0-based. 

# Instead of representing an infinite array in the input, we give the index of the first occurrence of 1 in the input itself. However, this input will be completely hidden from the user.
def InfArr(arr):
    low=0
    high=1
    while arr[high]==0:
        low=high
        high*=2
    while low<high:
        mid=low+(high-low)//2
        if arr[mid]==1:
            high=mid
        else:
            low=mid+1
    return low
if __name__=="__main__":
    arr=[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(InfArr(arr))

