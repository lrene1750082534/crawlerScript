# coding=utf-8
import re

# unitelog.UniteLogger.Infof("RecieveOrder : %+v", result[0])

# def is_all_chinese(strs):
#     for i in strs:
#         if not '\u4e00' <= i <= '\u9fa5':
#             return False
#     return True

# temp = is_all_chinese("铭记历史:大地遗孤")
# print(temp)

# lower_case_documents = ['Hello, how are you!', 'Win money, win from home.', 'Call me now.',
#                         'Hello, Call hello you tomorrow?']
# sans_punctuation_documents = []
# import string
# astr = "All's Well End's Well, Too"
#
# # for i in lower_case_documents:
# trantab = str.maketrans({key: None for key in string.punctuation})
# j = astr.translate(trantab)
# sans_punctuation_documents.append(j)

# print(j)
# j = j.replace(" ", "")
# if j.isalpha():
#     print("111111111111111111")
# else:
#     print("0000000000000000000")


#
# astr = "盲侠金鱼飞天猪"
# astr = "大清后宫（又名：大清后宫之还君明珠）（外判剧集）"
# astr = "笨小孩（原名：不一样的天空）合拍剧集"
# temp = re.findall(r"[（](.*?)[）]", astr)
# print("123", temp)
# # if not temp:
#     print("-------")
# # # name = temp[0].split("：")
# # # print(name[1])
# pattern = re.compile("又名")
# m = pattern.search(temp[0])
# if m:
#     print("==============")
# else:
#     print("++++++++++++")
# astr = "笨小孩（原名：不一样的天空）合拍剧集"
# rs = re.findall(r'([^（\）]+)(?:$|\（)', astr)
# print("rs:", rs)
# # ([^[\]]+)   # match one or more characters that are not '[' or ']' and place in group 1
# (?:$|\[)    # match either a '[' or at the end of the string, do not capture
# import re

# item = '大清后宫之-还君明珠'
# # item = '<h1>[风之领域] NO.056 纯纯的女孩 写真集 / 第2页</h1>'
# # item = re.sub(u"([^\u4e00-\u9fa5])","",item)
#
#
# item = re.findall(r'[^<>/h1第0-9页a-zA-Z- .]', item)
# # 正则去除^<>/h1第0-9页a-zA-Z . 这些符号
# item = ''.join(item)
# # item = item.replace('[', '').replace(']', '')
# # 正则去除[]
#
# print(item)

# from difflib import SequenceMatcher
#
#
# def similarity(a, b):
#     return SequenceMatcher(None, a, b).ratio()
#
#
# print(similarity('风流才子苏东坡', '风流才子-苏东坡'))
# 笨小孩

# res = None
# if not res:
#     print("================")
# else:
#     print("--------------")

