def ordered_binary_search(olist, item):
    if len(olist) == 0:
        return False
    else:
        midpoint = len(olist) // 2
        if olist[midpoint] == item:
            return True
        elif item < olist[midpoint]:
            return binarysearch(olist[:midpoint], item)
        else:
            return binarysearch(olist[midpoint+1:], item)

def binarysearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while (first <= last and not found):
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found
    
    
    
    
    
    
    
    
    



