# Splitting strings and resturns the elements as lists
def mysplit(strng):
    #
    lst = []

    fnd = strng.find(" ")
    # print(fnd)
    
    if fnd != -1 and strng[:fnd] != '':
        lst.append(strng[:fnd])    

    
    while fnd != -1:
        
        fnd_end = strng.find(" ", fnd + 1)
        # print(fnd_end)
        
        if fnd_end == -1:
            temp_strng = strng[fnd:].lstrip()    
        else:
            temp_strng = strng[fnd:fnd_end].lstrip()
        
        if temp_strng != '':
            lst.append(temp_strng)
        # lst.append(strng[fnd:fnd_end])
        fnd = fnd_end
    
    return lst
  
    #


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit("  moo m ooo  a b   c "))