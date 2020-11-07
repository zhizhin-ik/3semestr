def swap(function_to_decorate):
    def wrapper(arg1,arg2,show):
        function_to_decorate(arg2,arg1,show)
    return wrapper

@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(1, 4, show=True)