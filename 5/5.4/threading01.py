# -*- coding: utf-8 -*-
import threading
import time


def writing_novel():
    for x in range(3):
        print('%s正在写小说' % x)
        time.sleep(1)


def running():
    for x in range(3):
        print('%s正在跑步' % x)
        time.sleep(1)


def playing_game():
    for x in range(3):
        print('%s正在玩游戏' % x)
        time.sleep(1)


def single_thread():
    writing_novel()
    running()
    playing_game()


def multi_thread():
    t1 = threading.Thread(target=writing_novel)
    t2 = threading.Thread(target=running)
    t3 = threading.Thread(target=playing_game)

    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    multi_thread()