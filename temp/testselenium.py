#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument(
#     'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36')
#
# driver = Chrome(r"D:\pro-code\local code\aiqiyi\config\chromedriver.exe", options=chrome_options)
#
# with open(r'D:\pro-code\local code\aiqiyi\temp\stealth.min.js') as f:
#     js = f.read()
#
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": js
# })
driver = Firefox()
driver.get('https://www.youku.com/')
time.sleep(5)
driver.save_screenshot('./walkaround.png')

# 你可以保存源代码为 html 再双击打开，查看完整结果
source = driver.page_source
with open('./result.html', 'w') as f:
    f.write(source)
