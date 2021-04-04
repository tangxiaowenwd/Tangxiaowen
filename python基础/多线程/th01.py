#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2021/3/21 20:22
# Author  : TangXiaowen
import threading as th
import time

class Main():
    def __init__(self):
        pass

    def main(self):
        pass

def process():
    for i in range(4):
        time.sleep(1)
        print("当前线程是 %s" %th.current_thread().name)

if __name__ == "__main__":
    ta = [th.Thread(target=process) for i in range(4)]
    for i in ta:
        i.start()
    for i in ta:
        i.join()
