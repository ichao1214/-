# -*- coding: utf-8 -*-

# 以下几种情况会导致转化成 CSV 后导入 weka 失败
# 1.查询字符串中存在引号“”  -想办法去掉查询字符串中的引号
# 2.URL中存在分割符号，导致不该分割的地方分割了 -正则分组 []'' "" 和普通查询字符串

import codecs
import re

with codecs.open('SogouQ.sample', 'r', 'gbk') as f:
    with codecs.open('new.txt', 'w', 'gbk') as n:
        for line in f:
            s = line.split()[2]    # 要修改，应该部分查询字符串和URL中存在空格
            print s
            m = re.match(r'([\[\'\"]*)(.*)([\"\'\]]+)', s)
            print m.group(2)

            # fenge_str = '#?#?*'
            # context = fenge_str.join(s) + '\n'
            # print(context)
            #n.write(m.group(2))

