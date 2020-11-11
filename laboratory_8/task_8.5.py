import itertools

def get_permutations(s, n):
    result=itertools.permutations(s,n)
    result=list(result)
    for i,elem in enumerate(result):
        s=''
        for j in range(n):
            s+=elem[j]
        result[i]=s
    result.sort()
    return result

print(get_permutations("cat", 2))
#["ac", "at", "ca", "ct", "ta", "tc"]