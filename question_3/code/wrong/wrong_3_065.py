def remove_extras(lst):
    new_lst = [lst[0],]
    for e in lst:
        if e in new_lst:
            continue
        else:
            new_lst.append(e)
            
    return new_lst
    
print(remove_extras([1, 1, 1, 2, 3]))
print(remove_extras([1, 5, 1, 1, 3, 2]))
print(remove_extras([3, 4, 5, 1, 3]))
