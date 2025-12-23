class Searcher:
    # Returns the index of the key in the sorted list, or -1 if the key is not found
    @staticmethod
    def binary_search(sorted_list, key, comparer):
        # Type your code here.
        # step 1: initialize low and high
        low = 0
        high = len(sorted_list) - 1

        # step 2: binary search loop
        while high >= low:
            mid = (high + low) // 2
            comparison = comparer.compare(sorted_list[mid], key)
            if comparison < 0:
                low = mid + 1
            elif comparison > 0:
                high = mid - 1
            else:
                return mid
        return -1  # not found 
