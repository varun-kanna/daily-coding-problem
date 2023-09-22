def sub(nums):
    #? What if we calculated the prefix and postfix sums. We make two arrays, one for the prefix and one for the postfix. Then we can multiply both the arrays to get the result.   
    # [1,2,3,4,5]
    # Prefix : 1, 1, 2, 6, 24
    # Postfix : 1, 5, 20, 60, 120
    prefix = []
    sum = 1
    for i in range(len(nums)):
        prefix.append(sum)
        sum *= nums[i]

    sum = 1
    postfix = []
    for i in range(len(nums) - 1, -1, -1):
        postfix.insert(0,sum)
        sum *= nums[i]

    sum = []
    for i in range(len(prefix)):
        sum.append(prefix[i] * postfix[i])
    return sum
   

print(sub([1,2,3,4,5]))
print(sub([3,2,1]))