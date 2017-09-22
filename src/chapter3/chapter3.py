#!/usr/bin/env python
# _*_coding:UTF-8_*_
import os
from nester import print_lol
import pickle

os.getcwd()
os.chdir('C:\\Users\\Jonnick\\PycharmProjects\\head_first_python\\src')
os.getcwd()
man = []
other = []

try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as err:
    print('File error' + str(err))

try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error' + str(err))
except pickle.PickleError as p_err:
    print('PickleError' + str(p_err))

new_man = []
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error' + str(err))
except pickle.PickleError as p_err:
    print('PickleError' + str(p_err))

print_lol(new_man)
