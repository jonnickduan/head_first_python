#!/usr/bin/env python
# _*_coding:UTF-8_*_
import os
import pickle
from src.chapter5.chapter5 import get_coach_data
os.getcwd()
os.chdir('/Users/JonnickDuan/PycharmProjects/head_first_python/src/chapter6')


def put_to_store(files_list):
    all_athlete = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athlete[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athlete, athf)
    except IOError as err:
        print('File error: ' + str(err))
    return all_athlete


def get_from_store():
    all_athlete = {}
    try:
        with open('athlete.pickle', 'rb') as athf:
            all_athlete = pickle.load(athf)
    except IOError as err:
        print('File error: ' + str(err))
    return all_athlete


data = put_to_store(['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt'])
print(data)
