class Solution:
    def searchRange(self, nums, target):
#nums type list[int] ---sorted
#target type int'''
        i=0
        length=len(nums)
        count=nums.count(target)
        if target in nums:
            if length==1:
                return [0,0]
            elif length>1 and count>1:
                while nums[i]<target:
                    i+=1
                b=i+(count-1)
                l=[i,b]
                return l
            elif count==1:
                a1=nums.index(target)
                l=[a1,a1]
                return l
        else:
            return [-1,-1]
#Driver Code
'''d=Solution()
lis=list(map(int,input().split()))
t=int(input())
print(d.searchRange(lis,t))
'''