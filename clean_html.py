# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os

"""
根据输入的标签名，删除源文件中所有的标签
无法处理嵌套标签的问题
"""

# 处理类
class ProcessHtml(object):
    def __init__(self, in_file, out_file, del_tags):
        super().__init__()
        self.in_file = in_file
        self.out_file = out_file
        self.del_tags = del_tags
        self.soup = None

    def open_file(self):
        """
        打开文件，使用bs4库进行解析
        """        
        # 输入的文件路径
        in_file_path = os.path.join(os.path.dirname(__file__), self.in_file)

        # 打开文件并解析文件
        with open(in_file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml')
            self.soup = soup

    def del_tag(self, tag_name):
        find_tags = self.soup.find_all(tag_name)

        # 循环遍历，从文档树种删除标签
        for tag in find_tags:
            tag.extract()
    
    # 处理解析后的文件
    def clean_process(self):
        """
        根据标签名称，删除标签
        """        
        for tag_name in self.del_tags:
            self.del_tag(tag_name)


    # 输出文件
    def save_file(self):

        # 输出的文件路径
        out_file_path = os.path.join(os.path.dirname(__file__), self.out_file)

        # 把删除标签后的文档格式化输出到文件out.txt中
        with open(out_file_path, 'w', encoding='utf-8') as f:
            f.write(self.soup.prettify())

    # 运行
    def run(self):
        # 打开文件
        self.open_file()

        # 处理文件
        self.clean_process()

        # 输出文件
        self.save_file()

def main():
    tag_str = input("请输入你要删除的标签，多个标签之间用空格分隔：")
    del_tags = tag_str.split()

    # 输入文件(清洗的数据)
    in_file = 'in.txt'

    # 输出文件
    out_file = 'out.txt'

    process_html = ProcessHtml(in_file, out_file, del_tags)
    process_html.run()

if __name__ == "__main__":
    main()