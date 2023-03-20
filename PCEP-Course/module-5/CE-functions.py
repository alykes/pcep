def unique(list_1=[]):

    if len(list_1) == 0:
        return []

    ret_list = []
    dict = {}
    temp_list = list_1
    
    for i in list_1:
        count = 0
        for j in temp_list:
            if i == j:
                count += 1
            dict.update({i: count})
    
    for i in dict.keys():
        ret_list.append(i)
    
    return ret_list
    
print(unique([1, 2, 3, 3, 3, 3, 4, 5]))
print(unique([]))

############# SOLUTION #############
def unique(input_list=[]):
  to_return = []
  for el in input_list:
    if el not in to_return:
      to_return.append(el)
  return to_return

print(unique([1, 2, 3, 3, 3, 3, 4, 5]))
print(unique([]))

