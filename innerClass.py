# ********** Inner class *************
# QUE - how to acces member of one class to inside another class

class Employee:
    def __init__(self, eid,ename, esal):
        self.eid= eid
        self.ename= ename
        self.esal= esal
    def display(self):
        print('Employee id is : ', self.eid)
        print('Employee name is : ', self.ename)
        print('Employee salary is : ', self.esal)

class Increament():
    def inc(emp):
        emp.esal=emp.esal+10000
        emp.display()

e=Employee(101, 'Rahul', 20000)
Increament.inc(e)