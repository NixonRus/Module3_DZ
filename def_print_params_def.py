def print_params(a = 1, b = 'dark', c = True):
    print(a, b, c)

print_params()
print_params(3, 45)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Fuel', False, 74]
values_dict = {'a': True, 'b': 7, 'c': 'Audi'}


print_params(*values_list)
print_params(**values_dict)

values_list_2 = [21, 'DOMO']

print_params(*values_list_2, 42)