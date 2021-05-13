import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start= time.time()
        result=func(*args, **kwargs)
        end= time.time()
        print(func.__name__+" took"+str((end-start)*1000)+" mil sec")
        return result
    return wrapper
@time_it
def square(numbers):
    result=[]
    for numbers in numbers:
        result.append(numbers*numbers)
    return result
@time_it
def cube(numbers):
    result=[]
    for numbers in numbers:
        result.append(numbers*numbers*numbers)
    return result

array=range(1,100000)
first=square(array)
second= cube(array)
    
