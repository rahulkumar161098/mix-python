# ***************** Inheritance ******************
# thie process of inheriting the properties of the parent class to th echild class is called inheritance

#  Types of inheritance
# 1 single (only one parent class and one child class)

# class P:
#     def m1(self):
#         print('Parent class')
# class C(P):
#     def m2(self):
#         print('Child class')
# o=C()
# o.m1()
# o.m2()


# ***********************************************************************************************
# Multi level inheritance
# base class to parent class to child class

# class P:
#     def m1(self):
#         print('Parent class')

# class C(P):
#     def m2(self):
#         print('Child class')

# class CC(C):
#     def m3(self):
#         print('sub-child class')
# o=CC()
# o.m1()
# o.m2()
# o.m3()

# ***********************************************************************************************

# Hierarichal inheritance
#  one parent but multiple child class at same level is called hierarichal inheritance

# class P:
#     def m1(self):
#         print('parent class')
# class C1(P):
#     def m2(self):
#         print('child1 class')
# class C2(P):
#     def m3(self):
#         print('child2 class')

# o=C1()
# o.m1()
# o.m2()
# print('**********************')
# o1=C2()
# o1.m1()
# o1.m3()


# ***********************************************************************************************

# Multiple inheritance
# multiple parent class but only one child class is called multiple class
# if m1 is not work properly then control goes to the m2 method

class P:
    def m1(self):
        print('first parent class')
class P2:
    def m1(self):
        print('second parent class')
class C(P, P2):
    pass

c=C()
c.m1()
