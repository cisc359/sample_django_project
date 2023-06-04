
def f(*a, **kwargs ):
    """

    :param kwargs:
    :return:
    """

    for (key, value) in kwargs.items():
        print("The value of {} is {}".format(key, value))


#f(10)
#f(a = 10)
#f(1, 2)

tuple = (2,3,4)

map = {'a':1, 'b':2}

map = dict(a=3,b=4)

f(*tuple, **map)



