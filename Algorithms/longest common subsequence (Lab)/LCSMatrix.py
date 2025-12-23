# Your code here
# Declare any desired classes to be used by LCSMatrix

class LCSMatrix:
    def __init__(self, str1, str2):
        self.row_count = len(str1)
        self.column_count = len(str2)
        # Your code here
        self.str1 = str1
        self.str2 = str2
        self.matrix = [[0] * (self.column_count + 1) for _ in range(self.row_count + 1)]
        for i in range(1, self.row_count + 1):
            for j in range(1, self.column_count + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    self.matrix[i][j] = self.matrix[i - 1][j - 1] + 1
                else:
                    self.matrix[i][j] = max(self.matrix[i - 1][j], self.matrix[i][j - 1])
    
    # Returns the number of columns in the matrix, which also equals the length
    # of the second string passed to the constructor.
    def get_column_count(self):
        return self.column_count
    
    # Returns the matrix entry at the specified row and column indices, or 0 if
    # either index is out of bounds.
    def get_entry(self, row_index, column_index):
        # Your code here (remove placeholder line below)
        if 0 <= row_index <= self.row_count and 0 <= column_index <= self.column_count:
            return self.matrix[row_index + 1][column_index + 1]
        else:
            return 0
    
    # Returns the number of rows in the matrix, which also equals the length
    # of the first string passed to the constructor.
    def get_row_count(self):
        return self.row_count
    
    # Returns the set of distinct, longest common subsequences between the two
    # strings that were passed to the constructor.
    def get_longest_common_subsequences(self):
        # Your code here (remove placeholder line below)
        def backtrack(i, j, current):
            if i == 0 or j == 0:
                return {current[::-1]}  # Reverse and return as set
            
            if self.str1[i - 1] == self.str2[j - 1]:
                return backtrack(i - 1, j - 1, current + self.str1[i - 1])
            else:
                results = set()
                if self.matrix[i - 1][j] >= self.matrix[i][j - 1]:
                    results.update(backtrack(i - 1, j, current))
                if self.matrix[i][j - 1] >= self.matrix[i - 1][j]:
                    results.update(backtrack(i, j - 1, current))
                return results
    
        if self.matrix[self.row_count][self.column_count] == 0:
            return set()
        
        return backtrack(self.row_count, self.column_count, "")