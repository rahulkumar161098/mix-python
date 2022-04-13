# gen=(x*x for x in range(100000000000000000000000000000000))
# while True:
#     print(next(gen))


def fac(num):
    a, b=0,1
    while True:
        if a<=num:
            print(a)
            a,b=b,a+b
            

fac(100)