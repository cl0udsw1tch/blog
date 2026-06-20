class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        M,N=len(ransomNote),len(magazine)

        if M==1 and N==1: return ransomNote==magazine

        char_dict=defaultdict(int)
        for c in magazine:
            char_dict[c]+=1

        for c in ransomNote:
            if char_dict[c]==0: return False
            char_dict[c]-=1
        return True