array = [31,41,59,26,41,58]

def insert_sort(array):
    j = 1
    while j<len(array):
        key = array[j]
        i = j-1
        while i>=0 and array[i]>key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key
        j += 1
    return array

print insert_sort(array)
