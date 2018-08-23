def twoSum(nums, target):
    dic = dict()
    a=0
    #for i in range(len(nums)):
#        dic[nums[i]]=i
    for i in nums:
        
        if target-i in dic:
            print([dic[target-i],a])
            return [dic[target-i],nums.index(i)]
        else:
            dic[i]=nums.index(i)
        a+=1
        

if __name__=="__main__":
    twoSum([3,3],6)
