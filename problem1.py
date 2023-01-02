class Solution:
    def answerQueries(nums=[],queries=[]):
        nums.sort()
        ans =[]

        for query in queries:
            count = 0
            for num in nums:
                if query >= num:
                    query -= num
                    count += 1

                else:
                    break
            ans.append(count)

        return ans

print(Solution.answerQueries([4, 5, 2, 1],[3, 10, 21]))