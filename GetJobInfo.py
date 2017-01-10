#!/usr/bin/python

from urllib import request  # 发送post请求
from bs4 import BeautifulSoup  # html格式数据
import time
import XLSWrite


class GetJobInfo:
    def __init__(self):
        # 以下内容不需要修改
        self.url = 'http://scc.whut.edu.cn/vjlist.aspx?type=zph&vj&page='
        self.root_url = 'http://scc.whut.edu.cn/'
        self.pagenum = 1
        # 构造header
        self.headers = {
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0/ROY TOOL',
            'Referer': self.root_url}
        self.times = []
        self.places = []
        self.company = []
        self.details = []

    def write_info(self):
        xls = XLSWrite.XLSWrite()
        xls.newSheet('Sheet1')
        xls.write(0, 0, '时间')
        xls.write(0, 1, '地点')
        xls.write(0, 2, '公司')
        xls.write(0, 3, '详情')
        row = 1
        for i in self.times:
            xls.write(row, 0, i)
            row += 1
        row = 1
        for i in self.places:
            xls.write(row, 1, i)
            row += 1
        row = 1
        for i in self.company:
            xls.write(row, 2, i)
            row += 1
        row = 1
        for i in self.details:
            xls.write(row, 3, self.root_url + i)
            row += 1
        xls.save(u'D:/info.xls')

    def get_job_info(self):
        while 1:
            try:
                time_now = time.strptime(time.strftime('%Y-%m-%d %H:%M', time.localtime()), '%Y-%m-%d %H:%M')
                req = request.Request(url=(self.url + str(self.pagenum)), headers=self.headers)
                res = request.urlopen(req).read().decode('utf8')
                # You can replace 'lxml' with 'html.parser', and 'html.parser' doesnot need to install
                soup = BeautifulSoup(res, 'lxml')
                lis = soup.find('ul', class_='zl14').find_all('li')
                for li in lis:
                    items = li.find_all('span')
                    time_info = items[0].text.strip()
                    place_info = items[1].text.strip()
                    detail_info = li.find('a').get('href')
                    company_info = li.find('a').text.strip()
                    time_job = time.strptime(time_info, '%Y-%m-%d %H:%M')
                    if time_job >= time_now:
                        self.times.append(time_info)
                        self.places.append(place_info)
                        self.company.append(company_info)
                        self.details.append(detail_info)
                        print('时间：%s 地点：%s 公司：%s' % (time_info, place_info, company_info))
                    else:
                        return
                self.pagenum += 1
            except:
                time.sleep(10)
                continue


job = GetJobInfo()
job.get_job_info()
job.write_info()
print('[DONE]')
