from wss.persion import persion


class Employee(persion):
    '员工类'
    empCount = 3

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
        print(self)
        print(self.__class__)
        print("Total Employee", Employee.empCount)

    def display_employee(self):
        print("Name", self.name, ",Salary", self.salary)


emp1 = Employee("carl", 2000)
emp1.display_count()
emp1.display_employee()
print(hasattr(emp1, 'name'))
print(getattr(emp1, 'name'))
print("Employee.__doc__", Employee.__doc__)
print("Employee.__name__", Employee.__name__)
print("Employee.__bases__", Employee.__bases__)
print("Employee.__dict__", Employee.__dict__)
print("Employee.__module__", Employee.__module__)


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')

    def __str__(self):
        return


p = Parent()
c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值
print(issubclass(Child, Parent))
print(isinstance(c, Child))
print(isinstance(c, Parent))


class Vecor:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d,%d)'


class JustCounter:
    # 私有变量
    __secretCount = 0
    # 公开变量
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print("私有变量值", self.__secretCount)

    def getSecretCount(self):
        return self.__secretCount


just1 = JustCounter()
just1.count()
just1.count()
# print(just1.__secretCount) 报错，实例不能访问私有变量
try:
    print(just1.__secretCount)
except Exception as e:
    print('报错，实例不能访问私有变量', e)
else:
    print('没有报错')

print(just1.publicCount)
print(just1.getSecretCount())
# object._className__attrName 访问属性（包括私有属性）
print(just1._JustCounter__secretCount)
