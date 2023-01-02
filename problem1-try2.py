import bisect
class Solution:
    def answerQueries(nums=[],queries=[]):

        nums.sort()
        # print(nums)

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            # print(nums)

        answer = []

        for query in queries:
            index = bisect.bisect_right(nums, query)
            answer.append(index)

        return answer
print(Solution.answerQueries([4, 5, 2, 1],[3, 10, 21]))