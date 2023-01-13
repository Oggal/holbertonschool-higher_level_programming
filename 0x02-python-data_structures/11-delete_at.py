#!/usr/bin/python3


def delete_at(my_list, idx):
    if(idx >= 0 and len(my_list) > idx):
        del my_list[idx]
    return my_list