# str= r"<?xml version=\"1.0\" encoding=\"UTF-8\"?><Mediainfo version=\"0.7.71\"><File><track type=\"General\"><Count>305</Count><Count_of_stream_of_this_kind>1</Count_of_stream_of_this_kind><Kind_of_stream>General</Kind_of_stream><Kind_of_stream>General</Kind_of_stream><Stream_identifier>0</Stream_identifier><Count_of_video_streams>1</Count_of_video_streams><Count_of_audio_streams>1</Count_of_audio_streams><Video_Format_List>AVC</Video_Format_List><Video_Format_WithHint_List>AVC</Video_Format_WithHint_List><Codecs_Video>AVC</Codecs_Video><Video_Language_List>English</Video_Language_List><Audio_Format_List>AAC</Audio_Format_List><Audio_Format_WithHint_List>AAC</Audio_Format_WithHint_List><Audio_codecs>AAC LC</Audio_codecs><Audio_Language_List>English</Audio_Language_List><Complete_name>11 树懒慢吞吞_IPTV.mp4</Complete_name><File_name>11 树懒慢吞吞_IPTV</File_name><File_extension>mp4</File_extension><Format>MPEG-4</Format><Format>MPEG-4</Format><Format_Extensions_usually_used>mp4 m4v m4a m4b m4p 3gpp 3gp 3gpp2 3g2 k3g jpm jpx mqv ismv isma f4v</Format_Extensions_usually_used><Commercial_name>MPEG-4</Commercial_name><Format_profile>Base Media / Version 2</Format_profile><Internet_media_type>video/mp4</Internet_media_type><Codec_ID>mp42</Codec_ID><Codec_ID_Url>http://www.apple.com/quicktime/download/standalone.html</Codec_ID_Url><Codec>MPEG-4</Codec><Codec>MPEG-4</Codec><Codec_Extensions_usually_used>mp4 m4v m4a m4b m4p 3gpp 3gp 3gpp2 3g2 k3g jpm jpx mqv ismv isma f4v</Codec_Extensions_usually_used><File_size>248460390</File_size><File_size>237 MiB</File_size><File_size>237 MiB</File_size><File_size>237 MiB</File_size><File_size>237 MiB</File_size><File_size>237.0 MiB</File_size><Duration>191200</Duration><Duration>3mn 11s</Duration><Duration>3mn 11s 200ms</Duration><Duration>3mn 11s</Duration><Duration>00:03:11.200</Duration><Duration>00:03:11:05</Duration><Duration>00:03:11.200 (00:03:11:05)</Duration><Overall_bit_rate_mode>VBR</Overall_bit_rate_mode><Overall_bit_rate_mode>Variable</Overall_bit_rate_mode><Overall_bit_rate>10395832</Overall_bit_rate><Overall_bit_rate>10.4 Mbps</Overall_bit_rate><Frame_rate>25.000</Frame_rate><Frame_rate>25.000 fps</Frame_rate><Frame_count>4780</Frame_count><Stream_size>551331</Stream_size><Stream_size>538 KiB (0%)</Stream_size><Stream_size>538 KiB</Stream_size><Stream_size>538 KiB</Stream_size><Stream_size>538 KiB</Stream_size><Stream_size>538.4 KiB</Stream_size><Stream_size>538 KiB (0%)</Stream_size><Proportion_of_this_stream>0.00222</Proportion_of_this_stream><HeaderSize>549622</HeaderSize><DataSize>247910768</DataSize><FooterSize>0</FooterSize><IsStreamable>Yes</IsStreamable><Encoded_date>UTC 2020-12-31 08:48:39</Encoded_date><Tagged_date>UTC 2020-12-31 08:48:46</Tagged_date><File_last_modification_date>UTC 2021-01-28 06:12:02</File_last_modification_date><File_last_modification_date__local_>2021-01-28 14:12:02</File_last_modification_date__local_><TIM>00:00:00:00</TIM><TSC>25</TSC><TSZ>1</TSZ></track><track type=\"Video\"><Count>297</Count><Count_of_stream_of_this_kind>1</Count_of_stream_of_this_kind><Kind_of_stream>Video</Kind_of_stream><Kind_of_stream>Video</Kind_of_stream><Stream_identifier>0</Stream_identifier><StreamOrder>0</StreamOrder><ID>1</ID><ID>1</ID><Format>AVC</Format><Format_Info>Advanced Video Codec</Format_Info><Format_Url>http://developers.videolan.org/x264.html</Format_Url><Commercial_name>AVC</Commercial_name><Format_profile>Main@L4.1</Format_profile><Format_settings>CABAC / 3 Ref Frames</Format_settings><Format_settings__CABAC>Yes</Format_settings__CABAC><Format_settings__CABAC>Yes</Format_settings__CABAC><Format_settings__ReFrames>3</Format_settings__ReFrames><Format_settings__ReFrames>3 frames</Format_settings__ReFrames><Internet_media_type>video/H264</Internet_media_type><Codec_ID>avc1</Codec_ID><Codec_ID_Info>Advanced Video Coding</Codec_ID_Info><Codec_ID_Url>http://www.apple.com/quicktime/download/standalone.html</Codec_ID_Url><Codec>AVC</Codec><Codec>AVC</Codec><Codec_Family>AVC</Codec_Family><Codec_Info>Advanced Video Codec</Codec_Info><Codec_Url>http://developers.videolan.org/x264.html</Codec_Url><Codec_CC>avc1</Codec_CC><Codec_profile>Main@L4.1</Codec_profile><Codec_settings>CABAC / 3 Ref Frames</Codec_settings><Codec_settings__CABAC>Yes</Codec_settings__CABAC><Codec_Settings_RefFrames>3</Codec_Settings_RefFrames><Duration>191200</Duration><Duration>3mn 11s</Duration><Duration>3mn 11s 200ms</Duration><Duration>3mn 11s</Duration><Duration>00:03:11.200</Duration><Duration>00:03:11:05</Duration><Duration>00:03:11.200 (00:03:11:05)</Duration><Bit_rate>10055371</Bit_rate><Bit_rate>10.1 Mbps</Bit_rate><Width>1920</Width><Width>1 920 pixels</Width><Height>1080</Height><Height>1 080 pixels</Height><Pixel_aspect_ratio>1.000</Pixel_aspect_ratio><Display_aspect_ratio>1.778</Display_aspect_ratio><Display_aspect_ratio>16:9</Display_aspect_ratio><Rotation>0.000</Rotation><Frame_rate_mode>CFR</Frame_rate_mode><Frame_rate_mode>Constant</Frame_rate_mode><Frame_rate>25.000</Frame_rate><Frame_rate>25.000 fps</Frame_rate><Frame_count>4780</Frame_count><Standard>PAL</Standard><Resolution>8</Resolution><Resolution>8 bits</Resolution><Colorimetry>4:2:0</Colorimetry><Color_space>YUV</Color_space><Chroma_subsampling>4:2:0</Chroma_subsampling><Bit_depth>8</Bit_depth><Bit_depth>8 bits</Bit_depth><Scan_type>Progressive</Scan_type><Scan_type>Progressive</Scan_type><Interlacement>PPF</Interlacement><Interlacement>Progressive</Interlacement><Bits__Pixel_Frame_>0.194</Bits__Pixel_Frame_><Stream_size>240323373</Stream_size><Stream_size>229 MiB (97%)</Stream_size><Stream_size>229 MiB</Stream_size><Stream_size>229 MiB</Stream_size><Stream_size>229 MiB</Stream_size><Stream_size>229.2 MiB</Stream_size><Stream_size>229 MiB (97%)</Stream_size><Proportion_of_this_stream>0.96725</Proportion_of_this_stream><Language>en</Language><Language>English</Language><Language>English</Language><Language>en</Language><Language>eng</Language><Language>en</Language><Encoded_date>UTC 2020-12-31 08:48:39</Encoded_date><Tagged_date>UTC 2020-12-31 08:48:39</Tagged_date><colour_description_present>Yes</colour_description_present><Color_primaries>BT.709</Color_primaries><Transfer_characteristics>BT.709</Transfer_characteristics><Matrix_coefficients>BT.709</Matrix_coefficients><Color_range>Limited</Color_range></track><track type=\"Audio\"><Count>246</Count><Count_of_stream_of_this_kind>1</Count_of_stream_of_this_kind><Kind_of_stream>Audio</Kind_of_stream><Kind_of_stream>Audio</Kind_of_stream><Stream_identifier>0</Stream_identifier><StreamOrder>1</StreamOrder><ID>2</ID><ID>2</ID><Format>AAC</Format><Format_Info>Advanced Audio Codec</Format_Info><Commercial_name>AAC</Commercial_name><Format_profile>LC</Format_profile><Codec_ID>40</Codec_ID><Codec>AAC LC</Codec><Codec>AAC LC</Codec><Codec_Family>AAC</Codec_Family><Codec_CC>40</Codec_CC><Duration>191200</Duration><Duration>3mn 11s</Duration><Duration>3mn 11s 200ms</Duration><Duration>3mn 11s</Duration><Duration>00:03:11.200</Duration><Duration>00:03:11.200</Duration><Source_duration>191253</Source_duration><Source_duration>3mn 11s</Source_duration><Source_duration>3mn 11s 253ms</Source_duration><Source_duration>3mn 11s</Source_duration><Source_duration>00:03:11.253</Source_duration><Bit_rate_mode>VBR</Bit_rate_mode><Bit_rate_mode>Variable</Bit_rate_mode><Bit_rate>317375</Bit_rate><Bit_rate>317 Kbps</Bit_rate><Maximum_bit_rate>408375</Maximum_bit_rate><Maximum_bit_rate>408 Kbps</Maximum_bit_rate><Channel_s_>2</Channel_s_><Channel_s_>2 channels</Channel_s_><Channel_positions>Front: L R</Channel_positions><Channel_positions>2/0/0</Channel_positions><ChannelLayout>L R</ChannelLayout><Sampling_rate>48000</Sampling_rate><Sampling_rate>48.0 KHz</Sampling_rate><Samples_count>9177600</Samples_count><Frame_count>8963</Frame_count><Source_frame_count>8965</Source_frame_count><Compression_mode>Lossy</Compression_mode><Compression_mode>Lossy</Compression_mode><Stream_size>7585686</Stream_size><Stream_size>7.23 MiB (3%)</Stream_size><Stream_size>7 MiB</Stream_size><Stream_size>7.2 MiB</Stream_size><Stream_size>7.23 MiB</Stream_size><Stream_size>7.234 MiB</Stream_size><Stream_size>7.23 MiB (3%)</Stream_size><Proportion_of_this_stream>0.03053</Proportion_of_this_stream><Source_stream_size>7587379</Source_stream_size><Source_stream_size>7.24 MiB (3%)</Source_stream_size><Source_stream_size>7 MiB</Source_stream_size><Source_stream_size>7.2 MiB</Source_stream_size><Source_stream_size>7.24 MiB</Source_stream_size><Source_stream_size>7.236 MiB</Source_stream_size><Source_stream_size>7.24 MiB (3%)</Source_stream_size><Source_StreamSize_Proportion>0.03054</Source_StreamSize_Proportion><Language>en</Language><Language>English</Language><Language>English</Language><Language>en</Language><Language>eng</Language><Language>en</Language><Encoded_date>UTC 2020-12-31 08:48:39</Encoded_date><Tagged_date>UTC 2020-12-31 08:48:39</Tagged_date></track></File></Mediainfo>"
# rs = re.findall(r'<File_size>(.*?)</File_size>',str)[0]
# print(rs)
# res = re.findall(r'<Overall_bit_rate>(.*?)</Overall_bit_rate>',str)[0]
# print(res)
# res1 = re.findall(r'<Duration>(.*?)</Duration>',str)
# print(res1)
# res2 = re.findall(r'<Format>(.*?)</Format>',str)[0]
# print(res2)
# res3 = re.findall(r'<Width>(.*?)</Width>',str)[0]
# print(res3)
# res4 = re.findall(r'<Height>(.*?)</Height>',str)[0]
# print(res4)

