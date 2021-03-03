# -*- coding: utf-8 -*-


"""
李运辰 2021-3-3

公众号：python爬虫数据分析挖掘
"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',}

#r = requests.get(url, headers=headers)


import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('sheet1')

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(0,0, label='uid')
worksheet.write(0,1, label='content')
worksheet.write(0,2, label='likeCount')


import zlib
import requests

"""
# 1.爬取xml文件
def download_xml(url):
    bulletold = requests.get(url).content  # 二进制内容
    return zipdecode(bulletold)

def zipdecode(bulletold):
    '对zip压缩的二进制内容解码成文本'
    decode = zlib.decompress(bytearray(bulletold), 15 + 32).decode('utf-8')
    return decode

for x in range(1,11):
    # x是从1到11，11怎么来的，这一集总共46分钟，爱奇艺每5分钟会加载新的弹幕,46除以5向上取整
    #https://cmts.iqiyi.com/bullet/54/00/7973227714515400_60_19_87ad0a0d.br
    url = 'https://cmts.iqiyi.com/bullet/54/00/7973227714515400_300_' + str(x) + '.z'
    xml = download_xml(url)
    # 把编码好的文件分别写入个xml文件中（类似于txt文件），方便后边取数据
    with open('./lyc/zx' + str(x) + '.xml', 'a+', encoding='utf-8') as f:
        f.write(xml)

"""
count = 1
# 2.读取xml文件中的弹幕数据数据
from xml.dom.minidom import parse
import xml.dom.minidom
def xml_parse(file_name):
    global  count
    DOMTree = xml.dom.minidom.parse(file_name)
    collection = DOMTree.documentElement
    # 在集合中获取所有entry数据
    entrys = collection.getElementsByTagName("entry")
    print(entrys)
    result = []



    for entry in entrys:
        uid = entry.getElementsByTagName('uid')[0]
        content = entry.getElementsByTagName('content')[0]
        likeCount = entry.getElementsByTagName('likeCount')[0]
        print(uid.childNodes[0].data)
        print(content.childNodes[0].data)
        print(likeCount.childNodes[0].data)
        # 写入excel
        # 参数对应 行, 列, 值
        worksheet.write(count, 0, label=str(uid.childNodes[0].data))
        worksheet.write(count, 1, label=str(content.childNodes[0].data))
        worksheet.write(count, 2, label=str(likeCount.childNodes[0].data))
        count=count+1
        i = content.childNodes[0].data
        result.append(i)
    return result



for x in range(1,11):
    l = xml_parse("./lyc/zx" + str(x) + ".xml")

# 保存
workbook.save('弹幕数据集-李运辰.xls')