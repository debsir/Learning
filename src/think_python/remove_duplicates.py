#!/usr/bin/python

def remove_duplicates(L):
    uniq_list = []
    for item in L:
        if item not in uniq_list:
            uniq_list.append(item)
    return uniq_list


num_list = [1, 1, 2, 2, 3, 3]
new_list = remove_duplicates(num_list)
print new_list
