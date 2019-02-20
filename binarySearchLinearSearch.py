import timeit
from random import randint


def binary_search(mylist, find):
    while len(mylist) > 0:
        mid = (len(mylist))// 2
        if mylist[mid] == find:
            return True
        elif mylist[mid] < find:
             mylist = mylist[:mid]
        else:
             mylist = mylist[mid + 1:]
    return False;


def linear_search(mylist, find):
    for x in mylist:
        if x == find:
            return True
    return False


def binary_time():
    SETUP_CODE = '''
from __main__ import binary_search
from random import randint'''

    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
binary_search(mylist, find)'''

    times = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=1000)

    print("binary search time :",times)


def linear_time():
    SETUP_CODE = '''
from __main__ import linear_search
from random import randint'''

    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
linear_search(mylist, find)
        '''

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE,repeat=3, number=1000)

    print("linear search time is :",times)


if __name__ == "__main__":
    linear_time()
    binary_time()
