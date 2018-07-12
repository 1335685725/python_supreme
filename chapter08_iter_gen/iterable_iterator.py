from collections import Iterator
class Company:
    def __init__(self, emoloyee_list):
        self.employee = emoloyee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __iter__(self):
        return MyIterator(self.emoloyee)

class MyIterator(Iterator):
    def __init__(self, emoloyee_list):
        self.iter_list = emoloyee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        # for 循环
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word
if __name__ == '__main__':
    company = Company(["tom", "bob", "jane"])
    my_iter = iter(company)
    while True:
        try:
            next(my_iter)
        except StopIteration:
            break
    for item in company:
        print(item)