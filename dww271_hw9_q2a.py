#Question 2a



#a
def intersection_list(lst1,lst2):
    lst_of_common_elem=[]
    if len(lst1) < len(lst2):
        for i in range (len(lst1)):
            if lst1[i] in lst2:
                lst_of_common_elem.append(lst1[i])
    else:
        for i in range (len(lst2)):
            if lst2[i] in lst1:
                lst_of_common_elem.append(lst2[i])

    return lst_of_common_elem
   

def main():
    lst1=[1,2]
    lst2=[2,6,8,9]
    print(intersection_list(lst1,lst2))

    lst1=[3,5,6]
    lst2=[]
    print(intersection_list(lst1,lst2))

#main()


