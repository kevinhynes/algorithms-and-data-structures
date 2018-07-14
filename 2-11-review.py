import timeit
from random import randint


# 1. Devise an experiment to verify that the list index operator is O(1).
def index_operator(lst, i):
    lst[i] = None

for list_size in range(1000, 10001, 1000):
    lst = [randint(0, 1000000) for x in range(list_size)]
    index_test = timeit.Timer("index_operator(lst, randint(0, len(lst)-1))",
                              "from __main__ import index_operator,"
                              "lst, randint")
    print("list size:", list_size, "  time:",
          index_test.timeit(number=1000), "milliseconds")


# 2. Devise an experiment to verify that get item and set item are O(1) for
#   dictionaries.
def get_em(dct, i):
    return dct.get(i)

def set_em(dct, i):
    dct[i] = 1

for dict_size in range(1000, 10001, 1000):
    dct = {x: 0 for x in range(dict_size)}
    get_test = timeit.Timer("get_em(dct, randint(0, len(dct)-1))",
                            "from __main__ import get_em, dct, randint")
    print("dict size:", dict_size, "  time:",
          get_test.timeit(number=1000), "milliseconds")

for dict_size in range(1000, 10001, 1000):
    dct = {x: 0 for x in range(dict_size)}
    get_test = timeit.Timer("set_em(dct, randint(0, len(dct)-1))",
                            "from __main__ import set_em, dct, randint")
    print("dict size:", dict_size, "  time:",
          get_test.timeit(number=1000), "milliseconds")


# 3. Devise an experiment that compares the performance of the del operator on
#   lists and dictionaries.
def list_del(lst, i):
    del lst[i]

def dict_del(dct, k):
    try:
        del dct[k]
    except(KeyError):
        pass

for list_size in range(1000, 10001, 1000):
    lst = [x for x in range(list_size)]
    list_del_test = timeit.Timer("list_del(lst, randint(0, len(lst)-1))",
                                 "from __main__ import list_del,"
                                 "lst, randint")
    print("list size:", list_size, "  time:",
          list_del_test.timeit(number=1000), "milliseconds")

for dict_size in range(1000, 10001, 1000):
    dct = {x: 0 for x in range(dict_size)}
    dict_del_test = timeit.Timer("dict_del(dct, randint(0, len(dct) -1))",
                                 "from __main__ import dict_del,"
                                 "dct, randint")
    print("dict size:", dict_size, "  time:",
          dict_del_test.timeit(number=1000), "milliseconds")


# 4. Given a list of numbers in random order, write an algorithm that works in
#   O(nlog(n)) to find the kth smallest number in the list.

# 5. Can you improve the algorithm from the previous problem to be linear?
#   Explain.
