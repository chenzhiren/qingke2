import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from streamlit_echarts import st_pyecharts

# 金额分层
def fen_ceng(data):
    data['fenceng'] = 1
    for i in range(data.shape[0]):
        if type(data.iloc[i, 13]) == type(1.1):
            data.iloc[i, 14] = '有具体数据'
        if type(data.iloc[i, 13]) == type('abc'):
            data.iloc[i, 14] = '文字数据'
        if data.iloc[i, 13] ==1:
            data.iloc[i, 14] = '无数据'
    return data


# 去除括号方法
def one(w):
    if '[]' in w:
        w = w.replace('[]', '')
    else:
        w = w.replace("['", '').replace("']", '')
    return w


# 去除数据的括号
def clean_1(data):
    data['business'] = data['business'].apply(one)
    data['round'] = data['round'].apply(one)
    data['currency'] = data['currency'].apply(one)
    data['money'] = data['money'].apply(one)
    data['investers'] = data['investers'].apply(one)
    return data


# 区分国内外项目
def in_out(data):
    import re
    data['in_out'] = 1
    for i in range(len(data)):
        a = data.iloc[i, 1]
        b = re.findall('[a-zA-Z]', a)
        if len(b) != 0:
            c = re.findall('[\u4e00-\u9fa5]', a)
            if len(c) == 0:
                data.iloc[i, 15] = '国外'
            else:
                data.iloc[i,15]='国内'
        else:
            data.iloc[i, 15] = '国内'
    return data


# 前20投资者
def top_investers(data):
    import pandas as pd
    ls = data['investers'].to_list()
    new_ls = []
    for i in ls:
        if ',' in i:
            i = i.split(',')
            for x in i:
                x = x.replace("'", '').strip()
                new_ls.append(x)
        else:
            i = i.strip()
            new_ls.append(i)
    s1 = pd.Series(new_ls, index=[None for i in range(len(new_ls))]).value_counts()
    if '不公开的投资者' in s1.index:
        s1 = s1.drop('不公开的投资者')
        if '' in s1.index:
            s1 = s1.drop('').head(20)
        else:
            s1 = s1.head(20)
    s2 = pd.DataFrame(s1).reset_index().rename(columns={'index': '投资者', 0: '投资次数'})
    return s2



def invester_data(data, invester_top):
    l = invester_top['投资者'].to_list()
    ls = []
    for i in l:
        for x in range(len(data)):
            a = data.iloc[x, 8]
            if i in a:
                ls.append(x)
    ls = sorted(list(set(ls)))
    data = data.iloc[ls, :]
    return data

























