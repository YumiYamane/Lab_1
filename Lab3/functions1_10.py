def Unique(list):
    unique = []
    
    for i in list:
        if i not in unique:
            unique.append(i)
    
    return unique