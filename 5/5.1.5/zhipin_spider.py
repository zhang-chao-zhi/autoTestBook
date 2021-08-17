# -*- coding: utf-8 -*-
'''
Boss直聘爬虫类

@author freePHP
@version 1.0.0
'''
import ssl
import requests
import random
from bs4 import BeautifulSoup
import browsercookie

import pandas as pd

# for cookie in chrome_cookie:
#     if '__zp_stoken_' in str(cookie):
#         tmp_cookie = str(cookie)
#         tmp_cookie = tmp_cookie.replace("<Cookie ", "")
#         tmp_cookie = tmp_cookie.replace(" for .zhipin.com/>", "")
class ZhipinSpider(object):
      def __init__(self):
          user_agent = self.get_random_user_agent()
          ssl._create_default_https_context = ssl._create_unverified_context
          self.url = 'https://www.zhipin.com/c101270100/y_6/?query=测试工程师&ka=sel-salary-6'
          self.headers = {
              'user-agent': user_agent,
              'cookie': self.get_cookie(),
              'referer': 'https://www.zhipin.com/c101270100/y_6/?query=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&ka=sel-salary-6'
          }

      def get_cookie(self) -> str:
          chrome_cookie = browsercookie.chrome()
          # 筛选出zhipin.com的有效cookie
          for cookie in chrome_cookie:
              if '__zp_stoken_' in str(cookie):
                  real_cookie = str(cookie)
                  real_cookie = real_cookie.replace("<Cookie ", "")
                  real_cookie = real_cookie.replace(" for .zhipin.com/>", "")
                  return real_cookie
          return ''

      def get_page_html(self):
          response = requests.get(self.url, headers=self.headers)
          return response.text



      def deal_html(self, html):
          soup = BeautifulSoup(html, "html.parser")
          data_list = []
          # 岗位名称， 月薪, 工作地点、公司名
          job_areas = soup.select('.job-area')

          new_job_areas = []

          for job in job_areas:
              new_job_areas.append(job.get_text())

          salary_ranges = soup.select('.job-limit > .red')
          # 每页三十条数据
          new_salary_ranges = []
          for salary in salary_ranges:
              new_salary_ranges.append(salary.get_text())

          company_names = []
          # 在循环中自己组织拼接tag
          for i in range (1, 31):
            search_list_tag = 'search_list_company_' + str(i) + '_custompage'
            item = soup.find('a', attrs={'ka': search_list_tag})
            company_names.append(item.get_text())

          item_num = len(job_areas)

          for index in range(item_num):
              tmp_row = {'job_name': '测试工程师', 'salary': new_salary_ranges[index], 'job_area': new_job_areas[index], 'company_name': company_names[index]}
              data_list.append(tmp_row)

          return data_list

      def data_to_table(self, data):
          # 使用pandas来组织数据
          df = pd.DataFrame(data)
          return df

      def data_to_execl(self, data):
          df = pd.DataFrame(data)
          df.to_csv('job.csv', mode='a', encoding='utf_8_sig')


      def get_random_user_agent(self):

          user_agents = [
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
          ]
          num = len(user_agents)

          random_num = random.randint(0, num -1)
          return user_agents[random_num]




if __name__ == '__main__':
    spider = ZhipinSpider()
    html = spider.get_page_html()
    data = spider.deal_html(html)
    spider.data_to_execl(data)
    #df_data = spider.data_to_table(data)
