def merg_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    l_half = arr[:mid]
    r_half = arr[mid:]
    
    l_half = merg_sort(l_half)
    r_half = merg_sort(r_half)

    sorted_arr = merge(l_half, r_half)
    
    print(f"Merging: {l_half} and {r_half} -> {sorted_arr}")
    
    return sorted_arr

def merge(left, right):
    new = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    new.extend(left[i:])
    new.extend(right[j:])
    
    return new

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merg_sort(arr)
print("Final sorted array:", sorted_arr)
