清洗HTML源文件
=============

使用的库文件
-------------

1. Beautiful Soup

2. os

3. re

参考文档: https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

目的
---

1. 删除不需要的标签

2. 格式化输出HTML源文件

文档说明
--------

1. clean_html.py文档会把父标签及其字标签一起删掉，无论字标签是不是要删除的标签。

2. re_clean_html.py文档只会删除要删除的标签，如父标签要删除，子标签要保留，只会删除父标签留下字标签。