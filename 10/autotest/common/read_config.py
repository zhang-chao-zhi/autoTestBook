# *_*coding:utf-8 *_*
__author__ = "freephp"
import os,codecs
import configparser
prodir = os.path.dirname(os.path.abspath(__file__))
conf_prodir = os.path.join(prodir,'conf.ini')
class Read_Config():
     def __init__(self):
         with open(conf_prodir) as fd:
             data = fd.read()
             #清空文件信息
             if data[:3] ==codecs.BOM_UTF8:
                 data = data[3:]
                 file = codecs.open(conf_prodir,'w')
                 file.write(data)
                 file.close()
         self.cf = configparser.ConfigParser()
         self.cf.read(conf_prodir)
     def  get_http(self,name):
         value = self.cf.get("HTTP",name)
         return value

     def get_db(self,name):
         return self.cf.get("DATABASE",name)