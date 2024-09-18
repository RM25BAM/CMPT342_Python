""" def main():

    values = [3, 2, -1, 5, 8, 4]
    print(min(values))
    selectionSort(values)

    print('After sorting')

    print(values)
def selectionSort(values):
    temp = 0 
    ind = 0
    Min = 0
    j = 1
    for i in range(0, len(values)):
        if values[i] < values[j]:
            j += 1
        else:
            temp = values[j]
            ind = values.index(temp)
            values[ind] = values[i]
            values[i] = temp
        print(values[ind])
main() """
# Selection sort in Python

def selectionSort(val):  
    for ind in range(len(val) - 1):
        min_index = ind
        for j in range(ind + 1, len(val)):
            # select the minimum element in every iteration
            if val[j] < val[min_index]:
                min_index = j
            # swapping the elements to sort the array
            (val[ind], val[min_index]) = (val[min_index], val[ind])
def main():

    values = [3, 2, -1, 5, 8, 4]

    selectionSort(values)

    print('After sorting')

    print(values)

main()