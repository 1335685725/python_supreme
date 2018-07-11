def add(a, b):
    a += b
    return a

class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == '__main__':
    com1 = Company("com1" ,["bo1", "bo2"])
    com1.add("bo3")
    com1.remove("bo1")
    print(com1.staffs)

    com2 = Company("com2")
    com2.add("bo4")
    print(com2.staffs)

    com3 = Company("com3")
    com3.add("bo5")
    print(com3.staffs)  # ['bo4', 'bo5']
    print(com3.staffs is com2.staffs) # True
    '''
    com2和com3都使用了默认参数 列表, 列表是可变的, 他们共用了同一个[]
    '''
    print(Company.__init__.__defaults__)
    print("----------------------")

    a = 1
    b = 2
    c = add(a, b)
    print(c)
    print(a, b)

    print("----------------------")

    a = [1, 2]
    b = [3, 4]
    c = add(a, b)
    print(c)
    print(a, b)

    print("----------------------")

    a = (1, 2)
    b = (3, 4)
    c = add(a, b)
    print(c)
    print(a, b)
