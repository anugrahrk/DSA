class Solution:
    def inversionCount(self, arr):
        n = len(arr)
        return self.mergeSort(arr, 0, n - 1)

    def merge(self, arr, low, mid, high):
        count = 0
        left = low
        right = mid + 1
        temp = []
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid - left + 1)
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        return count

    def mergeSort(self, arr, low, high):
        count = 0
        if low >= high:
            return count
        mid = (low + high) // 2
        count += self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid + 1, high)
        count += self.merge(arr, low, mid, high)
        return count

# Driver code to test the function
if __name__ == "__main__":
    arr = [2, 3, 8, 6, 1]
    sol = Solution()
    result = sol.inversionCount(arr)
    print("Number of inversions:", result)
