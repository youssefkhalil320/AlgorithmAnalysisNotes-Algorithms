nums = ['e','x','h','a','u','s','t','e','d']
def permuteUnique(nums):
        res = []
        perm  = []
        count =  {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] +=1
                    perm.pop()
        dfs()
        return res


print(permuteUnique(nums))
#answer should be 181440 