#composition example
class parent:
    def __init__(self,name):
        self.name=name
    def onefun(self):
        print(self.name)
class child:
    def __init__(self,age):
        self.age=age
        self.obj_ref=parent('Murugesan_name')
        #composition (creating object,intialsing the parent class form the child class.
        self.obj_ref.onefun()
    def twofun(self):
        print(self.age)
child_obj=child(23)
child_obj.twofun()


#passing objects to another class
class Parent:
    def __init__(self,name):
        self.name=name
    def onefun(self):
        print(self.name)
class Child:
    def __init__(self,age,object):
        self.age=age
        self.object=object
    def twofun(self):
        print(self.age)
        self.object.onefun()
paren_obj=Parent("Dhoni")
child_obj=Child(23,paren_obj)
child_obj.twofun()


#MRO (Method Resolution Order) works on pri:Near  by search(1st inhertied is caught near by)
#pyytohn 2.7 will do deep search
class A:
    def fun(self):
        print("Inherited from A")
class B(A):
    def fun(self):
        print("Inherited from B")
class C(A):
    def fun(self):
        print("Inherited from C")
class D(C,B):
    pass
    # def fun(self):
    #     print("Inherited from D")

d=D()
d.fun()
