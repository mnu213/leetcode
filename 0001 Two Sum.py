class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for x in range(len(nums)):
            h[nums[x]] = x
            
        for x in range(len(nums)):
            if target - nums[x] in h:
                if h[target - nums[x]] == x:
                    print()
                else:
                    return [x,h[target-nums[x]]]
        
        '''
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x == y:
                    print()
                elif nums[x] + nums[y] == target:
                    return [x,y]
'''              
            
