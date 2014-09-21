import time

def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Time of function evaluation: \
{:f}".format(time.time()-t)
        return res
    return tmp

@timer
def func(x, y):
    return x + y

print func(1, 2)
