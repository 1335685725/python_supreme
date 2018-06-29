from chapter03_clz_obj.class_method import Date

class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year

class Student(User):
    def __init__(self, birthday):
        self.__birthday = birthday

        
if __name__ == '__main__':
    user = User(Date(1990, 2, 1))
    # print(user.__birthday) 私有属性 无法获取, 不能通过实例来访问
    print(user._User__birthday)  # Python底层是将birthday变形成这个形式来实现私有的
    # print(user._Student__birthday)
    print(user.get_age())
