1.14 LAB: Longest common subsequences

# Overview

Unlike a substring, a subsequence need not be continuous.  

**Example:** `"ARTS"` is a subsequence of `"ALGORITHMS"`, but it is not a substring.

## Dynamic Programming Matrix

A dynamic programming matrix can be used to solve the longest common subsequence problem. Rules for populating the matrix differ slightly from the longest common substring algorithm.  

Both algorithms populate rows from **top to bottom**, and **left to right** across a row. Each entry `matrix[R][C]` is computed as follows:

- **If characters match:**  
  `matrix[R][C] = 1 + matrix[R - 1][C - 1]`

- **If characters do not match:**  
  - Substring algorithm: `matrix[R][C] = 0`  
  - Subsequence algorithm: `matrix[R][C] = max(matrix[R - 1][C], matrix[R][C - 1])`

- **Out of bounds entries:**  
  Use `0`.  
  Example: When computing `matrix[0][0]` for a character match, instead of accessing `matrix[-1][-1]`, use `0`.

## Sample Matrix

The following shows the longest common subsequence matrix for strings `"ALASKAN"` and `"BANANAS"`. Entries corresponding to a character match are highlighted.

**7×7 matrix entries:**

- Row 0: `0, 1, 1, 1, 1, 1, 1`  
- Row 1: `0, 1, 1, 1, 1, 1, 1`  
- Row 2: `0, 1, 1, 2, 2, 2, 2`  
- Row 3: `0, 1, 1, 2, 2, 2, 3`  
- Row 4: `0, 1, 1, 2, 2, 2, 3`  
- Row 5: `0, 1, 1, 2, 2, 3, 3`  
- Row 6: `0, 1, 2, 2, 3, 3, 3`

![alt text](image-1.png)

➡️ The **largest number** in the matrix indicates the length of the longest common subsequence.  
Example: The largest entry above is `3`, so the LCS between `"ALASKAN"` and `"BANANAS"` is **3 characters long**.

## Multiple Longest Common Subsequences

A pair of strings may have more than one LCS.  

**Example:** `"ALASKAN"` and `"BANANAS"` have three longest common subsequences:  
- `"AAA"`  
- `"AAN"`  
- `"AAS"`

## Step 1: Building the LCS Set

The matrix can be used to build a set of all longest common subsequences. Two approaches:

1. **Build the entire numerical matrix**, then traverse it to build the LCS set.  
2. **Build a matrix of structures** that include both the numerical entry and the LCS set.  

![alt text](image-2.png)

**Example (Approach #2):**  
4×4 LCS matrix for strings `"BAAB"` and `"ABBA"`. Each entry has both a number and a string set.

- Row 0: `(0, {}), (1, {B}), (1, {B}), (1, {B})`  
- Row 1: `(1, {A}), (1, {A,B}), (1, {A,B}), (2, {BA})`  
- Row 2: `(1, {A}), (1, {A,B}), (1, {A,B}), (2, {AA,BA})`  
- Row 3: `(1, {A}), (2, {AB}), (2, {AB,BB}), (2, {AB,BB,AA,BA})`

## Step 2: Implementing the `LCSMatrix` Class

The `LCSMatrix` class is declared in **LCSMatrix.py**.  
The following methods must be completed:

- **Attributes:**  
  - Add an attribute for the matrix data.  
  - Each entry may be an integer or a more complex object, depending on the chosen approach.

- **`__init__()`**  
  - Two lines of code are provided to assign `row_count` and `column_count` to the lengths of `string1` and `string2`.  
  - Implement the remainder to build the LCS matrix.  
  - Use **case-sensitive** comparisons (`'a'` ≠ `'A'`).

- **`get_entry()`**  
  - Returns the numerical entry at the given row and column indices.  
  - Returns `0` if either index is out of bounds.

- **`get_longest_common_subsequences()`**  
  - Returns a Python `set` object containing all longest common subsequences for the two strings passed to `__init__()`.

## Step 3: Testing

- Test the implementation in **develop mode**.  
- Once verified, **submit** your solution.