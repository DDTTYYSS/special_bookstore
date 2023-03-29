import streamlit as st
import requests

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if name not in county:
            continue
        else:
            specificBookstoreList.append(item)
    return specificBookstoreList
        
            

    # 如果 name 不是我們選取的 county 則跳過
    # hint: 用 if-else 判斷並用 continue 跳過

    # districts 是一個 list 結構，判斷 list 每個值是否出現在 name 之中
    # 判斷該項目是否已經出現在 specificBookstoreList 之中，沒有則放入
    # hint: 用 for-loop 進行迭代，用 if-else 判斷，用 append 放入
    return specificBookstoreList

def getCountyOption(items):
    optionList=[]# 創建一個空的 List 並命名為 optionList
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList
        # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
        # hint: 想辦法處理 item['cityName'] 的內容

        # 如果 name 不在 optionList 之中，便把它放入 optionList
        # hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
        

def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res


def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write('Intro')
        # 用 st.write 呈現書店的 Introduction
        expander.subheader('Address')
        expander.write('address')
        # 用 st.write 呈現書店的 Address
        expander.subheader('Open Time')
        expander.write('Opentime')
        # 用 st.write 呈現書店的 Open Time
        expander.subheader('Email')
        expander.write('Email')
        # 用 st.write 呈現書店的 Email
        expanderList.append(expander)
        # 將該 expander 放到 expanderList 中
    return expanderList


def app():
    bookstoreList=getAllBookstore()

    countyOption=getCountyOption(bookstoreList)

    

    st.header('特色書店地圖')
    st.metric('Total bookstore', 118)
    county = st.selectbox('請選擇縣市', countyOption)

    specificBookstore = getSpecificBookstore(bookstoreList, county)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果')
    bookstoreInfo=getBookstoreInfo(specificBookstore)

    #district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

    app()
    
