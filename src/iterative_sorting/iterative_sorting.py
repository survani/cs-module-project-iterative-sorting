# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements

    # I have a -1 in this range because if it is the last item in the list we don't need to compare it anymore.
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # all elements to the right of the smallest index to the len of our arr
        for j in range(i + 1, len(arr)):

            # if the next item in the arr is less than the already min value replace it to now being the min value.
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        # now that it has sort we need to make the switch.
        if smallest_index != i:
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


# print(selection_sort([3, 4, 2, 4, 5, 6, 7, 4]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    length = len(arr) - 1
    sort = False

    while not sort:
        sort = True
        for i in range(0, length):
            if arr[i] > arr[i + 1]:
                sort = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


# print(bubble_sort([3, 4, 2, 4, 5, 6, 7, 4]))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
