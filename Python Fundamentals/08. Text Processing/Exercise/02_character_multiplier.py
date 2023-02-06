word1, word2 = input().split()
nums1 = [ord(num) for num in word1]
nums2 = [ord(num) for num in word2]
result = 0
if len(nums1) > len(nums2):
    for index1 in range(len(nums2)):
        result += nums1[index1] * nums2[index1]
    for num1 in nums1[len(nums2): len(nums1)]:
        result += num1
elif len(nums2) > len(nums1):
    for index2 in range(len(nums1)):
        result += nums1[index2] * nums2[index2]
    for num2 in nums2[len(nums1): len(nums2)]:
        result += num2
else:
    for index in range(len(nums1)):
        result += nums1[index] * nums2[index]

print(result)