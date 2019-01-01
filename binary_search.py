#define our function
def binary_search(item_list, item):
    #dfin first indx
    first = 0
    #dfin last indx
    last = len(item_list) - 1
    #dfin a boolean variabl to kip track of th rsult
    found = False
    #use a hil loop to hovr around th list
    while (first <= last and not found):
        #dfin th middl itm using th floor division
        mid = (first + last) // 2
        #st conditions using th if statmnt
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
             




