import itertools

def get_cartesian_product(a, b):
    result=itertools.product(a,b)
    result=list(result)
    return result

print(get_cartesian_product([1, 2], [3, 4]))