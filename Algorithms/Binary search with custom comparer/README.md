# 11.3 LAB: Binary search with custom comparer

Implement the Searcher class's `binary_search()` method in the Searcher.py file. Access Searcher.py by clicking on the orange arrow next to main.py at the top of the coding window. 

The method performs a binary search on the sorted list (second parameter) for the key (third parameter). `binary_search()` returns the key's index if found, -1 if not found.

Compare a list element to the key using the `compare()` method of the `comparer` object passed as a parameter of the Searcher's constructor. `comparer.compare(a, b)` returns an integer:

- greater than 0 if a > b
- less than 0 if a < b
- equal to 0 if a == b

A few test cases exist in main() to test `binary_search()` with both string searches and integer searches. Clicking "Run program" will display test case results, each starting with "PASS" or "FAIL". Ensure that all tests are passing before submitting code.

Each test in main() only checks that `binary_search()` returns the correct result, but does not check the number of comparisons performed. The unit tests in the submit mode check both `binary_search()`'s return value and the number of comparisons performed.