def func2(*args):
    for lim in args:
        if lim % 2 == 0:
            text = open('text.txt', 'a')
            text.write( f'{lim}={lim}\n')
func2(1,1,2,4,5,5,6,7,7,8,8,9,9,2,2)


def func228():
    text = open('text.txt', 'r')
    n = text.read()
    goga = {i: i for i in n if i not in ('=', '\n')}
    for key, value in goga.items():
        yield key,value

a = func228()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
