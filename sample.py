import random #ランダムモジュール
import math
import copy
import numpy as np
import copy

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

a = [2, 5, 6, 2, 7]

print(my_index_multi(a, 2))
