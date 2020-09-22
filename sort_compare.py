#!/usr/bin/env python
# coding: utf-8

# In[8]:


import time
import random


def insertion_sort(a_list):
    
    start_time = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, a_list)


def gap_insertion_sort(a_list, start, gap):
    
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def shell_sort(a_list):
    
    start_time = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, a_list)


def python_sort(a_list):
    
    start_time = time.time()

    a_list.sort()

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, a_list)


def list_gen(maxval):
    
    samplist = random.sample(range(1, (maxval + 1)), maxval)
    return samplist


def main():
    
    samp_size = [500, 1000, 10000]
    tests = {'Insertion': 0,
             'Shell': 0,
             'Python': 0}

    for smpl in samp_size:
        counter = 0
        while counter < 100:
            test_list = list_gen(smpl)
            tests['Insertion'] += insertion_sort(test_list)[0]
            tests['Shell'] += shell_sort(test_list)[0]
            tests['Python'] += python_sort(test_list)[0]
            counter += 1

        print ('For sample size %s:' % (smpl))

        for tst in tests:
            print (('%s Sort took %10.7f seconds to run,' 
                   'on average.') % (tst, tests[tst] / counter))

if __name__ == '__main__':
    main()













