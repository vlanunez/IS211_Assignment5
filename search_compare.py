#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import random


def sequential_search(a_list, item):
    
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)


def ordered_sequential_search(a_list, item):
   
    a_list = sorted(a_list)

    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)


def binary_search_iterative(a_list, item):
    
    a_list = sorted(a_list)

    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)


def binary_search_recursive(a_list, item):
    
    a_list = sorted(a_list)

    start_time = time.time()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)


def list_gen(maxval):
    
    samplist = random.sample(range(1, (maxval + 1)), maxval)
    return samplist


def main():

    samp_size = [500, 1000, 10000]
    tests = {'Sequential': 0,
             'Ordered': 0,
             'Bin Iterative': 0,
             'Bin Recursive': 0}

    for smpl in samp_size:
        counter = 0
        while counter < 100:
            test_list = list_gen(smpl)
            tests['Sequential'] += sequential_search(test_list, -1)[0]
            tests['Ordered'] += ordered_sequential_search(test_list, -1)[0]
            tests['Bin Iterative'] += binary_search_iterative(test_list, -1)[0]
            tests['Bin Recursive'] += binary_search_recursive(test_list, -1)[0]
            counter += 1

        print ('For sample size %s:' % (smpl))

        for tst in tests:
            print (('%s Search took %10.7f seconds to run, '
                   'on average.') % (tst, tests[tst] / counter))


if __name__ == "__main__":
    main()

