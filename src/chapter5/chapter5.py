#!/usr/bin/env python
# _*_coding:UTF-8_*_
import os

os.getcwd()
os.chdir('/Users/jonnickduan/PycharmProjects/head_first_python')


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return mins + ':' + secs


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=None):
        super().__init__()
        if a_times is None:
            a_times = []
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


def get_coach_data(fn):
    try:
        with open(fn) as time_file:
            data = time_file.readline()
            templ = data.strip().split(',')
            return AthleteList(templ.pop(0), templ.pop(0), templ)
    except IOError as err:
        print('File error: ' + str(err))
        return None
