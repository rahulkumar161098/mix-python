# ************ Plymorphism ***************
# polymorphism is the ability of an object to take on many forms

# operator overloading



class books:
    def __init__(self, pages):
        self.pages= pages
    
    def __add__(self,other):
        return self.pages+other.pages
    
    def __sub__(self,other):
        return self.pages- other.pages
    
    def __mul__(self,other):
        return self.pages*other.pages

b1=books(300)
b2= books(500)
print(b1+b2)
print(b1-b2)
print(b1*b2)


'''1,2,4,8,16,32,64,128,256,512,1024'''
# sum=1
# for i in range(20):
#     sum=sum*2
#     print(sum)

class Test:
    def __init__(self,*a):
        print('constractor with any number of argumnets')

t=Test()
t=Test(12)
t=Test(12,34)
t=Test(12,45,556,2324)