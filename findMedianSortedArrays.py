"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
:type nums1: List[int]
:type nums2: List[int]
:rtype: float
"""


class Solution:
    def findMedianSortedArrays1(self, nums1, nums2) -> float:
        def getKthElement(k):
            """
            方法一：二分查找
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

    def findMedianSortedArrays2(self, nums1, nums2) -> float:
        """
        方法二：归并排序
        这题很自然地想到归并排序，再取中间数，但是是nlogn的复杂度，题目要求logn
        所以要用二分法来巧妙地进一步降低时间复杂度
        思想就是利用总体中位数的性质和左右中位数之间的关系来把所有的数先分成两堆，然后再在两堆的边界返回答案
        """
        m = len(nums1)
        n = len(nums2)
        # 让nums2成为更长的那一个数组
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # 如果两个都为空的异常处理
        if n == 0:
            raise ValueError

        # nums1中index在imid左边的都被分到左堆，nums2中jmid左边的都被分到左堆
        imin, imax = 0, m

        # 二分答案
        while (imin <= imax):
            imid = imin + (imax - imin) // 2
            # 左堆最大的只有可能是nums1[imid-1],nums2[jmid-1]
            # 右堆最小只有可能是nums1[imid],nums2[jmid]
            # 让左右堆大致相等需要满足的条件是imid+jmid = m-imid+n-jmid 即 jmid = (m+n-2imid)//2
            # 为什么是大致呢？因为有总数为奇数的情况，这里用向下取整数操作，所以如果是奇数，右堆会多1
            jmid = (m + n - 2 * imid) // 2

            # 前面的判断条件只是为了保证不会index out of range
            if (imid > 0 and nums1[imid - 1] > nums2[jmid]):
                # imid太大了，这是里精确查找，不是左闭右开，而是双闭区间，所以直接移动一位
                imax = imid - 1
            elif (imid < m and nums2[jmid - 1] > nums1[imid]):
                imin = imid + 1
            # 满足条件
            else:
                # 边界情况处理，都是为了不out of index
                # 依次得到左堆最大和右堆最小
                if (imid == m):
                    minright = nums2[jmid]
                elif (jmid == n):
                    minright = nums1[imid]
                else:
                    minright = min(nums1[imid], nums2[jmid])

                if (imid == 0):
                    maxleft = nums2[jmid - 1]
                elif (jmid == 0):
                    maxleft = nums1[imid - 1]
                else:
                    maxleft = max(nums1[imid - 1], nums2[jmid - 1])

                # 前面也提过，因为取中间的时候用的是向下取整，所以如果总数是奇数的话，
                # 应该是右边个数多一些，边界的minright就是中位数
                if ((m + n) % 2) == 1:
                    return minright

                    # 否则我们在两个值中间做个平均
                return (maxleft + minright) / 2




nums1 = [1,4,6,7]
nums2 = [3,9,10]
s = Solution()
ans1 = s.findMedianSortedArrays1(nums1,nums2)
ans2 = s.findMedianSortedArrays2(nums1,nums2)
print(ans1)
print(ans2)

