def func(a,b,c,d=False,*args,**kwargs):
    print a, b, c, d, args, kwargs

func(*[1,2,3,4,5], **{'6':7})
func(*[1,2,3,], **{'e':7})
func(1, 2, *[3,], **{'e':7})
