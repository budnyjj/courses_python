class Simple:
    """ Simple class with private attribute """
    def __init__(self, count, str):
        self.__private_attr = 20
        print self.__private_attr
 
s = Simple(1,'22')
print s.__private_attr
