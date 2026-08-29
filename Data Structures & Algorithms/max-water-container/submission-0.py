class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        i = 0
        j = n-1
        area = 0

        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            n_area = height * width
            area = max(area, n_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
        return area
            