class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_sum_s=0;
        hash_sum_t=0;

        for i in range(len(s)):
            hash_sum_s+=hash(s[i])

        for i in range(len(t)):
            hash_sum_t+=hash(t[i])

        if hash_sum_s==hash_sum_t:
            return True

        return False
        