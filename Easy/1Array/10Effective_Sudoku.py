# 有效的数独
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

# 解题思路：逻辑题，理清逻辑即可

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s = set()
        for i in range(9):
        	# 判断每一行
        	for j in range(9):
        		if board[i][j] != '.' and board[i][j] in s:
        			return False
        		else:
        			s.add(board[i][j])
        	s.clear()
        	# 判断每一列
        	for k in range(9):
        		if board[k][i] != '.' and board[k][i] in s:
        			return False
        		else:
        			s.add(board[k][i])
        	s.clear()
        # 判断每一块
        for i in range(0, 9, 3):
        	for j in range(0, 9, 3):
        		for k in range(i ,i + 3):
        			for p in range(j, j + 3):
        				if board[k][p] != '.' and board[k][p] in s:
        					return False
        				else:
        					s.add(board[k][p])
        		s.clear()

        return True
        					