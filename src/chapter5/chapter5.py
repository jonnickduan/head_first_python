#!/usr/bin/env python
# _*_coding:UTF-8_*_


import os

os.getcwd()
os.chdir('C:\\Users\\Jonnick\\PycharmProjects\\head_first_python\\src\\chapter5')


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return mins + ':' + secs


def get_coach_data(fn):
    """
    :rtype: []
    """
    try:
        with open(fn) as time_file:
            return time_file.readline().strip().split(',')
    except IOError as err:
        print('File error: ' + str(err))
        return None


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

print(sorted(set([sanitize(each_time) for each_time in james]))[0:3])
print(sorted(set([sanitize(each_time) for each_time in julie]))[0:3])
print(sorted(set([sanitize(each_time) for each_time in mikey]))[0:3])
print(sorted(set([sanitize(each_time) for each_time in sarah]))[0:3])
