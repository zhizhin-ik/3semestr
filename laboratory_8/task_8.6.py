import itertools

def get_combinations(s, n):
    x=[]
    for k in range(1,n+1):
        result=itertools.combinations(s,k)
        result=list(result)
        result.sort()
        for i,elem in enumerate(result):
            tr=''
            for j in range(k):
                tr+=elem[j]
            x.append(tr)
    return x

print(get_combinations("cat", 2))