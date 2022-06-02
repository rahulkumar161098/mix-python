def sorted_arr(c):
    if len(c)<= 1:
        return c
    mid= len(c)//2
    left= c[:mid]
    right= c[mid:]
    
    # Recursion call
    left= sorted_arr(left)
    right= sorted_arr(right)

    return (marge_two_sort_arr(left, right))


# Que :-  marge to sorted list
def marge_two_sort_arr(a,b):
    sorted_arr =[]
    len_a= len(a)
    len_b= len(b)
    i=0
    j=0

    while i < len_a and j< len_b:
        if a[i] <= b[j]:
            sorted_arr.append(a[i])
            i+=1
        else:
            sorted_arr.append(b[j])
            j+=1
    while i < len_a:
        sorted_arr.append(a[i])
        i+=1
    while j < len_b:
        sorted_arr.append(b[j]) 
        j+=1
    return sorted_arr

# a= [4,7,8,9,10,12]
# b= [2,3,5,7]
c= [3,98,43,54,12,34,12,32,45]
print(sorted_arr(c))
