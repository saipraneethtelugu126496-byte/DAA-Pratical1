def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[arr[min_idx]] = arr[min_idx], arr[i]
        
    return arr

data = [6, 5, 1, 2, 4]
sorted_data = selection_sort(data)
print("Sorted array:", sorted_data)
