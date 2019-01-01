#dfin out function
def binary_search(itm_list, itm):
    first = 0
    last = len(itm_list) - 1
    found = False
    while(first <= last and not found):
        mid = (first + last) // 2
        if itm_list[mid] == itm:
            found = True
        elif itm < itm_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found