# id = [1]
# lst = []
# for i in id:
#     lst.append(i)
# ids = ",".join('%s' % j for j in lst)
# print(ids)


# alst = ['又名: 异度任务']
# name = alst[0]
# lst2 = name.split("：")
# print("lst2:", lst2)
# if len(lst2) == 1:
#     print("-----------------+")


# !/usr/bin/python

# import time
#
# ## dd/mm/yyyy格式
# # print (time.strftime("%d/%m/%Y"))
# print(time.strftime("%Y/%m/%d"))

# import re
# import os
#
# ips = []
# str = '175.43.33.11:9999@HTTP#[高匿]福建泉州 联通#支持HTTPS#支持POST118.24.128.46:1080@HTTP#[高匿]四川成都 电信/联通/移动#支持POST220.249.149.111:9999@HTTP#[高匿]福建南平 联通#支持HTTPS#支持POST58.253.157.193:9999@HTTP#[高匿]广东揭阳 联通#支持HTTPS#支持POST175.44.109.248:9999@HTTP#[高匿]福建南平 联通#支持HTTPS#支持POST175.42.158.66:9999@HTTP#[高匿]福建南平 联通#支持HTTPS#支持POST175.42.129.42:9999@HTTP#[高匿]福建南平 联通#支持HTTPS#支持POST58.253.152.233:9999@HTTP#[高匿]广东揭阳 联通175.43.56.3:9999@HTTP#[高匿]福建泉州 联通#支持HTTPS#支持POST220.189.70.176:8888@HTTP#[高匿]浙江嘉兴 电信#支持HTTPS#支持POST27.43.187.232:9999@HTTP#[高匿]广东揭阳 联通#支持HTTPS#支持POST222.189.191.207:9999@HTTP#[高匿]江苏扬州 电信#支持HTTPS#支持POST223.242.224.155:9999@HTTP#[高匿]安徽淮南 电信#支持HTTPS#支持POST58.253.159.52:9999@HTTP#[高匿]广东揭阳 联通#支持HTTPS#支持POST27.43.190.139:9999@HTTP#[高匿]广东揭阳 联通#支持HTTPS#支持POST175.42.123.183:9999@HTTP#[高匿]福建宁德 联通183.166.21.161:9999@HTTP#[高匿]安徽淮南 电信#支持HTTPS#支持POST49.70.99.104:9999@HTTP#[高匿]江苏宿迁 电信#支持HTTPS#支持POST183.166.20.250:9999@HTTP#[高匿]安徽淮南 电信#支持HTTPS#支持POST183.166.71.148:9999@HTTP#[高匿]安徽淮南 电信#支持HTTPS#支持POST222.189.190.232:9999@HTTP#[高匿]江苏扬州 电信#支持HTTPS#支持POST223.247.168.79:9999@HTTP#[高匿]安徽芜湖 电信#支持HTTPS#支持POST118.24.172.149:1080@HTTP#[高匿]四川成都 电信/联通/移动#支持POST183.166.21.126:9999@HTTP#[高匿]安徽淮南 电信#支持HTTPS#支持POST223.242.225.30:9999@HTTP#[高匿]安徽淮南 电信#支持HTTPS#支持POST58.253.156.253:9999@HTTP#[高匿]广东揭阳 联通#支持HTTPS#支持POST49.86.26.10:9999@HTTP#[高匿]江苏扬州 电信#支持HTTPS#支持POST58.253.152.238:9999@HTTP#[高匿]广东揭阳 联通#支持HTTPS#支持POST175.42.122.41:9999@HTTP#[高匿]福建宁德 联通#支持HTTPS#支持POST175.42.128.212:9999@HTTP#[高匿]福建南平 联通#支持HTTPS#支持POST175.42.128.193:9999@HTTP#[高匿]福建南平'
# iplist = str.split(" ")
# print("iplist:", iplist)
# for ip in iplist[:21]:
#     moudle = re.compile(r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5]):\d{0,5}')
#     result = re.findall(moudle, ip)
#     print("re:", result)
#     ips.append(result[0])
# if os.path.exists("dest.txt"):
#     os.remove("dest.txt")
# file_write_obj = open("dest.txt", 'w')  # 新文件
# for var in ips:
#     file_write_obj.write(var + '\n')  # 逐行写入
# file_write_obj.close()
# print("保存文件成功")
# import requests
# import os
# import time
# import requests
# from bs4 import BeautifulSoup

