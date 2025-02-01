
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i):
                print(" "*i,end="")
            for j in range(i+1):
                print("*"*((2*N)-1-(2*(i-1))),end="")
            for j in range(i):
                print(" "*i,end="")
            print()



if __name__ == '__main__':
    t = 1
    for _ in range(t):
        N = 3
        ob = Solution()
        ob.printTriangle(N)
        print("~")
