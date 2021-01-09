def mergeSort(ls):
    if len(ls) > 1:
        # Recursively Divide
        mid = len(ls)//2
        left = ls[:mid]
        right = ls[mid:]
        mergeSort(left) # Recursively Sort
        mergeSort(right)

        # merge until one list is depleted
        l = r = mergedIdx = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                ls[mergedIdx] = left[l]
                l += 1
            else:
                ls[mergedIdx] = right[r]
                r += 1
            mergedIdx += 1

        # Determine which one is depleted
        remaining,remainIdx = (left,l) if l < len(left) else (right,r)
        while remainIdx < len(remaining):
            ls[mergedIdx] = remaining[remainIdx]
            remainIdx += 1
            mergedIdx += 1

ls = [7,4,8,3,1,4,6,2,5]
print(ls)
mergeSort(ls)
print(ls)

