class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        a = []
        ptr_1 = 0
        ptr_2 = 0
        while ptr_1 < m and ptr_2 < n:
            if nums1[ptr_1] > nums2[ptr_2]:
                a.append(nums2[ptr_2])
                ptr_2 += 1
            else:
                a.append(nums1[ptr_1])
                ptr_1 += 1

        while ptr_1 < m:
            a.append(nums1[ptr_1])
            ptr_1 += 1

        while ptr_2 < n:
            a.append(nums2[ptr_2])
            ptr_2 += 1

        for i in range(m + n):
            nums1[i] = a[i]
