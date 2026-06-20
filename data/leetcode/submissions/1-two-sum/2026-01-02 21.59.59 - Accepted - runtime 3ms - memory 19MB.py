class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        M=len(nums)
        if M==2:
            return [0,1]
        
        map=defaultdict(list)
        for m in range(M):
            num=nums[m]
            map[num].append(m)

        for m in range(M):
            curr=nums[m]
            if target-curr in map:
                if target-curr==curr:
                    if len(map[curr])==2:
                        return map[curr]
                else:
                    return [m,map[target-curr][0]]
