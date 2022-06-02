def swap(a, b, arr):
    if a!=b:
        temp= arr[a]
        arr[a]= arr[b]
        arr[b]= temp

def partition(element, start_index, end_index):
    pivot_index= 0
    pivot= element[pivot_index]
    # print(pivot)

    # increase index with one  

    # print(end_index)
    while start_index < end_index:
        while start_index < len(element) and element[start_index] <= pivot:
            start_index +=1

        while element[end_index] > pivot:
            end_index -= 1

        if start_index < end_index:
            swap(start_index, end_index, element)

    swap(pivot_index, end_index, element)
    return end_index

def quick_sort(element,start_index, end_index):
    if start_index < end_index:
        pi= partition(element, start_index, end_index)
        quick_sort(element, start_index, pi - 1)  #left partition
        quick_sort(element, pi+1, end_index)        #right partition


element= [11,9,29,7,2,15,28]
quick_sort(element, 0, len(element)-1)
print(element)

    # start_index= pivot_index + 1
    # # print(start_index)
    # end_index= len(element) - 1