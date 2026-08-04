def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        
        
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

if __name__ == "__main__":
    data = [2, 1, 3, 5, 6]
    print("Original array:", data)
    
    insertion_sort(data)
    print("Sorted array:  ", data)
