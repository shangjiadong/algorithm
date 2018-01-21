"""
Implement mergesort.
   
   >>> mergesort([4, 2, 5, 1, 6, 3])
   [1, 2, 3, 4, 5, 6]   
"""

def mergesort(alist):
    if len(alist) > 1: 
        mid = len(alist)/2;
        left = alist[:mid]
        right = alist[mid:]
        
        mergesort(left)
        mergesort(right)
        
        i, j, k = 0, 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
    return alist
        
def main():
    print(mergesort([4,2,5,1,6,3]))
    
if __name__ == "__main__":
    main()
            
    