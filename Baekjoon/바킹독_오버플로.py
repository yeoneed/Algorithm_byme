def func2():
    r =1 
    for i in range(1, 50):
        r = r*i%61
    return r

print(func2())