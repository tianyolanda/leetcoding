height = [1,8,6,2,5,4,8,3,7]

maxarea = 0
left = 0
right = len(height)-1
for i in range(len(height)-1):
    area_new = min(height[left], height[right]) * (right-left)
    maxarea = max(maxarea,area_new)
    if height[left] > height[right]:
        right -= 1
    else:
        left += 1
print(maxarea)