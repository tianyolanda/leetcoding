nums1 = [1,2,3,7,0,0,0]
m = 4
nums2 = [2,5,6]
n = 3
j = 0
i = 0
count = 0
while count < m and j < n:
    l_j = 0
    nowi = nums1[i]
    while j < n and nowi > nums2[j]:
        nums1.insert(i + l_j, nums2[j])
        j += 1
        l_j += 1
    i += 1 + l_j
    count += 1
if j < n:
    nums1[i: i + n - j] = nums2[j:n]
del nums1[i + n - j:]

print(nums1)
