class Cat:
    def say(self):
        print("i am a cat")


class Dog:
    def say(self):
        print("i am a dog")


class Duck:
    def say(self):
        print("i am a duck")


class Company:
    def __init__(self, emoloyee_list):
        self.employee = emoloyee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

print("---------------------")

a = ["bo1", "bo2"]
b = ["bo2", "bo1"]
name_tuple = ["bo3", "bo4"]
name_set = set()
name_set.add("bo5")
name_set.add("bo6")
# a.extend(b)
# a.extend(name_set)
a.extend(company)
print(a)