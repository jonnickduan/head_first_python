#!/usr/bin/env python
# _*_coding:UTF-8_*_
import sys


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, fh)
            print('test')
        else:
            if indent:
                print("\t" * level, end='', file=fh)
            print(each_item, file=fh)
