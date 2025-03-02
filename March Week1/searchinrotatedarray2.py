# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.
def SA2(arr,k):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            return True
        if arr[low]==arr[mid] and arr[mid]==arr[high]:
            low+=1
            high-=1
            continue
        if arr[low]<=arr[mid]:
            if arr[low]<=k and k<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[high]>=k and arr[mid]<=k:
                low=mid+1
            else:
                high=mid-1
    return False
    


if __name__=="__main__":
    arr=[1,1,0,1,1,1,1,1]
    k=0
    print(SA2(arr,k))