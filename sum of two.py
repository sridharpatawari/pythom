nums=[2,7,11,15]
target=9
def twoSum(nums, target):
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    a.append(i)
                    a.append(j)
                    return a
print(twoSum(nums,target))