"""这是'nester.py'模块，提供了一个名为print_lol()的函数，这个函
数的作用是打印列表，其中有可能包含（也可能不包含）嵌套列表"""
import sys


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    """这个函数取一个位置参数，名为'the_list'，这可以是任何Python
    列表（也可以是包含嵌套列表的列表）。所指定的列表中每个数据项
    会（递归地）输出到屏幕上，而且各占一行。
    第二个参数（名为level）用来在遇到嵌套列表时插入制表符。"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, fh)
        else:
            if indent:
                print("\t" * level, end='', file=fh)
            print(each_item, file=fh)