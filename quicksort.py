def quicksort(array, start=0, stop=-1):
    
    
    # if array is empty, return an error message
    if not array:
        raise IndexError("Array is empty, cannot be sorted.")
    # if the array has just one element, then end
    if len(array) == 1:
        print("Array has only one element, cannot sort.")
        return array
    # if array has only two elements, then do a simple sort
    if len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
            return array
        else:
            return array
    sorted_array = []
    # select pivots from the array
    first_val = array[start]
    last_val = array[stop]
    middle_val = array[(len(array) - 1) // 2]
    pivots = [first_val, middle_val, last_val]
    sorted_pivots = []
    
    for pivot in pivots:
        if not sorted_pivots:
            sorted_pivots.append(pivot)

        else:
            for i, j in enumerate(sorted_pivots):
                if pivot not in sorted_pivots:
                    if pivot <= j:
                        sorted_pivots.insert(i, pivot)
                    else:
                        sorted_pivots.append(pivot)
            
    # if the array only had 3 elements then we're done
    if len(array) == 3:
        sorted_array = sorted_pivots
        return sorted_array
    
    pivot = sorted_pivots[1]
    middle_array = []
    left_array = []
    right_array = []
    
    for i in array:
        if i < pivot:
            left_array.append(i)
        elif i > pivot:
            right_array.append(i)
        else:
            middle_array.append(i)
    
    print(len(left_array))
    print("Left:", left_array)
    print(len(middle_array))
    print("Middle:", middle_array)
    print(len(right_array))
    print("Right:", right_array)
    if len(left_array) > 2:
        left_array = quicksort(left_array)
    if len(right_array) > 2:
        right_array = quicksort(right_array)
    
    sorted_array = left_array + middle_array + right_array
    
    return sorted_array