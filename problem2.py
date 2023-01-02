class Solution:
    def twoSum( nums = [2,7,11,15] ,target=[9]):
        nums.sort()
        # sum = []
        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):

                x = [nums[i]+nums[j]]
                # print(x)



                if x == target:
                    # print("Heloo")
                    return [i, j]
                else:
                    break
print(Solution.twoSum())