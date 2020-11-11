import itertools

def get_combinations_with_r(s, n):
    x=[]
    result=itertools.combinations_with_replacement(s,n)
    result=list(result)
    result.sort()
    for i,elem in enumerate(result):
        tr=''
        for j in range(n):
            tr+=elem[j]
        x.append(tr)
    return x


print(get_combinations_with_r("cat", 2))
#["aa", "ac", "at", "cc", "ct", "tt"]