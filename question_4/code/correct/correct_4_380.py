def sort_age(lst):
    newlst=[]
    while lst:
        big=lst[0]
        for n in lst:
            if n[1]>big[1]:
                big=n
        lst.remove(big)
        newlst.append(big)
    return newlst
            
