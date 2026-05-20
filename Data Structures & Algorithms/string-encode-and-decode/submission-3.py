class Solution:
    def encode(self, strs: List[str]) -> str:
      encoded_str=""
      for s in strs:
        length=len(s)
        encoded_str+=str(length)+"#"+s
      return encoded_str

    def decode(self, s: str) -> List[str]:
      decoded_str=[]
      j=0
      for i in range(len(s)):
        if s[i]=='#' and s[i-1].isdigit():
          l=int(s[j:i])
          j=i+l+1
          decoded_str.append(s[i+1: i+1+l])
      return decoded_str
