#!/usr/bin/env python
# _*_coding:UTF-8_*_
import os
from src.chapter5.chapter5 import get_coach_data, sanitize

os.getcwd()
os.chdir('C:\\Users\\Jonnick\\PycharmProjects\\head_first_python\\src\\chapter6')
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are " + str(sorted(set([sanitize(each_time) for each_time in sarah]))[0:3]))
