def square():
    i=1
    while True:
        yield i*i
        i+=1

for n in square():
    if n> 25:
        break
    print(n)