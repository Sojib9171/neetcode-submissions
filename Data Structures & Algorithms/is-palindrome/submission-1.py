import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        validString=re.sub('[^A-Za-z0-9]+', '', s)
        validString=validString.lower()
        for i in range(len(validString)):
            j=len(validString)-i-1
            if i<=j:
                if validString[i]!=validString[j]:
                    return False
        return True
        