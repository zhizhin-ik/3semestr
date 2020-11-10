def my_zip(*rest):
    n = len(rest[0])
    for i in rest:
        if len(i)<n:
            n=len(i)
    for k in range(n):
        a=[]
        for i in rest:
            a.append(i[k])
        yield tuple(a)

names = ["Alex", "Bob", "Alice", "John", "Ann"]
age = [25, 17, 34, 24, 42,23]
sex = ["M", "M", "F", "M", "F"]

for values in my_zip(names, age, sex):
    print("name: {} age: {} sex: {}".format(*values))

def my_map(func, iterable):
    for i in iterable:
        yield func(i)

def my_enumerate(a, start=0):
    i=start
    while True:
        yield start, a[start-i]
        start +=1
        if len(a)==start-i:
            break
start=1
a=['a','ab','abc','abcd','abcde']
for idx, elem in my_enumerate(a,start):
    print("{:1}: {:>6}".format(idx, elem))


