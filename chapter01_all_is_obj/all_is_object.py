'''
python中一切皆对象
'''

def ask(name="asd"):
    '''
    函数也是对象
    :param name:
    :return:
    '''
    print(name)

myfunc = ask
myfunc()

print("------------------------")

class Person():
    '''
    类也是对象
    '''
    def __init__(self):
        print("boooo")

my_class = Person
my_class()

print("------------------------")

'''可以添加到集合对象中去'''
obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())
# 四个值， 一个打印值一个返回值

print("------------------------")

'''函数可以作为返回值'''
def my_decorator():
    print("dec start")
    return ask

my_ask = my_decorator()
my_ask("liangben")