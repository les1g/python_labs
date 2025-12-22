from find_LCM import longest_common_substring
from find_LCM_optimized import longest_common_substring_optimized

if __name__ == "__main__":
    str1 = "abcdef"
    str2 = "zcdemf"

    print("\n=== Longest Common Substring Demo ===\n")
    print(f"String 1: {str1}")
    print(f"String 2: {str2}\n")

    # ---------------------------------------------------------
    # Standard Dynamic Programming Version
    # ---------------------------------------------------------
    print("1. Standard DP Version")
    print("----------------------")
    print("This version builds a full 2D matrix of size len(str1) × len(str2).")
    print("Each cell stores the length of the longest common substring ending")
    print("at that pair of characters. This uses O(n × m) space but is easy")
    print("to understand and visualize.\n")

    result = longest_common_substring(str1, str2)
    print("Longest common substring:", result, "\n")

    # ---------------------------------------------------------
    # Space-Optimized Dynamic Programming Version
    # ---------------------------------------------------------
    print("2. Optimized DP Version")
    print("------------------------")
    print("This version computes the same result but uses only one row of memory.")
    print("Instead of storing the entire matrix, it reuses a single list and")
    print("tracks only the values needed for the next computation.")
    print("This reduces space from O(n × m) to O(m) while keeping the same")
    print("time complexity and producing the exact same substring.\n")

    result_optimized = longest_common_substring_optimized(str1, str2)
    print("Longest common substring (optimized):", result_optimized, "\n")

    # ---------------------------------------------------------
    # Summary of Differences
    # ---------------------------------------------------------
    print("Summary:")
    print("--------")
    print("• Both functions return the exact same longest common substring.")
    print("• The standard version uses a full matrix (more memory).")
    print("• The optimized version uses only one row (much less memory).")
    print("• Both are optimal dynamic programming solutions—not heuristics.")
    print("• The difference is memory usage, not correctness.\n")