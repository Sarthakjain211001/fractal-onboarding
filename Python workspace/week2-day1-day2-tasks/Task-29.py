def recrusive_fun(x):
    if(x == 0):
        return 1
    return x*recrusive_fun(x-1)

print(recrusive_fun(5))
print(recrusive_fun(10))
print(recrusive_fun(1))
print(recrusive_fun(0))

