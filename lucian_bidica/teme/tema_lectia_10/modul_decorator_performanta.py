import time
from csv_library import write_csv


def decorator_functie_performanta(name="Algorithm"):
    def decorator(function):
        def inner(*args, **kwargs):
            t1 = time.time()
            result = function(*args, **kwargs)
            t2 = time.time()
            write_csv([name, len(result), t2 - t1])
            return result

        return inner

    return decorator
