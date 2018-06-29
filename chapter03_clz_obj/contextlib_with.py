import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    # contextmanager 修饰的函数必须是一个生成器, enter的代码可以放在yield之前来做
    yield {}
    # yield 后面是exit
    print("file close")

with file_open("bob.txt") as f_opener:
    print("file processing")