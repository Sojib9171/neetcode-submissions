class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      char_freq_count_list=[]
      
      for words in strs:
        char_freq_count=[0]*26
        for char in words:
          char_freq_count[ord(char)-ord('a')]+=1
        char_freq_count_list.append(char_freq_count)
        
      output_dict={}
      for i in range(len(char_freq_count_list)):
        if tuple(char_freq_count_list[i]) in output_dict:
          output_dict[tuple(char_freq_count_list[i])].append(strs[i])
        else:
          output_dict[tuple(char_freq_count_list[i])]=[strs[i]]

      output_list=list(output_dict.values())
      return output_list