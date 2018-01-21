"""
>>> num_inversions([4, 1, 3, 2])
4
>>> num_inversions([2, 4, 1, 3])
3
"""
def _num_inversions_helper(alist):
    if len(alist) < 2:
        return 0, alist
    
    mid = len(alist)//2
    rev_left, left = _num_inversions_helper(alist[:mid])
    rev_right, right = _num_inversions_helper(alist[mid:])
    
    blist = []
    count = 0
    i, j, k = 0, 0, 0
        
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            blist.append(left[i])
            i += 1
            k += 1
        else:
            count += (len(left) - i)
            blist.append(right[j])
            j += 1
            k += 1
    while i < len(left):
        blist.append(left[i])
        i += 1
        k += 1
    while j < len(right):
        blist.append(right[j])
        j += 1
        k += 1
    return count + rev_left + rev_right, blist
        
def num_inversions(alist):
    return _num_inversions_helper(alist)[0]
            
def main():
    print(num_inversions([4,2,5,1,6,3]))
    print(num_inversions([4, 1, 3, 2]))
    
if __name__ == "__main__":
    main()
            
            