def decorator_func(function_to_decorate):
    def changing_the_behavior_of_the_function(list_of_numbers):
        k=function_to_decorate(list_of_numbers)
        if k>10:
            return 'Очень много'
        if k==0:
            return 'Нет('
        else:
            return k
    return changing_the_behavior_of_the_function

@decorator_func
def func(a):
    k=0
    for i in a:
        if i%2==0:
            k+=1
    return k

a=[2,2,2,2,2,2,2,2,2,2,2]
print(func(a))