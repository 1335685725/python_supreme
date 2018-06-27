class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):
        return ",".join(self.employee)

    def __repr__(self):
        return ",".join(self.employee)


company = Company(["tom", "bob", "jane"])

print(company)

print("------------------")


class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        re_vector = MyVector(self.x + other.x, self.y + other.y)
        return re_vector

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


first_vector = MyVector(1, 3)
second_vector = MyVector(2, 4)
res_vector = first_vector + second_vector
print(res_vector)
