def test(*params):
    print(params)


test(14, 'cat', 'c', 18, True)



def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))