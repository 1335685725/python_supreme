from datetime import datetime, date

class User:
    def __init__(self, name: str, birthday: date):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

# 逻辑代码尽量写在main中, 如果写在外面, 别的文件import这个文件时就会执行
if __name__ == '__main__':
    user = User("bo1", date(year=1997, month=5, day=11))
    user.age = 30
    print(user._age)
    print(user.age)
