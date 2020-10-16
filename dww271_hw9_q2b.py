#Question 2b



#b
from ChainingHashTableMap import ChainingHashTableMap


def intersection_list(lst1, lst2):
    hash_table = ChainingHashTableMap()

    new_lst = []

    for i in lst1:
        hash_table[i] = 1

    for k in lst2:
        try:
            if hash_table[k] == 1:
                new_lst.append(k)
                
        except KeyError:
            pass

    return new_lst



