Dynamic programming is a technique where solutions to subproblems are stored in memory and used to quickly find the solution to the full problem.

The longest common substring problem is solved efficiently using dynamic programming. A matrix, a list of lists, stores the length of the longest common substring found in two strings as the strings' characters are examined. Matrix element (i, j) is assigned with zero if the first string's ith character doesn't match the second string's jth character. If the two characters do match, then matrix element (i, j) is assigned with the matrix element (i-1, j-1) +1.

Note that string slices in Python use the syntax str1[ start_index : end_index + 1 ] to get the substring from start_index up to and including end_index.

As the matrix fills in, only the previous row is needed to fill the current row. Thus, the only space required is two rows, plus the variables for the length and row of the longest substring found so far. In fact, once a value is used as an up_left value, the row element can be overwritten as part of the current row. Thus, only a single row is truly needed — the values before the current column are the current row's values, while values after the current column are the previous row's values. Ex: The current column is index 4 with the following row. The indices 0 - 3 (colored green) are from the current row, and indices 4 - 8 (colored red) are from the previous row.

