#!/usr/bin/env python
# _*_coding:UTF-8_*_
import os
from src.chapter5.chapter5 import get_coach_data
os.getcwd()
os.chdir('/Users/JonnickDuan/PycharmProjects/head_first_python/src/chapter6')
sarah = get_coach_data('sarah2.txt')
print(sarah.name + '\'s fastest times are ' + str(sarah.top3()))
james = get_coach_data('james2.txt')
print(james.name + '\'s fastest times are ' + str(james.top3()))
julie = get_coach_data('julie2.txt')
print(julie.name + '\'s fastest times are ' + str(julie.top3()))
mikey = get_coach_data('mikey2.txt')
print(mikey.name + '\'s fastest times are ' + str(mikey.top3()))
