import time


def decorator(num_of_repeats=1):
    def actual_decorator(func):

        def wrapper(*args, **kwargs):
            start_time_repeats = time.time()
            list_time = []
            for i in range(num_of_repeats):
                start_time_repeat = time.time()
                result = func(*args, **kwargs)
                time_repeat = time.time() - start_time_repeat
                list_time.append(time_repeat)
            time_repeats = time.time() - start_time_repeats
            return dict(
                        result=result,
                        time_repeats=time_repeats,
                        args_name=args,
                        func_name=func.__name__,
                        time_repeat=list_time
                        )
        return wrapper
    return actual_decorator


@decorator(50000)
def say_hello(name):
    return f'Hello {name}'

print(say_hello('Bob'))
print(say_hello('Alex')['time_repeats'])
print(say_hello('Bob')['time_repeat'][10001])



