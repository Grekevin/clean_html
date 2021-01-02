# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os

# 获取当前工作目录路径
cwd_path = os.path.dirname(__file__)

# 输入文件(清洗的数据)
IN_FILE_NAME = 'in.txt'

# 输出文件
OUT_FILE_NAME = 'out.txt'

# 输入文件路径
in_file_path = os.path.join(cwd_path, IN_FILE_NAME)

# 输出文件路径
out_file_path = os.path.join(cwd_path, OUT_FILE_NAME)

with open(in_file_path, 'r', encoding='utf-8') as f:
    # 解析文件
    soup = BeautifulSoup(f, 'lxml')

    # 找出要删除的标签，比如meta
    # tags_delete = soup.find_all('meta')

    # for tag in tags_delete:
        # 循环遍历，从文档树种删除标签
        # tag.extract()
    
    # 把删除标签的文档格式化输出到文件out.txt中
    with open(out_file_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())