import requests

def test_proxy():
    N = 1
    url = 'https://www.baidu.com'
    fp = open(r'D:\pro-code\local code\aiqiyi\proxy_IP\host.txt', 'r')
    ips = fp.readlines()
    # proxys = list()
    # for p in ips:
    #     print("p:", p)
    #     ip = p.strip('\n').split(':')
    #     print("ip:", ip)
    #     proxy = 'http:\\' + ip[0] + ':' + ip[1]
    #     proxies = {'proxy': proxy}
    #     proxys.append(proxies)
    proxys = [{'proxy': 'http:\\182.96.51.4:4232'},{'proxy': 'http:\\120.38.64.233:4245'}]
    for pro in proxys:
        try:
            s = requests.get(url, proxies=pro)
            print('第{}个ip：{} 状态{}'.format(N, pro, s.status_code))
        except Exception as e:
            print(e)
        N += 1


test_proxy()

# import urllib.request
#
# url = "https://www.baidu.com/"
# file = urllib.request.urlopen(url)
# print('获取当前url:', file.geturl())
# print('file.getcode,HTTPResponse类型:', file.getcode)
# print('file.info 返回当前环境相关的信息：\n', file.info())
# import json
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# # caps = DesiredCapabilities.CHROME
# # caps['loggingPrefs'] = {'performance': 'ALL'}
# # 78版本的chrome需要加这个，https://stackoverflow.com/questions/56812190/protractor-log-type-performance-not-found-error
# caps = {
#     'browserName': 'chrome',
#     'loggingPrefs': {
#         'browser': 'ALL',
#         'driver': 'ALL',
#         'performance': 'ALL',
#     },
#     'goog:chromeOptions': {
#         'perfLoggingPrefs': {
#             'enableNetwork': True,
#         },
#         'w3c': False,
#     },
# }
# driver = webdriver.Chrome(r"D:\pro-code\local code\aiqiyi\config\chromedriver.exe", desired_capabilities=caps)
# # driver = webdriver.Chrome(desired_capabilities=caps)
#
# driver.get('https://search.douban.com/movie/subject_search?search_text=%E7%94%B5%E8%A7%86%E9%A3%8E%E4%BA%91&cat=1002')
#
# logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]
#
# with open('./devtools.json', 'w') as f:
#     json.dump(logs, f)
#
# driver.close()


