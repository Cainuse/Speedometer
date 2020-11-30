import sys
import random as rand


def search(arr, x):
    return search_with_binary(arr, 0, len(arr), x)


def search_with_binary(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return search_with_binary(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return search_with_binary(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


if __name__ == "__main__":
    for i in range(0, 100):
        arr = []
        for j in range(int(sys.argv[3])):
            arr.append(rand.randint(int(sys.argv[1]), int(sys.argv[2])))
        result = search(arr, int(sys.argv[4]))
    print("done!")
