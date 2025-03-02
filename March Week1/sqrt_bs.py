# Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.

# Floor value of any number is the greatest Integer which is less than or equal to that number

# Examples:

# Input: n = 4
# Output: 2
# Explanation: Since, 4 is a perfect square, so its square root is 2.
def sqrt(n):
    l,h=0,n
    ans=-1
    while l<=h:
        mid=(l+h)//2
        if mid*mid<=n:
            ans=mid
            l=mid+1
        else:
            h=mid-1
    return ans

if __name__=="__main__":
    n=int(input("enter the Number:"))
    print(sqrt(n))
