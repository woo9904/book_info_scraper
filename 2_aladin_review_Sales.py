from email import header
from itsdangerous import exc
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
#from configparser import ConfigParser

#알라딘에서 평점과 sales point만 가져오는 코드임. 

#----------------------------------------------------------------------
#준비단계
#사람임을 나타냄 / 기본 url 주소 가져옴
headers={""} #add your user-agent
url="https://search.kyobobook.co.kr/web/search?vPstrKeyWord="

#책 목록들 파일 읽기
with open("2020_text_list.txt", encoding='utf-8') as f: #txt파일에 책 목록들 저장
    lines=f.readlines()
#책 이름들을 리스트로 저장
lines=[line.rstrip('\n').split("-")[0].rstrip() for line in lines]

#책 작가들 파일 읽기
with open("작가.txt", encoding='utf-8') as f: #txt파일에 작가들 저장
    authors=f.readlines()
#작가들을 리스트로 저장
authors=[author.rstrip('\n').split("외")[0].rstrip() for author in authors]

#출판사들 파일 읽기
with open("출판사.txt", encoding='utf-8') as f: #txt파일에 출판사들 저장
    publishers=f.readlines()
#작가들을 리스트로 저장
publishers=[publisher.rstrip('\n') for publisher in publishers]

#데이터프레임 틀
df=[]

#----------------------------------------------------------------------
#함수
def kobo_search(book_name):
    global lines, headers, df
    url="https://search.kyobobook.co.kr/web/search?vPstrKeyWord="
    url=url+book_name

    url=url.replace(" ", "%20") #교보문고에서는 링크 생성 방식이 다음과 같음

    #서버 접속
    res=requests.get(url, headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")


    for href in soup.find("tbody", attrs={"id":"search_list"}).find_all("tr"):
        #test_=href.find("div", attrs={"class":"title"})
        #print(test_)
        book=[]
        another_link=href.find("a")["href"] #ISBN 링크 가져오기
        book_writer=href.find("div", attrs={"class":"author"}).get_text().split("|")[0].strip().replace(" 지음","") #작가 가져오기
        book_pub=href.find("div", attrs={"class":"author"}).get_text().split("|")[-2].strip() #출판사 가져오기
        book_year=href.find("div", attrs={"class":"author"}).get_text().split("|")[-1].strip() #출판연도 가져오기
        book_price=href.find("div", attrs={"class":"org_price"}).get_text().strip() #정가 가져오기
        #print(another_link)

        #ISBN 링크 이동, ISBN 가져오기
        res=requests.get(another_link, headers=headers)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, "lxml")
        book_ISBN=soup.find("span", attrs={"title":"ISBN-13"}).get_text()
        #데이터 프레임 리스트 만들기 (ROW)
        book=[book_name, book_writer, book_pub, book_year, book_ISBN, book_price.replace("원","")]
        df.append(book)
        print(book_name+"----완료----")
        break


def aladin_search(book_name):
    global lines, headers, df

    url="https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord="+book_name
    url=url.replace(" ", "+") #알라딘에서는 링크 생성 방식이 다음과 같음
    res=requests.get(url, headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")

    for href in soup.find("div", attrs={"id":"Search3_Result"}).find_all("div"):
        #test_=href.find("div", attrs={"class":"title"})
        #print(test_)
        book=[]
        another_link=href.find("a")["href"] #ISBN 링크 가져오기

        #ISBN 링크 이동, ISBN 가져오기
        res=requests.get(another_link, headers=headers)
        res.raise_for_status()
        soup=BeautifulSoup(res.text, "lxml")

        #------------->>>
        #<추가적으로 sales point, 평점을 가져오는 코드>
        book_sales_point=soup.find("div", attrs={"style":"display:inline-block;"}).get_text().split(" ")[3].strip()
        book_review=soup.find("a", attrs={"class":"Ere_sub_pink Ere_fs16 Ere_str"}).get_text().strip()
        #<<<----------------

        #데이터 프레임 리스트 만들기 (ROW)
        #------------->>>
        book=[book_name, book_sales_point, book_review]
        print(book)
        #<<<----------------
        df.append(book)
        print(book_name+"----완료----")
        break

#---------------------------------------------------------------------
#Main 함수 (본문)
length=len(lines)
for i in range(len(lines)):
    print("총",str(length), "중", str(i) ,"번째")
    #URL 주소 합치기(생성)
    #book_name=lines[i]+" "+authors[i]+" "+publishers[i]
    book_name=lines[i]
    try:
        aladin_search(book_name)
    except (IndexError, AttributeError):
        try:
            print(book_name, "없음!")
            book=[book_name, " "," "]
            df.append(book)
            #kobo_search(book_name)
        except (IndexError, AttributeError):
            book=[book_name, " "," ", " ", " ", " "]
            df.append(book)
            print(book_name+"!!!!!!!!오류!!!!!!!!")


#데이터 프레임 만들기 
#df=pd.DataFrame(df, columns=['책 이름', '작가','출판사', '출판연도', 'ISBN', '정가'])
df=pd.DataFrame(df, columns=['책 이름', 'sales point','평점'])
df.head(3)

#저장
df.to_excel("csv로 책 저장2.xlsx", encoding='utf-8-sig')



