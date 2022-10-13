class PrefixSum:
# Prefixes must be contiguous blocks that begin at index 0
# Postfix are the same except begin at the last index

# Prefixes generaly used to avoid repeated work

# Q. Given an array of values, design a data structure that can query the sum of a subarray of the values

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)
