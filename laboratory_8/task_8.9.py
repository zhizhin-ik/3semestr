import itertools

def maximize(lists, m):
    sum=0
    for i in lists:
        sum+=max(list(itertools.chain(i)))**2
    return sum%m

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000))
# 206