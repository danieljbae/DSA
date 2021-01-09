import numpy as np

def mergeSort(ls):
    if len(ls) > 1:
        # Recursively Divide list into 2 halves
        mid = len(ls) // 2
        left = ls[:mid]
        right = ls[mid:]
        mergeSort(left) # Recursively sort both lists
        mergeSort(right)

        # Merge lists until one is depleted
        mergedIdx = l = r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                ls[mergedIdx] = left[l]
                l += 1
            else:
                ls[mergedIdx] = right[r]
                r += 1
            mergedIdx += 1

        # Determine which ls is remaining and append
        remainIdx,remaining  = (l,left) if l < len(left) else (r,right)
        while remainIdx < len(remaining):
            ls[mergedIdx] = remaining[remainIdx]
            remainIdx += 1
            mergedIdx += 1

def main(ls=None):
    ls = list(np.random.randint(100, size=10))
    print(type(ls))
    # ls = [12, 11, 13, 5, 6, 7]
    print(ls)
    mergeSort(ls)
    print(ls)

if __name__ == '__main__':
    main()
