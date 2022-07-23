# book_info_scraper
Although with only one piece of information in the book(book name, author, publisher, ISBN code etc..), we can get other information through this programming.   

When I working in the library, teacher gave me Excel files and asked me to fill in the empty space. That is a lot of empty space about 1000 spaces.    
Only what I know is name of book, but I had to find the author, publisher, price, and ISBN all on the Internet.   

To save my time, I made book information scaper program.    
It is so useful that all the simple labor of computer work in the library has declined dramatically and they hired me for part-time-job.


* **제작자 : 정우진(Woo)**
* **제작 일 : 22.02.10**
* **보고서 작성 일 : 22.07.22**

## Description

근로장학생으로 학교 도서관에서 일을한다. 대부분 일은 책을 받으면 바코드를 붙이거나 청구기호를 붙이는 일을 한다.   
그러던 중 엑셀 서류 업무를 부탁하셨다. 그 업무는 책 이름 또는 책 출판사, 지은이 등등 빈 칸이 많이 있었고,    
해당 엑셀에 있는 정보로만 이용해서 인터넷에서 검색을 해서 나머지 빈 공간을 채우도록 하는 것이다.   

단순작업이라고 생각하고 이는 프로그래밍을 통해 해결할 수 있을것 같다고 생각하여 다음과 같은 프로그램을 짰다.   

책의 이름이든지, ISBN코드 이든지, 책의 정보를 메모장에 입력을 하면,
도서 사이트 알라딘 또는 교보문고를 통해 웹 스크롤을 해서
책의 이름, 출판사, 작가, 출판년도, ISBN코드, 가격 등 정보를 얻은 뒤 엑셀 파일로 다시 정리를 해준다.   

또 알라딘 서적인 경우, Sales point와 평점을 얻어야 하는데 이또한 추가적으로 얻을 수 있도록 했다.   

영어 서적도 다음과 같이 필요하므로 abebook에서 정보를 얻도록 했다. 

## Environment
실행에 필요한 package이다.   

* python 3.8.10
* requests, bs4, pandas
  
## Files
작성한 코드가 각자 어떤 역할을 하는지 설명해준다. 
1. 1_book_info_scapper.py
    * 검색어를 칠 목록을 txt파일로 정리하면 알라딘에서 해당 서적을 찾아 정보를 얻고, 만약 없다면 교보문고에서 해당 서적을 찾아 정보를 얻는다. 
    * 사용하는 사이트 : [교보문고](https://search.kyobobook.co.kr/)
    * 사용하는 사이트 : [알라딘](https://www.aladin.co.kr/)
	
2. 2_aladin_review_Sales.py
    * 평점과 알라딘의 sales point만 정보를 얻기 위한 코드이다. 
    * 사용하는 사이트 : [알라딘](https://www.aladin.co.kr/)
	
3. 3_book_scapper_for_English.py
    * 영어 서적일 경우 우리나라 서적 홈페이지로는 얻을 수 없는 정보가 많이 있다. 따라서 1번 코드와 동일하지만 영어 서적 홈페이지로 동일하게 조사하는 코드이다. 
    * 사용하는 사이트 : [abebooks](https://www.abebooks.com/)

## Usage
작품을 실행하기 위한 방법에 대해 설명한다.   

1. 아래와 같이 도서를 조사하기 전에 주어진 정보가 어떤것이 있는지 확인한다. 

|출판년도, ISBN, 정가를 입력해야 하는 형태|책 제목, 저자, 출판사를 입력해야 하는 형태|
|--|--|
|![nn](/image/source_data.png)|![nn](/image/source_data_2.png)|


2. 2020_text_list.txt 검색 키워드를 입력한다. 이때 ISBN코드만 넣는 것이 가장 정확한 정보를 찾기 쉽다.   
   ISBN코드가 없을 경우 책제목, 출판사, 작가와 같이 한 줄에 ,로 구분지어 연속적으로 적는것이 좋다. 

|txt파일에 정보 입력하기|
|--|
|![nn](/image/input.png)|

3. CSV로 책 저장.csv 또는 CSV로 책 저장2.csv로 결과가 출력된다.   

|ISBN을 입력해 Sales point, 평점을 얻은 형태|책 이름과 작가, 출판사를 통해 출판연도, ISBN을 얻은 형태|
|--|--|
|![nn](/image/2_result.png)|![nn](/image/3_result.png)|

---------------------------------------------------------
