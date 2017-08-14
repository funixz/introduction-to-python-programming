def subtract_reversed(a_list):
    if len(a_list) == 0:
        return 0
    result = a_list[-1]
    index = 0
  #  a_list.sort(reverse=True)
    listlen = len(a_list)
    while index < listlen - 1:
        elem = a_list[index]
        result -= elem
        index += 1
    return result
    
    
new = subtract_reversed([5, 4, 2])

print (new)
