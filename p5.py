def binarySearch(arr, first, last, ele): 
    if last>=first: 
        mid = int(first + (last - first)/2)
        if arr[mid] == ele: 
            return mid
        elif arr[mid] > ele: 
            return binarySearch(arr, first, mid-1, ele) 
        else: 
            return binarySearch(arr, mid + 1, last, ele) 
    else:  
        return "Number not in the list"

arr = sorted(list(map(int, input().split())))
ele = int(input())
print(binarySearch(arr, 0, len(arr)-1, ele))

# Input format type:

# 78 67 99 56 45 80
# 56

# After sorting array will be [45, 56, 67, 78, 80, 99] 

# Output
# 1