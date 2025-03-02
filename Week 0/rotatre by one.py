
class Solution:
    def rotate(self, arr):
        last=[]
        last.append(arr[-1])
        first=arr[:-1]
        final=last+first
        return final
            
            
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        print("~")
        t -= 1