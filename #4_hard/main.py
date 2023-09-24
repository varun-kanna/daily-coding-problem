def firstMissingPositiveNumber(nums):
    #? Use a set. O(n) time complexity and O(n) space complexity
    nums_set = set(nums)
    print(nums_set)
    for i in range(1, len(nums) + 1):
        print(i)
        if i not in nums_set:
            return i
    # If nums sequence is 1 - len(nums)
    return len(nums) + 1

# Basically if the index (first number) isn't in the nums_set, we return the index. This is because if we get to the index, that indicates that the index should be the smallest possible positive integer.

# If all numbers in the range are in the solution range, the smallest positive integer is len(nums) + 1.
# We use a set to ensure we only look at unique elements.
print(firstMissingPositiveNumber([1,3,4,-1,1]))
#print(firstMissingPositiveNumber([1,2,0]))
#print(firstMissingPositiveNumber([1,2,0,4,3]))