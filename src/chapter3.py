#!/usr/bin/env python
# _*_coding:UTF-8_*_
import os

from nester import print_lol

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
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        print_lol(man, fh=man_file)
        print_lol(other, fh=other_file)
except IOError:
    print('File error' + str(err))
