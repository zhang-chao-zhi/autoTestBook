# coding:utf-8
import yaml

file_path = './test.yaml'

with open(file_path, 'rb') as f:
    data = yaml.load(f)

    print(data)
