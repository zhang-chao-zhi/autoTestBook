# -*- coding: utf-8 -*-
from threading import Thread
from time import time, sleep


class DownFile(Thread):
    def __init__(self, file_name, cost_time):
        super().__init__()
        self.__name = file_name
        self.__time = cost_time

    def run(self):
        print('Start to download %s.....' % self.__name)
        sleep(self.__time)  # 模拟消耗时间
        print('%s finish download' % self.__name)


start = time()
task1 = DownFile('Python机器学习.pdf', 3)
task1.start()
task2 = DownFile('Golang编程指南.pdf', 4)
task2.start()
task3 = DownFile('细说PHP.pdf', 3)
task3.start()
task1.join()
task2.join()
task3.join()

end = time()
print("三个文件下载完成一共耗时：%.2f秒" % (end - start))
