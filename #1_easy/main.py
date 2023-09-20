nums = [10,15,3,7]
target = 18

#? O(n^2) since worst case we iterate through the nums in two nested for loops
# def two_sum():
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return True
#     return False

# print(two_sum())

#? O(n) space complexity and O(n) time complexity. Doing this in one pass will require additional memory, hashtable
# We want to find the complement of the current nums, calculated by sum-current num, if we find the complement anywhere in the array, we return True. We can use a hashset to store the complements. 

#nums = [10,15,3,7]
#nums = []
nums = [-1,55,-5,2]
target = -6

complement = set()
def two_sum():
    for i in nums:
        if i in complement:
            return True
        else:
            complement.add(target-i)
    return False

print(two_sum())