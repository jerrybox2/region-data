# -*- coding: utf-8 -*-
"""
# reference: https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module
"""
import time
from functools import wraps


def execute_time(fn):
    """
    :param fn:  需要记录执行时间的函数名
    :return:
    """
    @wraps(fn)
    def fn_wrap(*args, **kwargs):
        start_time = time.time()

        result = fn(*args, **kwargs)

        elapsed_time = time.time() - start_time
        print('Execution time: %.3f .' % elapsed_time)
        return result
    return fn_wrap
