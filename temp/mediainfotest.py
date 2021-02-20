#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import os
import pymysql
import requests
import json
import xlwt, re

'''
封装查询单条、多条数据
'''
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
pdbinfo = {"host": '172.16.112.26',
           "port": 3306,
           "user": 'root',
           "passwd": 'wangfan123',
           "db": '03eam',
           "charset": 'utf8'}


class MySQLUtil:
    def __init__(self):
        self.dbinfo = pdbinfo
        self.conn = MySQLUtil.__getConnect(self.dbinfo)
        self.info_list = []
        self.dict_all = {}
        self.f_fail = open('/opt/提取失败日志.log', 'a', encoding='utf-8')

    @staticmethod
    def __getConnect(pdbinfo):
        try:
            conn = pymysql.connect(host=pdbinfo['host'], port=pdbinfo['port'], user=pdbinfo['user'],
                                   passwd=pdbinfo['passwd'],
                                   db=pdbinfo['db'], charset=pdbinfo['charset'])
            return conn
        except Exception as error:
            print("get connect happen error %s " % error)

    def close_db(self):
        try:
            self.conn.close()
        except Exception as error:
            print("close db happen error %s " % error)

    def get_alldata(self, psql):
        cur = self.conn.cursor()
        try:
            cur.execute(psql)
        except Exception as error:
            print("execute sql happen error %s " % error)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def get_singledata(self, psql):
        rows = self.get_alldata(psql)
        row_len = len(rows)
        print(row_len)

        if rows != None:
            for row in rows:
                for i in row:
                    print(i)
                    return i

    def get_first(self, param):
        if param:
            return param[0]
        else:
            return ''

    # 定义个方法传递字典数据,返回自己想要的字段数据,返回值列表
    def get_dict_data(self, json_data):
        # 文件的
        # 获取文件大小
        filesize = re.findall(r'<File_size>(.*?)</File_size>', json_data)
        filesize = self.get_first(filesize)
        # 总体码率
        malv = re.findall(r'<Overall_bit_rate>(.*?)</Overall_bit_rate>', json_data)
        malv = self.get_first(malv)
        # 时长
        duration = re.findall(r'<Duration>(.*?)</Duration>', json_data)
        duration = self.get_first(duration)
        # 文件格式
        file_format = re.findall(r'<Format>(.*?)</Format>', json_data)
        file_format = self.get_first(file_format)
        # 获取帧宽
        samp_width = re.findall(r'<Width>(.*?)</Width>', json_data)
        samp_width = self.get_first(samp_width)
        # 获取帧高
        samp_height = re.findall(r'<Height>(.*?)</Height>', json_data)
        samp_height = self.get_first(samp_height)
        # 码率模式
        bitRateMode = re.findall(r'<Overall_bit_rate_mode>(.*?)</Overall_bit_rate_mode>', json_data)
        bitRateMode = self.get_first(bitRateMode)
        # 帧率
        frameRate = re.findall(r'<Frame_rate>(.*?)</Frame_rate>', json_data)
        frameRate = self.get_first(frameRate)

        # video 匹配
        videos = re.compile('<track type=\"Video\">(.*?)</track>', re.S).findall(json_data)[0]
        # print(videos[0])

        # 视频格式
        video_format = re.compile('<Format>(.*?)</Format>').findall(videos)
        video_format = self.get_first(video_format)
        # 宽度
        video_width = re.compile('<Width>(.*?)</Width>').findall(videos)
        video_width = self.get_first(video_width)
        # 高度
        video_height = re.compile('<Height>(.*?)</Height>').findall(videos)
        video_height = self.get_first(video_height)
        # 位深
        video_bit_depth = re.compile('<Bit_depth>(.*?)</Bit_depth>').findall(videos)
        video_bit_depth = self.get_first(video_bit_depth)
        # 视频码率
        video_bit_rate = re.compile('<Bit_rate>(.*?)</Bit_rate>').findall(videos)
        video_bit_rate = self.get_first(video_bit_rate)
        # 扫描方式
        video_scan_type = re.compile('<Scan_type>(.*?)</Scan_type>').findall(videos)
        video_scan_type = self.get_first(video_scan_type)
        # 如果文件的码率模式为空则取视频的码率模式
        # 成品介质-码率

        # audio 匹配
        audios = re.compile('<track type=\"Audio\">(.*?)</track>', re.S).findall(json_data)[0]
        # print(audios)
        # 音频格式
        audio_format = re.compile('<Format>(.*?)</Format>', re.S).findall(audios)
        audio_format = self.get_first(audio_format)
        # 音频format_profile根据这个来判断是MP2还是MP3，如果profile为空则取format的值
        audio_profile = re.compile('<Format_profile>(.*?)</Format_profile>', re.S).findall(audios)
        audio_profile = self.get_first(audio_profile)
        if audio_profile == "Layer 2":
            audio_profile = "MP2"
        if audio_profile == "Layer 3":
            audio_profile = "MP3"
        # 采样率
        audio_sampling_rate = re.compile('<Sampling_rate>(.*?)</Sampling_rate>', re.S).findall(audios)
        audio_sampling_rate = self.get_first(audio_sampling_rate)
        # 音频码率
        audio_bit_rate = re.compile('<Bit_rate>(.*?)</Bit_rate>', re.S).findall(audios)
        audio_bit_rate = self.get_first(audio_bit_rate)

        return [filesize, malv, duration, file_format, samp_width, samp_height, bitRateMode, frameRate,
                video_format, video_width, video_height, video_bit_depth, video_bit_rate, video_scan_type,
                audio_format, audio_profile, audio_sampling_rate, audio_bit_rate]

    def record(self):
        # 创建一个excel表存放文件路径信息，第一列是目录，第二列是文件名
        wb = xlwt.Workbook()
        sh = wb.add_sheet('元数据')
        # 写第一行
        row_count = 0
        sh.write(row_count, 0, "文件名")
        sh.write(row_count, 1, "文件大小")
        sh.write(row_count, 2, "码率")
        sh.write(row_count, 3, "总时长")
        sh.write(row_count, 4, "视频格式")
        sh.write(row_count, 5, "帧宽")
        sh.write(row_count, 6, "帧高")
        sh.write(row_count, 7, "码率模式")
        sh.write(row_count, 8, "帧率")
        sh.write(row_count, 9, "视频格式")
        sh.write(row_count, 10, "宽度")
        sh.write(row_count, 11, "高度")
        sh.write(row_count, 12, "位深")
        sh.write(row_count, 13, "视频码率")
        sh.write(row_count, 14, "扫描方式")
        sh.write(row_count, 15, "音频格式")
        sh.write(row_count, 16, "类型")
        sh.write(row_count, 17, "采样率")
        sh.write(row_count, 18, "音频码率")
        # 批量写入视频信息
        row_count = 1
        for item in self.dict_all:
            sh.write(row_count, 0, item)
            sh.write(row_count, 1, self.dict_all[item][0])
            sh.write(row_count, 2, self.dict_all[item][1])
            sh.write(row_count, 3, self.dict_all[item][2])
            sh.write(row_count, 4, self.dict_all[item][3])
            sh.write(row_count, 5, self.dict_all[item][4])
            sh.write(row_count, 6, self.dict_all[item][5])
            sh.write(row_count, 7, self.dict_all[item][6])
            sh.write(row_count, 8, self.dict_all[item][7])
            sh.write(row_count, 9, self.dict_all[item][8])
            sh.write(row_count, 10, self.dict_all[item][9])
            sh.write(row_count, 11, self.dict_all[item][10])
            sh.write(row_count, 12, self.dict_all[item][11])
            sh.write(row_count, 13, self.dict_all[item][12])
            sh.write(row_count, 14, self.dict_all[item][13])
            sh.write(row_count, 15, self.dict_all[item][14])
            sh.write(row_count, 16, self.dict_all[item][15])
            sh.write(row_count, 17, self.dict_all[item][16])
            sh.write(row_count, 18, self.dict_all[item][17])
            row_count += 1

        wb.save("元数据统计.xls")

    def action(self):
        selectSql = "select dfile from ftpln_file_movelink order by id desc limit 200"
        rows = self.get_alldata(selectSql)
        for i in rows:
            # print("----------------------------")
            url = "http://118.186.213.226:8888/api/mediainfo/master"
            file_name = "/vol" + i[0]
            data = {
                "file_name": file_name
            }
            result = requests.post(url=url, data=json.dumps(data))
            res = json.loads(result.content)
            try:
                info_list = self.get_dict_data(res['file_info'])
                self.dict_all[i] = info_list

            except Exception as e:
                print(i, '------提取此文件信息失败---------')
                print("报错：", e)
                self.f_fail.write(file_name + '\r\n' + str(res) + '\r\n')

            finally:
                MySQLUtil().close_db()
        self.f_fail.close()
        self.record()


if __name__ == '__main__':
    print("==========================")
    conn = MySQLUtil().action()
    print("]]]]]]]]]]]]]]]]]]]]]]]]]")

    print("执行完成")
