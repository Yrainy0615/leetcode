"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""

"""
方法一：
解题关键主要是想找到 num2 = target - num1，是否也在 list 中，那么就需要运用以下两个方法：
num2 in nums，返回 True 说明有戏
nums.index(num2)，查找 num2 的索引
"""
class Solution(object):
    def twosum1(self,nums,target):
        lens = len(nums)
        j = -1
        for i in range(lens):
            # 存在符合条件的数
            if (target - nums[i]) in nums:
                #如果num2=num1,且nums中只出现了一次，说明找到是num1本身(.count输出出现次数)
                if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):
                    continue
                else:
                    # index(x,i+1)是从num1后的序列后找num2,返回索引
                    j = nums.index(target - nums[i],i+1)
                    break
        if j > 0:
            return [i,j]
        else:
            return []
    """
    方法二：
    通过哈希来求解，这里通过字典来模拟哈希查询的过程
    个人理解这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤。
    """
    def twosum2(self,nums,target):
        hashmap = {}
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        #ind是索引，num是值
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            #Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值(none)。
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return[i,j]
    """
    方法三：
    这样写更直观，遍历列表同时查字典
    """
    def twosum3(self,nums, target):
        dct = {}
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i


nums = [2, 7, 11, 5]
target = 9
s = Solution()
sum1 = s.twosum1(nums,target)
sum2 = s.twosum2(nums,target)
sum3 = s.twosum3(nums,target)
print(sum1)
print(sum2)
print(sum3)