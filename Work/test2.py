# a =[{'name': 'AA', 'price': 32.2, 'shares': 100},
# {'name': 'IBM', 'price': 91.1, 'shares': 50},
# {'name': 'CAT', 'price': 83.44, 'shares': 150},
# {'name': 'MSFT', 'price': 51.23, 'shares': 200},
# {'name': 'GE', 'price': 40.37, 'shares': 95},
# {'name': 'MSFT', 'price': 65.1, 'shares': 50},
# {'name': 'IBM', 'price': 70.44, 'shares': 100}]

# def stock_name(s):
#     return s['name']

# #print(a.sort(key=stock_name))
# print(sorted(a, key=lambda s: s['name']))

# def add(x, y):
#     def do_add():
#         print(f'Adding {x} + {y} -> {x+y}')
#         def dont_add():
#             print('hihi')
#             return x+y
#         return dont_add

#     return do_add

# k = add(3, 4)
# j=k()
# print(j())

import time

def after(seconds, func):
    time.sleep(seconds)
    print('Excuting function')
    func()

def greeting():
    print('Hello World')

def add(x, y):
    def do_add():
        print(f"Adding {x} + {y} -> {x+y}")
        return x+y
    return do_add

after(4, add(2, 3))
