from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.has_duplicate_element_in_rows(board):
            return False;

        if self.has_duplicate_element_in_columns(board):
            return False;

        sub_board_1 = [row[:3] for row in board[:3]]
        sub_board_1_1D= [item for row in sub_board_1 for item in row]
        if self.has_duplicate_element_in_row(sub_board_1_1D):
            return False;
        
        
        sub_board_2 = [row[3:6] for row in board[:3]]
        sub_board_2_1D= [item for row in sub_board_2 for item in row]
        if self.has_duplicate_element_in_row(sub_board_2_1D):
            return False;


        sub_board_3 = [row[6:9] for row in board[:3]]
        sub_board_3_1D= [item for row in sub_board_3 for item in row]
        if self.has_duplicate_element_in_row(sub_board_3_1D):
            return False;

        sub_board_4 = [row[:3] for row in board[3:6]]
        sub_board_4_1D= [item for row in sub_board_4 for item in row]
        if self.has_duplicate_element_in_row(sub_board_4_1D):
            return False;


        sub_board_5 = [row[3:6] for row in board[3:6]]
        sub_board_5_1D= [item for row in sub_board_5 for item in row]
        if self.has_duplicate_element_in_row(sub_board_5_1D):
            return False;


        sub_board_6 = [row[6:9] for row in board[3:6]]
        sub_board_6_1D= [item for row in sub_board_6 for item in row]
        if self.has_duplicate_element_in_row(sub_board_6_1D):
            return False;


        sub_board_7 = [row[:3] for row in board[6:9]]
        sub_board_7_1D= [item for row in sub_board_7 for item in row]
        if self.has_duplicate_element_in_row(sub_board_7_1D):
            return False;


        sub_board_8 = [row[3:6] for row in board[6:9]]
        sub_board_8_1D= [item for row in sub_board_8 for item in row]
        if self.has_duplicate_element_in_row(sub_board_8_1D):
            return False;


        sub_board_9 = [row[6:9] for row in board[6:9]]
        sub_board_9_1D= [item for row in sub_board_9 for item in row]
        if self.has_duplicate_element_in_row(sub_board_9_1D):
            return False;
        return True;

    def has_duplicate_element_in_row(self, row: [str])->bool:
      element_counts=dict();
      for element in row:
          if element in element_counts:
              element_counts[element]+=1
          else:
              element_counts[element]=1

      if '.' in element_counts:
          del element_counts['.']

      for count in element_counts.values():
          if count>1:
              return True
      return False

    def has_duplicate_element_in_rows(self, board)->bool:
        row_num=col_num=len(board)
        for i in range (row_num):
            has_duplicate=self.has_duplicate_element_in_row(board[i])
            if has_duplicate:
                return True
        return False

    def has_duplicate_element_in_columns(self, board)->bool:
        board_T = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
        row_num=col_num=len(board_T)
        for i in range (row_num):
            has_duplicate=self.has_duplicate_element_in_row(board_T[i])
            if has_duplicate:
                return True
        return False