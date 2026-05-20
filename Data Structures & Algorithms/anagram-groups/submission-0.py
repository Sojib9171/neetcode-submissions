class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      sorted_str_list=[]
      for i in range(len(strs)):
        sorted_str=sorted(strs[i])
        sorted_str_list.append("".join(sorted_str))
        
      output_dict={}
      for i in range(len(sorted_str_list)):
        if sorted_str_list[i] in output_dict:
          output_dict[sorted_str_list[i]].append(i)
        else:
          output_dict[sorted_str_list[i]]=[i]

      index_lists=list(output_dict.values())
      output_list=[]
      for indexes in index_lists:
        str_list=[]
        for index in indexes:
          str_list.append(strs[index])
        output_list.append(str_list)

      return output_list