# from selenium import webdriver
#
# driver_path = r'D:\pro-code\local code\aiqiyi\config\chromedriver.exe'  # 这是chrome驱动路径
#
# # 自定义代理IP 及 请求头。
# chromeOptions = webdriver.ChromeOptions()
# # chromeOptions.add_argument("--proxy-server=http://218.93.119.165:9002")
# chromeOptions.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36')
#
# browser = webdriver.Chrome(executable_path=driver_path,chrome_options=chromeOptions)
#
# browser.get("https://search.douban.com/movie/subject_search?search_text=%E7%94%B5%E8%A7%86%E9%A3%8E%E4%BA%91&cat=1002")  # 查看IP是否切换。
#
# # 获取请求头信息
# agent = browser.execute_script("return navigator")
# print(agent)  # 查看请求头是否更改。
#
# from openpyxl import load_workbook
# path = "./香港亚视电视台-本地生产项目清单（2020-2015年内容）_41.xlsx"
# wb = load_workbook(path)
# sheet_name = wb.sheetnames[0]
# ws = wb[sheet_name]
# ws['AM4'] = "豆瓣"
# for i in range(5, ws.max_row + 1):
#     y = 'AM' + str(i)
#     name = ws[i][3].value  # 中文名
#     engname = ws[i][2].value  # 英文名
#     print('正在查找《{}》的英文名称。。。'.format(name))
#     print('表格提供的英文名称《{}》。。。'.format(engname))
#     # e_name = self.get_ename(name, engname)
#     # if e_name:
#     #     ws[y].value = "有"
#     # else:
#     #     ws[y].value = "无"
#     wb.save(path)
#     time.sleep(2)

