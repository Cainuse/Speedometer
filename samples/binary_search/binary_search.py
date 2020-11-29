import sys
import numpy as np


class BinSearch:
    def search(self, arr, x):
        return self.search_with_binary(arr, 0, len(arr), x)

    def search_with_binary(self, arr, low, high, x):
        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

                # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.search_with_binary(arr, low, mid - 1, x)

                # Else the element can only be present in right subarray
            else:
                return self.search_with_binary(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1


if __name__ == "__main__":
    array = np.random.randint(sys.argv[1], sys.argv[2], sys.argv[3])
    bs = BinSearch()
    bs.search(array, int(sys.argv[4]))
