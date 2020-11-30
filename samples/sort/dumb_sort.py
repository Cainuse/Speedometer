import random
import sys


class DumbSort:

    @staticmethod
    def sort(array: list):

        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key


class ValidateSort:

    @staticmethod
    def validate(array: list):
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                print('invalid!')
                return
        print('valid!')


if __name__ == "__main__":
    size = int(sys.argv[1])
    array = [random.randint(0, size*10) for _ in range(0, size)]
    DumbSort.sort(array)
    ValidateSort.validate(array)
    print("done!")
