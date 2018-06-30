def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    #for i in range(len(nums)):
        #for j in range(i+1,len(nums)):
            #if nums[i] + nums[j] == target:
                #return [i,j]

    d = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in d.keys():
            return [d[complement],i]
        d[nums[i]]=i
    
print(twoSum([2,7,11,15],9))
