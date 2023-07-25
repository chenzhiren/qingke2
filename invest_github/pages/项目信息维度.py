import streamlit as st

import pymysql
import pandas as pd
import data_clean
import data_analyse
import numpy as np
st.set_page_config(
    layout='wide'
)
#取出最新一批次数据
data=pd.read_excel('data_clean2022.xlsx')
data = data.rename(columns={0: 'company_name', 1: 'base', 2: 'found_time', 3: 'field', 4: 'business', 5:'round', 6: 'currency',
      7: 'money', 8: 'investers', 9: 'financing_time', 10: 'create_time', 11: 'pici', 12: 'real_money',
      13:'fenceng',14:'in_out',15:'id'})


text_input=st.text_input('请输入公司名称，可查询该公司的详细信息')
if text_input:
      new_data=data[data['company_name']==text_input]
      new_data=new_data.drop_duplicates(subset=['company_name', 'round'], keep='last')
      new_data=new_data.drop(['create_time','pici','real_money','fenceng','in_out','id','business','base','field','found_time'],axis=1)
      st.subheader('公司融资事件')
      st.dataframe(new_data)

      result=data[data['company_name']==text_input]
      st.subheader('公司基本情况')
      st.write('公司名称：'+result['company_name'].values[0])
      st.write('公司成立日期：'+result['found_time'].values[0])
      st.write('行业：'+result['field'].values[0])
      st.write('主要业务：'+result['business'].values[0])