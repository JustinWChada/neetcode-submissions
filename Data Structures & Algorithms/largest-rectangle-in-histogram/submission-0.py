class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []  # stack of (height, start_index)
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            # Pop while current height is less than stack top
            while stk and height < stk[-1][0]:
                h, j = stk.pop()
                max_area = max(max_area, h * (i - j))
                start = j
            stk.append((height, start))

        # Clean up remaining stack
        while stk:
            h, j = stk.pop()
            max_area = max(max_area, h * (n - j))

        return max_area
