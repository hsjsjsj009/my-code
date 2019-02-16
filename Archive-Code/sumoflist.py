def sum_of_list(lst):
        if len(lst)>0:
            if type(lst[0]) == int :
                return lst[0]+sum_of_list(lst[1:])
            elif type(lst[0]) == list:
                return sum_of_list(lst[0])
        else :
            return 0

print(sum_of_list([1,[2,[6,[[1,2,[1,[3,[]]]]]]]]))