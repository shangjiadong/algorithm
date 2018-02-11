"""
Maximum Weighted Independent Set 

   [HINT] independent set is a set where no two numbers are neighbors in the original list.
      see also https://en.wikipedia.org/wiki/Independent_set_(graph_theory)

   input:  a list of numbers (could be negative)
   output: a pair of the max sum and the list of numbers chosen

   >>> max_wis([7,8,5])
   (12, [7,5])

   >>> max_wis([-1,8,10])
   (10, [10])

   >>> max_wis([])
   (0, [])
"""
# top-down version
def max_wis(alist):
    mwis = {-1: (0, []), 0: (0, [])}
    l = len(alist)
    if l not in mwis:
        (top, top_backtrack) = max_wis(alist[:l-1])
        (botm, botm_backtrack) = max_wis(alist[:l-2])
        if top > botm + alist[l-1]:
            mwis[l] = (top, top_backtrack)
        else:
            botm_backtrack.append(alist[l-1])
            mwis[l] = (botm+alist[l-1], botm_backtrack)
    return mwis[l]
    
# bottom-up version
def max_wis2(alist):
    adj = (0, [])
    nonAdj = (0, [])
    for i in range(len(alist)):
        temp = adj
        if adj[0] < nonAdj[0] + alist[i]:
            nonAdj[1].append(alist[i])
            adj = (nonAdj[0] + alist[i], nonAdj[1])
        nonAdj = temp
    return adj

def main():
    print(max_wis([7,8,5]))
    print(max_wis([-5,-4,-1]))
    print(max_wis([-1,-8,10]))
    print(max_wis([]))

    print(max_wis2([7,8,5]))
    print(max_wis2([-5,-4,-1]))
    print(max_wis2([-1,-8,10]))
    print(max_wis2([]))

if __name__ == '__main__':
    main()