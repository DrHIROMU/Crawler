# 如果先前沒安裝過requests 套件則這邊會失敗, 因此需要先安裝, 可用這個指令: pip install requests
import requests
import re
from bs4 import BeautifulSoup
import sqlite3
import datetime
import mariadb
import sys
try:
    conn = mariadb.connect(
        user="root",
        password="123456",
        host="127.0.0.1",
        port=3306,
        database="stock"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

company_ids = ['2330', '2454']

# 指定要抓取的網頁URL
# url = "https://www.ptt.cc/bbs/hotboards.html"
for company_id in company_ids:
    url = "https://mops.twse.com.tw/mops/web/ajax_t05st03?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&inpuType=co_id&TYPEK=all&co_id="+company_id
    
    # 使用requests.get() 來得到網頁回傳內容
    # response = requests.get(url,verify=False)


    payload = {}

    response = requests.post(url, json = payload)

    
    # request.get()回傳的是一個物件 
    # 若抓成功(即r.status_code==200), 則網頁原始碼會放在物件的text屬性, 我們把它存在一個變數 'web_content'
    web_content = response.text
    
    # 可以印出來看看, 會跟從網頁右鍵查看原始碼看到的一樣
    # print(web_content) 



    # 以 Beautiful Soup 解析 HTML 程式碼 : 
    soup = BeautifulSoup(web_content, 'html.parser')

    # 找出所有class為"board-name"的div elements
    # boardNameElements = soup.find_all('th', text = re.compile('實收資本額'))

    cols = ['公司名稱','股票代號','實收資本額']

    for col in cols:
        capital = soup.find('th', text = re.compile(col))
        print(col)
        th_tag = capital.parent
        next_td_tag = th_tag.findNext('td')
        print(next_td_tag.contents[0].strip().replace('元','')+'\n')


    # print(nextSiblings)

    # boardNames = [e.text for e in boardNameElements]

    # popularityElements = soup.find_all('div', class_="board-nuser")
    # popularities = [int(e.text) for e in popularityElements]

    # for pop, bn in zip(popularities, boardNames):
    #     print(pop, bn)

    # conn = sqlite3.connect("test.db")
    
    # 後面都用這個 cursor來做SQL操作.
    # c = conn.cursor()

    # c.execute('''
    # CREATE TABLE records
    #  (boardnames text,
    #   popularity int,
    #   timestamp datetime)
    # ''')

    # now_dt = datetime.datetime.now()

    # c.execute('DELETE FROM records')
    
    # for bn, pop in zip(boardNames, popularities):
    #     c.execute('INSERT INTO records VALUES (?,?,?)', (bn, pop, now_dt))
    
    # 將指令送出, 確保前述所有操作已生效
    # conn.commit()

    # print(c.execute("select * from records;").fetchall())



    print("==============================================================================")
