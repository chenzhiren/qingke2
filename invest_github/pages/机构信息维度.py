import streamlit as st
import pymysql
import pandas as pd
from pyecharts import options as opts
import data_analyse
import numpy as np
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
st.set_page_config(
    layout='wide'
)
#取出最新一批次数据
data=pd.read_excel('data_clean2022.xlsx')
data = data.rename(columns={0: 'company_name', 1: 'base', 2: 'found_time', 3: 'field', 4: 'business', 5:'round', 6: 'currency',
      7: 'money', 8: 'investers', 9: 'financing_time', 10: 'create_time', 11: 'pici', 12: 'reaal_money',
      13:'fenceng',14:'in_out',15:'id'})
data_in=data[data['in_out']=='国内']
data_out=data[data['in_out']=='国外']

a1,a2=st.columns([1,2])
with a1:
     st.write('国内投资事件的投资机构列表')
     investers=data_analyse.investers(data_in)
     st.dataframe(investers)

with a2:
    st.write('国外投资事件的投资机构列表')
    investers = data_analyse.investers(data_out)
    st.dataframe(investers)


st.write('查询投资者投资的所有项目')
text_input=st.text_input('请输入投资者名称，并点击回车，即可查询该投资者投资的所有项目')
if text_input:
        ls=[]
        for i in range(len(data)):
            if text_input in data.iloc[i,8]:
                ls.append(data.iloc[i,0])
        ls=list(set(ls))
        new_data=data.drop_duplicates(subset=['company_name','round'],keep='last')
        new_data = new_data.set_index('company_name', inplace=False)
        result=new_data.loc[ls,['base','found_time','field','round','financing_time']]
        result=result.reset_index()
        st.dataframe(result)
        data_analyse.investers_field(result)
