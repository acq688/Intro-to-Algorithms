#!/usr/bin/env python3
import argparse

def insertion_sort(my_list):
    sorted_list = []
    for str_item in my_list:
        item = int(str_item)
        for index, sorted_item in enumerate(sorted_list):
            if item <= sorted_item:
                sorted_list.insert(index, item)
                break
        else:
            sorted_list.append(item)

    return sorted_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', dest='my_list', 
                        nargs='*', required=True)
    args = parser.parse_args()
    print(args.my_list)
    print(insertion_sort(args.my_list))
