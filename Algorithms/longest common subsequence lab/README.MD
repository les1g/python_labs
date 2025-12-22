# **Goal of lab:**

Understand **how dynamic programming is used to compute the Longest Common Subsequence (LCS)** and implement a class (`LCSMatrix`) that:

- Builds the LCS DP matrix correctly  
- Returns individual matrix entries  
- Returns **all** longest common subsequences, not just the length  

The real purpose of the lab is to ensure you can **apply dynamic programming**, **store structured matrix data**, and **return correct results through class methods**, not just print output.

---

# **Key class to implement:**

`LCSMatrix(string1, string2)`

This class must:

- Build the LCS matrix using DP rules  
- Store matrix entries (integers or structures)  
- Provide access to matrix values  
- Generate the full set of LCS strings  

---

# **Core behavior required:**

### **Dynamic Programming Rules**

- **If characters match:**  
  `matrix[R][C] = 1 + matrix[R-1][C-1]`

- **If characters do NOT match:**  
  `matrix[R][C] = max(matrix[R-1][C], matrix[R][C-1])`

- **Out-of-bounds:**  
  Use `0`

### **Methods you must implement**

#### **`__init__()`**
- Build the entire DP matrix  
- Use case‑sensitive comparisons  
- Optionally store sets of subsequences in each cell (approach #2)

#### **`get_entry(row, col)`**
- Return the **numeric** DP value  
- Return `0` if out of bounds  

#### **`get_longest_common_subsequences()`**
- Return a **Python set** of all LCS strings  
- Must include *every* valid LCS (e.g., `"AAA"`, `"AAN"`, `"AAS"`)

---

# **Grading logic:**

### **0/10 or partial credit**
- Matrix built incorrectly  
- Only returns the length, not the subsequences  
- Missing or incorrect method implementations  
- Case-insensitive comparisons  
- Incorrect DP rules  

### **10/10**
- DP matrix is correct  
- `get_entry()` returns correct numeric values  
- `get_longest_common_subsequences()` returns **all** LCS strings  
- Implementation matches the required DP logic  
- Works for all test cases in `main.py` and hidden unit tests  

---

# **Reason for this lab (why it exists):**

This lab teaches you:

- **How dynamic programming works in practice**  
- How to build and traverse a DP matrix  
- How to return structured results (sets of strings)  
- How to implement a class that hides internal details (similar to an ADT)  
- How to solve a classic CS problem used in:  
  - DNA sequence alignment  
  - File comparison (diff tools)  
  - Text similarity  
  - Version control systems  

It reinforces that **correct output is not enough** — the grader checks whether you implemented the **correct DP logic**, not whether you hard‑coded answers.

