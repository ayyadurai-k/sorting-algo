def quick_sort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Index for smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot into correct position
    return i + 1

# Input as per your format
print("Enter elements into list:")
a = [int(x) for x in input().split()]
high = len(a)

# Sorting the list using quick sort
quick_sort(a, 0, high - 1)

# Output
print("The sorted list is", a)
