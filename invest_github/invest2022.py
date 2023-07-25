import streamlit as st
import pandas as pd
import data_clean
import data_analyse
st.set_page_config(
    layout='wide'
)
data=pd.read_excel('data_clean2022.xlsx')
data = data.rename(columns={0: 'company_name', 1: 'base', 2: 'found_time', 3: 'field', 4: 'business', 5:'round', 6: 'currency',
      7: 'money', 8: 'investers', 9: 'financing_time', 10: 'create_time', 11: 'pici', 12: 'reaal_money',
      13:'fenceng',14:'in_out',15:'id'})
data_in=data[data['in_out']=='国内']
data_out=data[data['in_out']=='国外']

st.header('2022年清科投融资数据分析')
st.subheader('项目说明')
st.write('本项目数据来源：通过爬虫，获取清科集团旗下网站投资界的2022年一部分投资数据，具体网站投资界https://zdb.pedaily.cn/inv/')
st.write('经过数据清洗，整理和统计，将投资数据情况可视化呈现，用以反映投资趋势，投资的活跃程度等客观情况。')

col1,col2,col3=st.columns([2,0.5,2])
with col1:
    st.subheader('国内外投资事件数量')
    data_analyse.in_out_scale(data)
with col2:
    pass
with col3:
   st.subheader('部分投资事件展示')
   new_data = data[['company_name', 'field', 'investers']]
   st.dataframe(new_data.head(5))

a1,a2,a3=st.columns([2,0.5,2])
with a1:
    st.subheader('国内投资活跃度前五行业')
    data_analyse.topfive_industry(data_in)
with a2:
    pass
with a3:
    st.subheader('国外投资活跃度前五行业')
    data_analyse.topfive_industry2(data_out)

b1,b2,b3=st.columns([2,0.5,2])
with b1:
    st.subheader('国内活跃投资机构前10')
    data_analyse.top_investers(data_in)
with b2:
    pass
with b3:
    st.subheader('国外活跃投资机构前10')
    data_analyse.top_investers2(data_out)

