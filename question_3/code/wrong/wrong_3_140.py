# def remove_extras(lst):
#     my_lst = []
#     for i in lst:
#         if i not in my_lst:
#             my_lst.append(i)
#         return my_lst

def remove_extras(lst):
    new_lst = []
    for i in range(lst):
      if lst[i] in new_lst:
        lst.append(i)
      return new_lst