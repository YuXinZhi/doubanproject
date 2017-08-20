'''
name : //h1/span[@property="v:itemreviewed"  
year : //h1/span[@class="year"]   (2017)    year.lstrip('(').rstrip(')')
type : //div[@id="info"]/span[@property="v:genre"]
time ：//div[@id="info"]/span[@property="v:runtime"]   123分钟 
area ：//div[@id="info"]//span[@class="pl"][2]

待考虑情况：
片长: 137分钟 / 140分钟(加长版)

待解决：
<span class="pl">又名:</span> 解氷 / 化冰 / Bluebeard<br>


'''

'''
序号	电影名称	别名	类型	年份	片长	成品完成时间	压片人员	编辑人员	分辨率
'''




import requests
from lxml import etree
import re
import xlwt
import time

def gen_xls_from_urls(urls=None,work_name='于孟孟',editor_name = '编辑',resolution =1080,program_type = '电影'):
    '''

    :param urls:        节目的链接列表
    :param work_name:   压片人
    :param editor_name: 编辑
    :param resolution:  默认分辨率
    :param program_type:节目类型
    :return:
    '''
    # 表格的标题
    title = ['序号', '电影名称', '别名', '类型', '年份', '片长', '成品完成时间', '压片人员', '编辑人员', '分辨率']

    program_type = program_type

    # 创建Excel文件
    xls = xlwt.Workbook()
    sheet = xls.add_sheet(program_type)

    # 第一行写标题
    column = -1
    for t in title:
        column += 1
        sheet.write(0, column, t)

    # 电影成品部数
    total = len(urls)

    # 起始行列数
    row = 0
    # 当前正处理的电影数
    count = 0
    for url in urls:
        column = -1
        info = []
        response = requests.get(url)
        html = response.text  # html type is string
        page = etree.HTML(html.encode('utf-8'))

        #print(html)

        # 根据url获取节目信息
        # 电影名
        name = page.xpath('//h1/span[@property="v:itemreviewed"]/text()')[0].split(' ')[0]
        # 年份
        year = page.xpath('//h1/span[@class="year"]/text()')[0].lstrip('(').rstrip(')')
        typelist = page.xpath('//div[@id="info"]/span[@property="v:genre"]/text()')
        # 类型列表字符串
        type = '/'.join(typelist)
        # 时长
        '''
        106分钟(台湾)
        '''
        duration = page.xpath('//div[@id="info"]/span[@property="v:runtime"]/text()')[0].rstrip('分钟')
        # 别名
        alternatenames = re.findall('<span class="pl">又名:</span>(.*?)<br/>', html)
        if alternatenames :
            alternatename = alternatenames[0].strip(' ')
        else:
            alternatename = ' '
        #alternatename = re.findall('<span class="pl">又名:</span>(.*?)<br/>', html)[0]

        info.append(name)
        info.append(alternatename)
        info.append(type)
        info.append(year)
        info.append(duration)

        row += 1
        column += 1
        count += 1
        # 序号
        sheet.write(row, column, count)
        for i in info:
            column += 1
            sheet.write(row, column, i)

    today_time = time.strftime('%Y%m%d', time.localtime())

    editor_info = [today_time, work_name, editor_name, resolution]

    # 其他信息起始列
    start_column = 6
    for i in range(1, total + 1):
        column = start_column
        for e in editor_info:
            sheet.write(i, column, e)
            column += 1

    xls.save(today_time + work_name + '（' + program_type + str(total) + '）' + '.xls')


def gen_xls_from_file(file):
    f = open(file, 'r')
    urls = []
    for line in f:
        #line.rstrip('\n').strip(' ')
        print(line)
        urls.append(line)
    print(len(urls))
    gen_xls_from_urls(urls=urls)

if __name__ == '__main__':
    #成品的豆瓣链接
    urls = ['https://movie.douban.com/subject/27041519/',
            'https://movie.douban.com/subject/27085694/',
            'https://movie.douban.com/subject/1307853/',
            'https://movie.douban.com/subject/1905788/',
            'https://movie.douban.com/subject/26678594/',
            'https://movie.douban.com/subject/27065621/',
            'https://movie.douban.com/subject/26279202/',
            'https://movie.douban.com/subject/1298497/',
            'https://movie.douban.com/subject/26843838/',
            'https://movie.douban.com/subject/2122766/',
            'https://movie.douban.com/subject/1308146/',
            'https://movie.douban.com/subject/26627705/',
            'https://movie.douban.com/subject/25884801/',
            'https://movie.douban.com/subject/26574949/',
            'https://movie.douban.com/subject/26751902/',
            'https://movie.douban.com/subject/26754831/',
            'https://movie.douban.com/subject/26412618/',
            'https://movie.douban.com/subject/1297511/',
            'https://movie.douban.com/subject/1302191/',
            'https://movie.douban.com/subject/1292060/',
            'https://movie.douban.com/subject/26667056/',
            'https://movie.douban.com/subject/1291845/',
            'https://movie.douban.com/subject/1950192/',
            'https://movie.douban.com/subject/1304045/',
            'https://movie.douban.com/subject/1947729/',
            'https://movie.douban.com/subject/26646360/',
            'https://movie.douban.com/subject/1301629/',
            'https://movie.douban.com/subject/26995137/',
            'https://movie.douban.com/subject/1361276/'            
            ]

    gen_xls_from_urls(urls=urls)
    #gen_xls_from_file(r'D:\genxls\douban.txt')