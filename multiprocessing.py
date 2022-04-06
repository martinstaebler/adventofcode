import time
import concurrent.futures

def do_something(seconds):
    print(f'Sleeping {seconds} second(s) ...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)