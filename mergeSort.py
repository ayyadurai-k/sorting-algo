def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: Already sorted

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements from both halves
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Input as per your format
print("Enter elements into list:")
a = [int(x) for x in input().split()]

# Sorting the list using merge sort
a[:] = merge_sort(a)  # Updating the list in place

# Output
print("The sorted list is", a)
