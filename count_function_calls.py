from functools import wraps


class CallsLimitExceededException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = message

    def __str__(self):
        return self.message


class FunctionCallsCounter(object):
    """
    Decorator which raises an exception
    when function calls exceed a defined limit.
    """
    def __init__(self, max_calls):
        self.max_calls = max_calls

    def __call__(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if wrapped.calls > self.max_calls:
                raise CallsLimitExceededException('No more calls allowed!')
            func(*args, **kwargs)
            wrapped.calls += 1

        wrapped.calls = 1
        return wrapped


# Demonstration
@FunctionCallsCounter(2)
def print_one(one):
    print(one)


print_one(1)
print_one(1)
print_one(1)
