import random
import sys


def insertion_sort(unsorted_array: list):
    """
    Sorts array using insertion sort
    """
    for i in range(1, len(unsorted_array)):
        key = unsorted_array[i]
        j = i - 1
        while j >= 0 and key < unsorted_array[j]:
            unsorted_array[j + 1] = unsorted_array[j]
            j -= 1
        unsorted_array[j + 1] = key


def validate(sorted_array: list):
    """
    Validates that array is sorted
    """
    for i in range(0, len(sorted_array) - 1):
        if sorted_array[i] > sorted_array[i + 1]:
            print('invalid!')
            return
    print('valid!')


if __name__ == "__main__":
    size = int(sys.argv[1])
    array = [random.randint(0, size*10) for _ in range(0, size)]
    insertion_sort(array)
    validate(array)
    print("done!")
