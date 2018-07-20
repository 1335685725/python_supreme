#pep380
import sys
sys.exc_info()
# 子生成器传递的值, 都是直接传递给调用方的,调用方通过send()发送的值都是直接传递给子生成器的, 如果发送的是None, 会调用子生成器的next方法
# 如果不是None, 会调用子生成器的send方法,
# 2. 子生成器退出的时候, 最后return EXPR ,会触发StopIteration(EXPR)异常
# 3. yield from表达式的值, 是子生成器终止时, 传递给StopIteration异常的第一个参数
# 4. 如果调用的时候出现了StopIteration异常, 委托生成器会回复运行, 同时其他异常会继续向上冒泡
# 5. 传入委托生成器的异常里,除了GeneratorExit异常, 其他所有异常全部传递给子生成器的.throw方法,如果调用.throw()出现了StopIteration
# 异常, 那就会回复委托生成器的运行,其他异常向上冒泡
# 6.如果委托生成器上调用.close()或传入GeneratorExit异常, 会调用子生成器的.close方法, 没有就不调用,如果调用.close方法时候抛出异常, 那么
# 就向上冒泡, 否则委托生成器抛出GeneratorExit异常