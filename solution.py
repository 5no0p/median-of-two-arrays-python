def median_of_two_arrays(arr1, arr2):

    # Merge of the two arrays
    merged_array = arr1 + arr2

    # Sorting the resultant array
    merged_array.sort()

    # length of the merged array
    length = len(merged_array)

    # If length of array is even
    if length % 2 == 0:
        meddle_index = length // 2
        fist_middle_number = merged_array[meddle_index]
        second_middle_number = merged_array[meddle_index - 1]
        answer = (fist_middle_number + second_middle_number) / 2
        return answer

    # If length of array is odd
    else:
        meddle_index = length // 2
        answer = merged_array[meddle_index]
        return answer


arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]

print("Median = ", median_of_two_arrays(arr1, arr2))
