# Given a positive integer n, return the nth row of pascal's triangle.
# Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
# Examples:

# Input: n = 4
# Output: [1, 3, 3, 1]
# Explanation: 4th row of pascal's triangle is {1, 3, 3, 1}.
def Pascals(n):
    if n==1:
        return  [1]
    prev=Pascals(n-1)
    arr=[]
    arr.append(1)
    for i in range(1,len(prev)):
        arr.append(prev[i]+prev[i-1])
    arr.append(1)
    return arr
if __name__=="__main__":
    n=int(input())
    print(Pascals(n))