def section_sort(arr):
    for i in range(0, len(arr)-1 ):
        current_min_idx= i
        # print(current_min_idx)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[current_min_idx]:
                current_min_idx= j
        arr[i], arr[current_min_idx] = arr[current_min_idx], arr[i] #swap

arr= [2,9,4,7,1,8,5]
section_sort(arr)
print(arr)