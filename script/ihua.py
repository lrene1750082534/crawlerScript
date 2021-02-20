#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver


class Ihua:
    def __init__(self):
        self.browser = webdriver.Chrome(r"D:\pro-code\local code\aiqiyi\config\chromedriver.exe")
        self.ips = []  # 临时存储结果，便于最后持久化保存

    def dealips(self, ipstr):
        '''
        处理获取的结果，截取有用的信息
        :param ipstr: 从页面获取的结果文本
        :return:
        '''
        try:
            iplist = ipstr.split(" ")
            for ip in iplist[:21]:
                if ip == "":
                    continue
                moudle = re.compile(
                    r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]):\d{0,5}')
                result = re.findall(moudle, ip)
                self.ips.append(result[0])
            self.save()
        except Exception as e:
            print("dealips error:", e)

    def content(self):
        '''
        请求对应页面获取结果
        :return:
        '''
        try:
            print("start")
            date = time.strftime("%Y/%m/%d")
            url = "https://ip.ihuan.me/today/" + date + "/09.html"
            print("requests url:", url)
            self.browser.get(url)
            time.sleep(3)
            page_source = self.browser.page_source
            soup = BeautifulSoup(str(page_source), 'lxml')
            ipstr = str(soup.find('p', class_='text-left').text)
            self.dealips(ipstr)
        except Exception as e:
            print("content error:", e)

    def save(self):
        '''
        保存最终结果，输入到文本
        :return:
        '''
        try:
            if os.path.exists("proxy_IP/hosts.txt"):
                os.remove("proxy_IP/hosts.txt")
            file_write_obj = open("proxy_IP/hosts.txt", 'w')
            for var in self.ips:
                file_write_obj.write(var + '\n')
            file_write_obj.close()
            print("保存文件成功")
            return
        except Exception as e:
            print("save error:", e)


if __name__ == '__main__':
    Ihua().content()
