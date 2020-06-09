"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


class Solution:
    """
    方法一：滑动窗口
    使用两个指针表示字符串中的某个子串（的左右边界）。其中左指针代表枚举子串的起始位置，右指针为rk
    在每一步的操作中，将左指针向右移动一格，表示枚举下一个字符作为起始位置，
    然后不断地向右移动右指针，但需要保证这两个指针对应的子串中没有重复的字符，
    在移动结束后，这个子串就对应以左指针开始的，不包含重复字符的最长子串，记录下这个子串的长度。
    """
    def lengthOfLongestSubstring1(self, k: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(k)
        # 右指针，初始值为 -1，相当于字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(k[i - 1])
            while rk + 1 < n and k[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(k[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
    """
    方法二：动态规划
    已知字符串S1='abcc'，其最长无重复子串是'abc'，问字符串S2='abccd'的最长无重复子串长度是什么？
    S1结尾加上'd'之后，最长无重复子串有两种可能的来源：
    最长无重复子串包含新增的'd'，即'cd'
    最长无重复子串不包含新增的'd'，即S1的最长无重复子串'abc'
    比较'cd'与'abc'，len('abc')>len('cd')，所以S2的最长无重复子串依然是'abc'
    根据例子的思路推广至一般的情况：
     给出一个字符串Si，已知它的最长子串长度为Li，如果在Si的末尾追加一个字符C
     lengthOfLongestSubString(Si+1)=max(Li,len(C结尾的无重复子串))
    """
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        def find_left(s, i):
            tmp_str = s[i]
            j = i - 1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)

        length = 0
        for i in range(0, len(s)):
            length = max(length, find_left(s, i))
        return length


k = 'abcabbccabcca'
s = Solution()
ans1 = s.lengthOfLongestSubstring1(k)
ans2 = s.lengthOfLongestSubstring2(k)

print(ans1)
print(ans2)



       