#dfin linar sarch
def linear_search(itm_list, itm):
    pos = 0
    found = False
    while pos < len(itm_list) and not found:
        if itm_list[pos] == itm:
            found = True
        else:
            pos = pos + 1
    return found, pos





