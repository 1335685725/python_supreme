class Company:
    def __init__(self, emoloyee_list):
        self.employee = emoloyee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])
emploee = company.employee
for em in emploee:
    print(em)

print("**********实现了__getitem__*************")
'''先尝试找__iter__才会去找__getitem__'''
company1 = company[:2]
for em in company1:
    print(em)
'''先尝试__len__才会去找__getitem__'''
print(len(company1))
