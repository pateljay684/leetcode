
# coding: utf-8

# In[3]:


nums=[2, 7, 11, 15]
target = 9
if len(nums) <= 1:
    print("False")
buff_dict = {}
for i in range(len(nums)):
    if nums[i] in buff_dict:
        print([buff_dict[nums[i]], i])
    else:
        buff_dict[target - nums[i]] = i

