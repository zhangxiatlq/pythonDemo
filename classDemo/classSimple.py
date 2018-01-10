class Employee:
    '所有哦员工的基类'
    empCount = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmplyee(self):
        print("Name:",self.name,"  age:",self.age)

    def prt(self): #self不是关键字，可以随意命名
        print(self)
        print(self.__class__)

if __name__ == "__main__":
    emp1 = Employee("xiaoming",25)
    emp2 = Employee("xiaoqiang",30)
    print(emp1.displayEmplyee())
    print(emp2.displayEmplyee())
    t = Employee;
    t.__init__(t,"xiaozhang",20)
    print(t.displayEmplyee(t))
