class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        M=len(s)
        if M==1:
            return True

        ptr1,ptr2=0,M-1
        while ptr1<=ptr2:
            if s[ptr1].isalnum() and s[ptr2].isalnum():
                if s[ptr1].lower()!=s[ptr2].lower():
                    return False
                else:
                    ptr1+=1
                    ptr2-=1
            else:
                if not s[ptr1].isalnum():
                    ptr1+=1
                if not s[ptr2].isalnum():
                    ptr2-=1
        return True