# Splitting strings and resturns the elements as lists
def mysplit(strng):
    #
    if strng.isspace() or strng == "":
        return []
    
    strng = strng.strip()
    lst = []
    
    fnd = strng.find(" ")
    
    if fnd == -1:
        lst.append(strng[:])    
    else:
        lst.append(strng[:fnd])
        
        while fnd != -1:
            fnd_end = strng.find(" ", fnd +1)
            if fnd_end == -1:
                lst.append(strng[fnd:].lstrip())
            elif not strng[fnd:fnd_end].isspace():
                lst.append(strng[fnd:fnd_end].lstrip())
            
            fnd = fnd_end
        
    return lst
    #


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit("  moo m ooo  a b   c "))
print(mysplit("  moo m ooo  a b   c     "))