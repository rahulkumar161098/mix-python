# *************************************************************************************************8
# ************* class method ****************

#  @classmethod
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walk with {} legs'.format(name, cls.legs))
# with reference variable
a=Animal()
a.walk('Dog')
# without reference varialbe
Animal.walk('cat')


#  WAP to track number of object created for a class
class Count:
    count=0
    def __init__(self):
        Count.count=Count.count+1
    @classmethod
    def noOfObject(cls):
        print('no of objects are', cls.count)

c1=Count()
c2=Count()
c3=Count()
c4=Count()
c5=Count()
Count.noOfObject()


# *****************************************************************************************************
# ********** Static method *************
# Just general utility method/helper method

# Eng

class Cal:

    @staticmethod
    def add(x,y):
        print('sum of two number is: ', x+y)
    @staticmethod
    def mul(x,y):
        print('product of two number is: ', x*y)
    @staticmethod
    def avg(x,y):
        print('Average of two number is: ', (x+y)/2)
c=Cal()
c.add(3,4)
c.mul(3,4)
c.avg(3,4)