class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current_path: list[str]):
            # Base case: reached the end of digits
            if index == len(digits):
                result.append("".join(current_path))
                return
            
            # Get letters for current digit
            letters = digit_map[digits[index]]
            
            for letter in letters:
                current_path.append(letter)
                backtrack(index + 1, current_path)
                current_path.pop()  # Backtrack
                
        backtrack(0, [])
        return result