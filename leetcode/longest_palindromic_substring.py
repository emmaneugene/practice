# Given a string s, return the longest palindromic substring in s

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        
        for i in range(len(s) // 2):
            if s[i] != s[-1 - i]:
                return False
            
        return True
    
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
    
        start_idx: int = 0
        end_idx: int = len(s) 
        
        # Advance end pointer
        for i in range(1, len(s)):
            substr: str = s[start_idx: i+1]
            if self.isPalindrome(substr):
                result = substr if len(substr) > len(result) else result
            
        # Advance start pointer
        for i in range(1, len(s)):
            substr: str = s[i: end_idx]
            if self.isPalindrome(substr):
                result = substr if len(substr) > len(result) else result
        
        return result
        

# if __name__ == "__main__":
#     print(Solution.isPalindrome("hello"))
#     print(Solution.isPalindrome("abba"))
#     print(Solution.isPalindrome("abcelecba"))