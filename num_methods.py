import sys

def swap(array, item1, item2):
    results = array
    a, b = array.index(item1), array.index(item2)
    results[a], results[b] = array[b], array[a]
    return results

a = [1,2,3,4]

