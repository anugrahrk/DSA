class Solution:
    def Factorial(self,N):
        if N==0 or N==1:
            return 1
        else:
            return N*self.Factorial(N-1)
if __name__=="__main__":
    sol=Solution()
    N=5
    print("Factorial of",N,"is:",sol.Factorial(N))
