import functools
from collections import OrderedDict
import requests
import psutil
import os



def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

def memory_usage(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        result = f(*args, **kwargs)
        mem_after = get_process_memory()
        total_memory = mem_after - mem_before
        print(f'Total memory of {f.__name__} - {total_memory}')
        return result
    return wrapper

def LFUcache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            print(deco._cache)
            if cache_key in deco._cache:
                # переносимо в кінець списку
                deco._cache.move_to_end(cache_key, last=True)
                # додаэмо 1 до значення в словник "counter"
                deco._cache_counter[cache_key] += 1
                return deco._cache[cache_key]
            result = f(*args, **kwargs)
            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                 # видаляємо найменш вживаний елемент
                value = deco._cache_counter[0]
                deco._cache.move_to_end(value)
                deco._cache_counter.popitem(last=False)
            deco._cache[cache_key] = result
            return result
        deco._cache_counter = OrderedDict()
        deco._cache = OrderedDict()
        return deco
    return internal

@memory_usage
@LFUcache()

def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')

