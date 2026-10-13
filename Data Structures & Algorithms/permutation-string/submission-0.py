from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = Counter(s1)
        window = {}
        
        have = 0
        need_count = len(need)
        
        l = 0
        
        for r in range(len(s2)):
            char = s2[r]
            
            # Add right character
            window[char] = window.get(char, 0) + 1
            
            # If frequency matches exactly
            if char in need and window[char] == need[char]:
                have += 1
            
            # Shrink window if size > len(s1)
            if r - l + 1 > len(s1):
                left_char = s2[l]
                
                if left_char in need and window[left_char] == need[left_char]:
                    have -= 1
                
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                
                l += 1
            
            # Check if all matched
            if have == need_count:
                return True
        
        return False