# e_name= (True, 'Battle Field Network')
# eng='Battlefield Network'
# ''.join(e_name[1].split())
#
# print("1:",''.join(e_name[1].split()).lower())
# print("2:",''.join(eng.split()).lower())
# if eng == e_name[1]:
#     print(">>>>>>>>>>>>>")
# if e_name[0] and ''.join(eng.split()).lower() == ''.join(e_name[1].split()).lower():
#     print("-------------+")

# import requests
# from urllib import parse
#
# url = 'https://so.youku.com/search_video/q_%E6%83%85%E9%99%B7%E5%A4%9C%E4%B8%AD%E7%8E%AF2?searchfrom=1'
# data = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "cache-control": "no-cache",
#     "cookie": "_uab_collina=161361364927426107739567; cna=VYYWGOpN5gkCAXL0JIK3YDxv; __ysuid=16136136493369K9; __ayft=1613613649343; __aysid=1613613649344kdU; __ayscnt=1; xlly_s=1; ctoken=hQRokx_V0xfOb57BjnG2PAbG; _m_h5_tk=91b084f01a2d48598a29403d0cc23609_1613618167025; _m_h5_tk_enc=1c08c66ff9f68499bbb5aaf7b51278d9; UM_distinctid=177b2ea6f0a18-0a0c404a0b4452-53e3566-144000-177b2ea6f0b6a8; P_sck=V7wU57eViOUGtaWmBkAvurEtyjsV%2Fgm8QPzr3yUw%2FXpq6RmwScwxLb6Sh5CKF2spCZxzt7LBFVyEhSUbkE1RUSz9k7odBvhxMdKHJ8Wz6NWOXIpCSfeFfB91W5pagsq79okpFvPVvpYGb0Vt%2FXL5OQ%3D%3D; P_gck=NA%7CeF5tR7nBrs3VLiRmZZVmZQ%3D%3D%7CNA%7C1613614955981; P_pck_rm=02aVb%2FmP36aff7942a70b8ZBickxjod81tOXwasSx25%2BmYvJiuvns5P2cMEbmVrTBsdHHSjDfrN1Q%2B3xWmo%2FG6npK3bVqnt%2BIrqoXxkcEpWZuJKM0uGK%2BD%2BKDBQieY0ZuEAVNM9GDnK4FQ0IjSnpsgKWbUR7GObr8mHoRQ%3D%3D%5FV2; youku_history_word=%5B%22%25E7%2594%25B5%25E8%25A7%2586%25E9%25A3%258E%25E4%25BA%2591%22%5D; P_ck_ctl=16F522CEFDDAA0A6BE2FEF392CE94B4B; __arpvid=1613617811232tp3ljJ-1613617811259; __aypstp=18; __ayspstp=18; isg=BAkJZq9qjZUNYk675KNcrSLQGDVjVv2I5Qe3xqt-AvAv8ikE86dqWPVqMFbErZXA; tfstk=cctlBANwmU7Sc3bD50sWQvZn0I3Oao0PNH-20nhRLkZ9A2RlUsDbuPWtgxfJZHUC.; l=eBSA5GF7Ov9olzPoBO5aFurza77tmIRb41PzaNbMiInca6sNtFMCBNCIAUDWSdtjgt1hpety-Z76RdLHR3fCOxDDBvRlN5Ftnxf..",
#     "referer": "https://www.youku.com/",
#     "pragma": "no-cache",
#     "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "none",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
# }
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
# }
# res = requests.get(url, headers=data)
# with open(file="ceshi124.html", mode="wb") as f:
#     f.write(res.content)
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(open("../result/红孩儿.html", encoding='UTF-8'), features="lxml")
# pre_verity = re.search("霸下通用客户端-验证码", str(soup))
#
# print(pre_verity)
# if pre_verity:
#     print("------")
# else:
#     print("==================")
# url = '电视风云'
# encodeurl = parse.quote(url)
# print(encodeurl)
from bs4 import BeautifulSoup

