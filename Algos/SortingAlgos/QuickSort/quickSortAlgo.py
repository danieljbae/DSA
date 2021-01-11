def partition(ls, lo, hi):
    i = (lo-1) # smaller region region
    pivot = ls[hi]
    for j in range(lo, hi):
        if ls[j] <= pivot: # found smaller val: expand small region and swap(small region tail + 1, curr)
            i += 1
            ls[j], ls[i] = ls[i], ls[j]
    ls[i+1], ls[hi] = ls[hi], ls[i+1] # swap in pivot with head of bigger region, bc pivot resided in it's tail
    return i+1

def quickSort(ls, lo, hi):
    if len(ls) == 1:
        return ls
    # Recursively divide to values left/right of pivot
    if lo < hi:
        pivIdx = partition(ls, lo, hi) # sorts the pivot (exclusively) in correct position
        quickSort(ls, lo, pivIdx-1)
        quickSort(ls, pivIdx+1, hi)

def main():
    ls = [10, 7, 8, 9, 1, 5]
    n = len(ls)
    print(ls)
    quickSort(ls, lo=0, hi=n-1)
    print(ls)

if __name__ == "__main__"":
    main()


"""
Lamuto's Partition Scheme: Choose pivot and sort in correct position, by moving all values smaller than our pivot to left.
Implied... since left region strictly contains: vals < pivot ,  thus right must contain: vals >= pivot

[i+1] = correct pivot

smaller region           bigger region
ls[0]...ls[i] | pivot | ls[i+1]...ls[j] | ls[j]...ls[n-1]
<------------- processed --------------> <-- unprocessed -->
"""
