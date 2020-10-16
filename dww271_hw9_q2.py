#Question 2



#a
def intersection_list(lst1,lst2):
    lst_of_common_elem=[]
    if len(lst1)<len(lst2):
        for i in range (len(lst1)):
            if lst1[i] in lst2:
                lst_of_common_elem.append(lst1[i])
    else:
        for i in range (len(lst2)):
            if lst2[i] in lst1:
                lst_of_common_elem.appened(lst[i])

    return lst_of_common_elem
   '''
    I suppose it doesnt matter whether or not i look for the shorter list
    because it would have to iterate through both anyway because pythons
    "in" function was used. But I already wrote it so....
    '''

def main():
    lst1=[1,2]
    lst2=[2,6,8,9]
    print(intersection_list(lst1,lst2))

    lst1=[3,5,6]
    lst2=[]
    print(intersection_list(lst1,lst2))

#main()


#b
def intersection_list(lst1,lst2):
    lst_of_common_elements=[]
    dictionary={}
    
    if len(lst1)<len(lst2):
        for key in lst1:
            dictionary[key]=0

        for element in lst2:
            if element in dictionary:
                dictionary[element]+=1

        for key,value in dictionary.items():
            if dictionary[key]>=1:
                lst_of_common_elements.append(key)
    else:
        for key in lst2:
            dictionary[key]=0

        for element in lst2:
            if element in dictionary.items():
                dictionary[element]+=1

        for key,value in dictionary:
            if dictionary[key]>=1:
                lst_of_common_elements.append(key)

    '''
    I suppose it doesnt matter whether or not i look for the shorter list
    because it would have to iterate through both anyway. But I already wrote it
    so....
    '''

    return lst_of_common_elements

def main():
    lst1=[1,2]
    lst2=[2,6,8,9]
    print(intersection_list(lst1,lst2))

    lst1=[3,5,6]
    lst2=[]
    print(intersection_list(lst1,lst2))

#main()
