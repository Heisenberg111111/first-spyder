# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:14:55 2022

@author: wsy-1
"""

#引入requests库和BeautifulSoup库
import requests
from bs4 import BeautifulSoup

#目标网址
url="https://www.shanghairanking.cn/rankings/bcur/201611"
r=requests.get(url)


#改变编码方式
#print(r.encoding)
r.encoding = r.apparent_encoding

#用BeautifulSoup库煲汤
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
#print(soup.prettify)



#所有信息都在td标签中
re = soup.find_all('td')
print(re)
# #将所以信息汇集到ulist列表中
# ulist=[]

# #选择学校数量
# num= 20
# for i in range(1,num+1):
#     for e in range((i-1)*6,(i)*6):
#         if re[e].string!=None:
#             #tag.string获得字符串
#             ulist.append(re[e].string)
            
#         else:
#             #tag.text获得汉字
#             ulist.append(re[e].text)

# #去掉列表中的空字符
# u=[]
# for i in ulist:
#     u.append(i.strip())
    
# for i in range(1,num+1):
#     print("{}\t{}\t{}\t{}\t{}\t{}".format(u[i*6-6],u[i*6-5],u[i*6-4],u[i*6-3],u[i*6-2],u[i*6-1]))

