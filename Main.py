from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  # Write code here
  array2 = [0 for i in range(m + n)]
    i = 0
    j = 0
    k = 0
    while i <= m and j <= n:
        if array[i] <= array[j]:
            array2[k] = array[i]
            i += 1
        else:
            array2[k] = array[j]
            j += 1
        k += 1
    if i > m:
        while j <= n:
            array2[k] = array[j]
            j += 1
            k += 1
    else:
        while i <= m:
            array2[k] = array[i]
            i += 1
            k += 1


# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
