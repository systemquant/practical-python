def custom_iter(obj):
    _iter = obj.__iter__()
    while True:
        try:
            print(_iter.__next__(), end='')
        except StopIteration:
            break

def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line

if __name__ == '__main__':
    # with open("Data/portfolio.csv") as f:
    #     custom_iter(f)
        
    #for line in filematch("Data/portfolio.csv", 'IBM'):
    #    print(line, end='')

    a = '''\    /\\
 )  ( ')
(  /  )
 \(__)|
'''

    print(a)

    for line in a.split('\n'):
        print('fmt.Println("' + line + '")')


