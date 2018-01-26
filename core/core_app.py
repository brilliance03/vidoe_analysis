# -*- coding:utf-8 -*-
# proprammer = 'lizheng'

from queue import Queue
import threading
from pywinauto import Application
from PIL import Image
import time
import datetime

screenshot_queue = Queue()


class Log():
    @classmethod
    def log(self, invoker_name, message):
        '''静态输出方法'''
        self.__log_by_stdout(invoker_name, message)

    @classmethod
    def __log_by_stdout(self, invoker_name, message):
        str_output = '%s [%10s] %s' % (self.__get_current_time(), invoker_name, message)
        print(str_output)

    @classmethod
    def __log_by_logger(self, invoker_name, message):
        pass

    @classmethod
    def __get_current_time(self):
        '''将当前时间以yyyy-mm-dd HH:MM:SS格式输出'''
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')



class Captor(threading.Thread):
    '''捕获屏幕中的视频截图'''

    def __init__(self, name, screenshot_queue, app, monitor_list):
        threading.Thread.__init__(self, name=name)
        self.screenshot_queue = screenshot_queue
        self.app = app
        self.monitor_list = monitor_list

    def run(self):
        Log.log(self.getName(), '---屏幕捕获中---')
        while len(self.monitor_list) > 0:        # 当监视器列表中有元素的时候，一直循环
            target = self.monitor_list.pop(0)    # 每次取出监视器列表的第一个元素
            # 根据监视器列别表的名称，获取窗口中对应的wrapper元素
            item = self.get_monitor_item(target)
            screenshot_save_path = self.get_monitor_screenshot(
                item)         # 操作wrapper元素，在屏幕进行自动切换.并截图
            self.screenshot_queue.put(screenshot_save_path)
            Log.log(self.getName(), 'caputre one picture at ' +
                    screenshot_save_path)
        else:
            Log.log(self.getName(), '---此次轮询结束---')

    def get_monitor_item(self, target):
        '''根据传入的监控器名称，在窗口中获取对应的控件对象'''
        '''TODO: 代码实现'''
        return []

    def get_monitor_screenshot(self, wrapper_item):
        '''操作传入的控件对象，自动进行屏幕操作，截图。返回截图保存路径'''
        '''TODO: 代码实现'''
        # return 'd:\\test.png'
        return 'C:\\Users\\brill\\Desktop\\test.png'


class Analyser(threading.Thread):
    '''分析截取下来的视频截图'''

    def __init__(self, name, screenshot_queue):
        threading.Thread.__init__(self, name=name)
        self.screenshot_queue = screenshot_queue

    def run(self):
        while True:
            processing_screenshot = self.screenshot_queue.get()
            self.analysis(processing_screenshot)
            Log.log(self.getName(), 'get a picture from ' +
                    processing_screenshot)

    def analysis(self, screenshot_path):
        img = Image.open(screenshot_path)
        img.show()
        Log.log(self.getName(), 'Done')


def main():
    captor = Captor('Captor', screenshot_queue, 'app', [x for x in range(3)])
    analyser = Analyser('Analyser', screenshot_queue)

    captor.start()
    analyser.start()

    captor.join()
    analyser.join()

    Log.log(self.getName(), 'Over?')


if __name__ == '__main__':
    Log.log(__name__, 'test')
    main()
