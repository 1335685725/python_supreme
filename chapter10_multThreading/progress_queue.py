import time
from multiprocessing import Process, Queue, Pool, Manager,Pipe

# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == '__main__':
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(queue,))
#     my_consumer = Process(target=consumer, args=(queue,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# 共享全局变量不能用于多进程, 可以适用于多线程
# def producer(a):
#     a +=1
#     time.sleep(2)
#
# def consumer(a):
#     print(a)
#
# if __name__ == '__main__':
#     a = 1
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# multiprocessing中的queue不能用于进程池, 但是Manager().Queue()可以
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == '__main__':
#     queue = Manager().Queue(10)
#     pool = Pool()
#
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))
#
#     pool.close()
#     pool.join()

# 通过Pipe实现进程中通信
# pipe 性能高于queue
# def producer(pipe):
#     pipe.send("bbb")
#
# def consumer(pipe):
#     print(pipe.recv())
#
# if __name__ == '__main__':
#     recev_pipe, send_pipe = Pipe()
#     # pipe只能用于两个进程中的通信
#     my_producer = Process(target=producer, args=(send_pipe,))
#     my_consumer = Process(target=consumer, args=(recev_pipe,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# dict
def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == '__main__':
    progress_dict = Manager().dict()
    first_progress = Process(target=add_data, args=(progress_dict, "b", 1))
    second_progress = Process(target=add_data, args=(progress_dict, "bb", 2))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()
    print(progress_dict)