def function(a):
    return print(a**2)

def print_map(function, iterable):
    iterator=iterable.__iter__()
    while True:
        try:
            value=iterator.__next__()
        except StopIteration:
            break
        function(value)

iterable=[0,1,2,3,4]
print_map(function,iterable)