# def amain(name, year):
#     soup = BeautifulSoup(open("../temp/test.html", mode='r', encoding='utf-8'), features="lxml")
#     # print(soup.prettify()) # 格式化打印文本内容
#     items = soup.find_all(attrs={"type": "1027"})
#     # print(items)
#     if items:
#         for item in items:
#             print("-" * 50)
#             content = BeautifulSoup(str(item), features='lxml')
#             titleobj = content.find('mark', class_='temp-hight-title_1ISDT')
#             if titleobj:
#                 title = str(content.find('mark', class_='temp-hight-title_1ISDT').text)
#                 if title:
#                     if title == name:
#                         astr = str(content.find('div', class_='poster-desc_uTT1A').text)
#                         print("astr:", astr)
#                         verify_year = astr.split("·")[1].strip()
#                         print("year:", verify_year)
#                         if verify_year == year:
#                             print("success")
#                             return True
#                         print("failed")
#                     print("标题未匹配上")
#                 print("无合规内容")
#             print("未提供内容")
#     print("无匹配结果")
#     print("------------------------")
#     return False
#
#
# print(amain('电视风云', '2000'))

# astr = str(b'\xe6\x88\x91\xe5\x92\x8c\xe5\x83\xb5\xe5\xb0\xb8\xe6\x9c\x89\xe4\xb8\xaa\xe7\xba\xa6\xe4\xbc\x9a',encoding='utf-8')
# print(astr)

