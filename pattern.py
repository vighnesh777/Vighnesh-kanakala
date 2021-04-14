def fucn(nums,t):
   i=0
   j=0
   if t in nums:
      if len(nums)==1:
         return [0,0]
      elif len(nums)>1 and nums.count(t)>1:
         while nums[i]<t:
            i+=1
         a=i
         while nums[a]==t:
            j+=1
         b=j
         l=[a,b]
         return l
nums1=[3,3,3]
t1=3
print(fucn(nums1,t1))