import itertools

def compress_string(s):
    result=itertools.groupby(s)
    x=[]
    for key,value in result:
        value=list(value)
        x.append((len(value), int(key)))
    return x


print(compress_string('1222311'))
#[(1, 1), (3, 2), (1, 3), (2, 1)]