# import codecs
# title = r'\xe7\x94\xb5\xe8\xa7\x86\xe5\x89\xa7 \xc2\xb7 2000 \xc2\xb7 \xe4\xb8\xad\xe5\x9b\xbd\xe9\xa6\x99\xe6\xb8\xaf \xc2\xb7 30\xe9\x9b\x86\xe5\x85\xa8'.replace(" ",'')
# hexstring = title.replace(r'\x', '')
# real_title = codecs.decode(hexstring, "hex").decode('utf-8')
# print("real_title:", real_title)

# astr = str(r'\xe7\x94\xb5\xe8\xa7\x86\xe5\x89\xa7 \xc2\xb7 2000 \xc2\xb7 \xe4\xb8\xad\xe5\x9b\xbd\xe9\xa6\x99\xe6\xb8\xaf \xc2\xb7 30\xe9\x9b\x86\xe5\x85\xa8')
# print(astr.split(r'\xc2\xb7'))
import time

# browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=opt)


# 快手
# import requests
# from urllib import parse
# import urllib.request
# import urllib.parse
#
#
# def doubantest(name):
#     url = 'https://search.douban.com/movie/subject_search?search_text=%E6%96%97%E7%BD%97&amp;cat=1002'
#     # url = 'https://search.douban.com/movie/subject_search'
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#         "Cache-Control": "max-age=0",
#         "Connection": "keep-alive",
#         "Cookie": 'bid=5Tlfm0C3t5g; _pk_ref.100001.2939=%5B%22%22%2C%22%22%2C1613802918%2C%22https%3A%2F%2Fmovie.douban.com%2Fexplore%22%5D; _pk_ses.100001.2939=*; ll="108288"; __utmc=30149280; __utma=30149280.1549413386.1613802960.1613802960.1613802960.1; __utmz=30149280.1613802960.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="233581190:Y+kBgzIaWmE"; ck=8siy; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23358; _vwo_uuid_v2=D2813C9931BE7444E88AF888C012646D5|88f6e966d5c44c6a742643f8652c89fa; _pk_id.100001.2939=527ff31490b2bea8.1613802918.1.1613803735.1613802918.; __utmt=1; __utmb=30149280.6.10.1613802960; __yadk_uid=jbNsyHVl1kwV9jEawkufhrucc2zv3OMz',
#         "Host": "search.douban.com",
#         "Referer": "https: // movie.douban.com/",
#         "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
#         "sec-ch-ua-mobile": "?0",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "none",
#         "Sec-Fetch-User": "?1",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
#     }
#     params = {
#         "search_text": name,
#         "cat": 1002
#     }
#     response = urllib.request.urlopen(url=url)
#     # response = requests.get(url=url, params=params, headers=headers)
#     page_source = response.read()
#     # page_source = response.content
#     with open(file="%s.html" % name, mode="wb") as f:
#         f.write(page_source)
#
#
# if __name__ == '__main__':
#     name = "斗罗大陆"
#     doubantest(name)
