# Find the length of longest subarray with the same
# value in each position: O(n)
def longestSubarray(nums):
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:      # if left value not equal to right value
            L = R                   # set left pointer to right pointer
        length = max(length, R - L + 1)
    return length

### Try to rewrite the solution above without left and right pointers   ###
# Need to see if this works
    # length = 0
    #
    # for num in range(len(nums)-1):
    #     if nums[num] == nums[num+1]:
    #         length += 1
    #     else:
    #         length = 0

# Find length of the minimum size subarray where the sum is
# greater than or equal to the target.
# Assume all values in the input are positive.
# O(n)
def shortestSubarray(nums, target):
    L, total = 0, 0
    length = float("inf")       # set high since want to minimize
                                # can also set to len(num) + 1

    for R in range(len(nums)):
        total += nums[R]        # add value to sum
        while total >= target:  # perform this while the sum is above the target value
            length = min(R - L + 1, length)     # capture min of current window size and record min window size
            total -= nums[L]                    # reduce total sum by value at left pointer
            L += 1                              # increment left pointer
    return 0 if length == float("inf") else length