import time

def decorator_maker_with_arguments(path):
    def my_decorator(func):
        def wrapped(arg):
            function_call_time = time.time()
            result = func(arg)
            answer=result
            function_end_time=time.time()
            function_time="--- %s seconds ---" % (function_end_time-function_call_time)
            function_call_time='1. Время вызова функции '+time.ctime(function_call_time)+'\n'
            arg='2. Входящие аргументы '+str(arg)+'\n'
            if answer is None:
                answer='-'
            answer="3. Ответ return (если есть, если нет то логгировать '-') "+str(answer)+'\n'
            function_end_time='4. Время завершения работы функции '+time.ctime(function_end_time)+'\n'
            function_time='5. Время работы функции '+str(function_time)
            with open(path, "w", encoding="utf8") as file:
                file.write(function_call_time)
                file.write(arg)
                file.write(answer)
                file.write(function_end_time)
                file.write(function_time)
            return result
        return wrapped
    return my_decorator

path='C:\\Users\\User\\PycharmProjects\\3semestr\\laboratory_4\\text_4.4.txt'
@decorator_maker_with_arguments(path)
def decorated_function_with_arguments(arg):
    arg=arg**2
    return arg

print(decorated_function_with_arguments(1234))




