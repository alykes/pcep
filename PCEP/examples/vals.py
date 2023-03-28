my_list = [1, 2, 3]

for v in range(len(my_list)):
   print('v is:', v, 'and my_list[v] is:', my_list[v])
   print('Before insert:', my_list)
   my_list.insert(1, my_list[v])
   print('After insert:', my_list)

print('...and finally:', my_list)