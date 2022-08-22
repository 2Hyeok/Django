# crawling.py

# 스레드 Thread
# 스레드를 쓰지 않은경우
# import time
# def doing() :
#     time.sleep(1) # 1초 마다 멈춰라
#     print("실행중")
#
# start = time.time()
# for i in range(10) : # 10번반복
#     doing()
# end = time.time()
# print("실행시간 :",(end-start)) # 반복이 끝난후 시간 표시

# 스레드를 사용하여 처리한 경우
import time
import threading
# def doing() :
#     time.sleep(1)
#     print("쓰레드 실행중")
# # 메인도 쓰레드 이기에 메인도 만들어주어야함
# if __name__ == "__main__" :
#     start = time.time() # 실행전 저장
#     # 조인이라는 메소드를 실행 해 주어야함
#     # 반복문으로 돌림, 쓰레드를 리스트로 담음
#     threads = []
#     for i in range(10) :
#         t = threading.Thread(target=doing) # run이라는 메소드가 있지만 파이썬은 아무거나 정해주면됨
#         t.start()   # 실행 대기 상태
#         threads.append(t)
#     for thread in threads :
#         thread.join()
#     end = time.time()
#     print("실행시간 :",(end-start))
    
#-------------------------------------------------------------------------

# 조인을 안부를 수 있게하는 방법이 있음
# 동시
# concurrent
from concurrent import futures  # start() join을 자동으로 처리
# def doing() :
#     time.sleep(1)
#     return "스레드 실행중" # 리턴 시켜줌
# if __name__ == "__main__" :
#     start = time.time()
#     results = []
#     with futures.ThreadPoolExecutor() as excutor :
#         for i in range(10) :
#             result = excutor.submit(doing)
#             results.append(result)
#     for f in futures.as_completed(results) :
#         print(f.result())
#     end = time.time()
#     print("실행시간 :",(end-start))
    
#---------------------------------------------------------------------------

# 쓰레드를 사용하지않음
# 연산
# 멀티프로세스
# def calc_sum(list) :
#     sum = 0
#     for i in range(list[0], list[1]+1) :
#         # 넘어온 값만큼 sum을 계산
#         sum += i
#     return sum
# if __name__ == "__main__" :
#     start = time.perf_counter() # time.time() 써도 상관 없음, 기능은 똑같음
#     result = calc_sum([1, 100000000]) # 실행시간이 길라면 숫자를 크게 주면됨
#     print(result)
#     end = time.perf_counter()
#     print("실행시간 :",(end-start))

#---------------------------------------------------------------------------

# 쓰레드로 처리
# def calc_sum(list):
#     sum = 0
#     for i in range(list[0], list[1]+1) :
#         sum += i
#     return sum
# if __name__ == "__main__" :
#     # start(), join() 뺄거임
#     start = time.time()
#     with futures.ThreadPoolExecutor() as excutor :
#         # 2차원 배열로 만들것임
#         sub = [ [1, 100000000//2], [100000000//2 + 1, 100000000] ] # 리스트로 던지는것이 시작위치와 끝 위치, index로 주기에 정수가나와야함 // 두개 써줘야함
#         results = excutor.map(calc_sum, sub) # 알아서 처리함
#     print(sum(results))
#     end = time.time()
#     print("실행시간 :",(end-start))

#------------------------------------------------------------------------

# 멀티프로세스
from multiprocessing import Pool
# def calc_sum(list):
#     sum = 0
#     for i in range(list[0], list[1]+1) :
#         sum += i
#     print(sum)
# if __name__ == "__main__" :
#     start = time.time()
#     sub = [ [1, 100000000//2], [100000000//2 + 1, 100000000] ]
#     pool = Pool(processes=2) # 프로세스를 몇개를 쓸것인지 정해줌
#     pool.map(calc_sum, sub)
#     pool.close() # 썻기에 닫아주어야함
#     pool.join()
#     end = time.time()
#     print("실행시간 :",(end-start))

#------------------------------------------------------------------------

# 쓰레드 동기화
# 두개를 동시에 처리하면서 공유하는 변수가 있어야함
# 전역변수로 변수 생성

# number = 0
# def thread1(num):
#     global number
#     for i in range(num+1) :
#         number += 1
#
# def thread2(num):
#     global number
#     for i in range(num+1) :
#         number += 1
#
# # 쓰레드 처리
# if __name__ == "__main__" :
#     threads = [] # 쓰레드 들을 담을 리스트
#     start = time.time()
#     t1 = threading.Thread(target=thread1, args=(50000000,))
#     t1.start()
#     threads.append(t1)
#     t2 = threading.Thread(target=thread2, args=(50000000,))
#     t2.start()
#     threads.append(t2)
#     for thread in threads :
#         thread.join()
#     print(number)
#     end = time.time()
#     print("실행시간 :", (end-start))
    
#------------------------------------------------------------------------

# 쓰레드의 충돌 방지
# 쓰레드 동기화
# number = 0
# lock = threading.Lock()
# def thread1(num):
#     global number
#     lock.acquire()  # 다른 스레드의 접근을 금지하도록 락을 걸어줌
#     for i in range(num) :
#         number += 1
#     lock.release()  # 작업이 끝났기 때문에 락을 풀어줌
# def thread2(num):
#     global number
#     lock.acquire()  # 다른 스레드의 접근을 금지하도록 락을 걸어줌
#     for i in range(num) :
#         number += 1
#     lock.release()  # 작업이 끝났기 때문에 락을 풀어줌
# # 쓰레드 처리
# if __name__ == "__main__" :
#     threads = [] # 쓰레드 들을 담을 리스트
#     start = time.time()
#     t1 = threading.Thread(target=thread1, args=(50000000,))
#     t1.start()
#     threads.append(t1)
#     t2 = threading.Thread(target=thread2, args=(50000000,))
#     t2.start()
#     threads.append(t2)
#     for thread in threads :
#         thread.join()
#     print(number)
#     end = time.time()
#     print("실행시간 :", (end-start))

#------------------------------------------------------------------------

# 멀티프로세스 동기화
# 공유하는 변수가 있을경우 멀티 프로세스도 동기화를 해주어야함
# from multiprocessing import shared_memory, Semaphore, Process
# import numpy as np
# def calc_sum(id, number, shm, arr, sem): # 매개변수를 여러개 받아줌, 쓰레드의 이름이 넘어옴
#     # id 스레드 번호
#     # number 최대값
#     # shm 공유메모리(셰어드메모리)
#     # arr numpy.array배열
#     # sem 세마포어
#     sum = 0
#     for i in range(number) :
#         sum += 1
#     sem.acquire()   # 세마포어 획득, 임계영역에 들어감, 임계영역은 무조건 (쓰레드)1개밖에 못들어감, 하지만 세마포어는 여러개가 가능함
#                     # 세마포어는 자리하나를 차지했다는 개념이라, 충돌안나게 처리해줌
#     new_shm = shared_memory.SharedMemory(name=shm) # 공유매모리를 사용할 수 있게 가져옴
#     tmp_arr = np.ndarray(arr.shape, dtype=arr.dtype, buffer=new_shm.buf) # 넘겨받은 갯수만큼 받아라, 넘겨받은 array의 dtype, 임시기억장소
#     tmp_arr[0] += sum # 쓰레드 들이 계산한 값을 누적해야함
#     sem.release()   # 세마포어 해제
# if __name__ == "__main__" :
#     start = time.time()
#     arr = np.array([0]) # 0을 넣어놓는 하나짜리 방 생성
#     # 공유 메모리이기에 메인에서 만들어서 보냄
#     shm = shared_memory.SharedMemory(create=True, size=arr.nbytes)
#     np_shm = np.ndarray(arr.shape, dtype=arr.dtype, buffer=shm.buf)
#     sem = Semaphore()
#     p1 = Process(target=calc_sum, args=(1, 50000000, shm.name, np_shm, sem)) # 다 넘어가야함
#     p2 = Process(target=calc_sum, args=(2, 50000000, shm.name, np_shm, sem))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time.time()
#     print(np_shm[0]) # 합계는 이곳에 들어있음
#     print("실행시간 :", (end-start))
#     shm.close() # 닫다
#     shm.unlink() # 끊다

#--------------------------------------------------------------------------------------------------
# 네트워크
import urllib.request as req
from urllib.error import URLError
# f = req.urlopen("http://www.daum.net") # 먼저 열어주어야함, 링크를 주면됨
# print(f.read( 100 ).decode("utf-8")) # 몇 바이트 읽어올지, 디코딩 해주어야함
# html 소스를 가져옴

# re = req.Request("http://www.daum.net")
# try :
#     req.urlopen(re) # 오픈시 예외처리
# except URLError as e :
#     print(e.reason)

# response = req.urlopen("http://www.daum.net")
# print(response) # 객체가 넘어옴, 하나씩 꺼내써야함, 메소드를 통해 꺼내면됨
# print("url :",response.geturl())
# headers = response.info() # 헤더 정보들이 넘어옴
# print("date :", headers["date"]) # 딕셔너리
# print(headers) # 많은 정보가 있음
# data = response.read() # 모든 데이터를 가져옴
# print(len(data)) # 데이터의 길이

#--------------------------------------------------------------------------------------------------

# # 크롤링
# import urllib.request
# url = "https://cdn.topstarnews.net/news/photo/202205/14689700_790468_3839.jpg"
# savename = "ricegood.jpg"
# urllib.request.urlretrieve(url, savename)
# print("저장했습니다")
#
# # 파일저장
# url = "http://www.google.com/robots.txt"
# txt = urllib.request.urlopen(url)
# data = txt.read().decode("utf-8")
# # print(data) # 콘솔창 표시
# with open("robots.txt", "w", encoding="utf-8") as f:
#     f.write(data)
# print("저장했습니다.")

#-------------------------------------------------------------------------------------------------

# 스크랩핑
# RSS -> 스크랩핑을 해라 라고 재공해주는 것, 기본은 XML, 제공해 주는것이 많지는 않음, 기상청같은경우 RSS를 이용해 크롤링 해야함
import urllib.request as req
import urllib.parse as pa # 나중에 주소와 아이디를 합치기 위함
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp" # ?stnId=109 이부분은 나중에 따로 사용할 예정
values = { # 딕셔너리로 만듬
    "stnId" : 109
    }
params = pa.urlencode(values)
url = url + "?" + params # 주소를 합침
# print(url)

data = req.urlopen(url).read().decode("utf-8") # 주소를 읽어들임
# print(data)

#------------------------------------------------------------------------------------------------------
# BeauticulSoup
from bs4 import BeautifulSoup as bs
html = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>HTML Test </title>
        </head>
        <body>
            <h2>HTML 연습</h2>
            <p id="first"> 짜장면 </p>
            <p class="strong"> 짱뽕 </p>
            <p class="point strong"> 탕수육 </p>
            <p id="second"> 울면 </p>
        </body>
    </html>
"""

soup = bs(html, "html.parser") # html을 자르는것
print("<<" +soup.find("h2").string+ ">>") # 글자를 꺼내라
print("<<" +soup.html.body.h2.string+ ">>")

h2 = soup.find("h2")
body = h2.parent # body만 출력
# print(body)
html = body.parent # html 전부 출력
# print(html)
p1 = h2.next_sibling.next_sibling
print(p1.string)
nodes = body.children
# for node in nodes :
#     print(node) # 자식 노드들이 나옴
#     print(node.string) # 문자열만 나옴

ps = soup.find_all("p") # p테그 찾기
for p in ps :
    print(p.string)
    
p = body.findChild()
print(h2.string)
print()

p1 = soup.find(id="first") # id가 first인것
print(p1.string)

p4 = soup.find(id="second") # id가 second인것
print(p4.string)

pp = soup.find_all(class_="strong") # class는 예약어 이기에 _를 포함함
for p in pp :
    print(p.string)
    
    
# select()
# select_one()
# 테그 밑에 테그가 또있어야하는것이 필요
html = """
 <html>
        <head>
            <meta charset="utf-8">
            <title> HTML 연습 </title>
        </head>
        <body>
            <h2 class="title"> 웹 스크랩핑 </h2>
            <p id="name"> HTML </p>
            <p class="subject"><a> XML </a></p>
            <p class="subject"><b><a> JSON </a></b></p>
            <a> CDATA </a>
        </body>
    </html>
"""
soup = bs(html, "html.parser")
h2 = soup.select_one("body h2")
print("<<" + h2.string + ">>")

ps = soup.select( ".subject" )
for p in ps :
    print( p.string )

pp = soup.select( "body p" )
for p in pp :
    print( p.string )
    
pp = soup.select( "p a" ) # 자손 선택자
for p in pp :
    print( p.string )

pp = soup.select( "p > a" ) # 자식 선택자
for p in pp :
    print( p.string )
    
p = soup.select_one("p#name")
print(p.string)

p = soup.select_one("p.subject")
print(p.string)
#------------------------------------------------------------------------------------------------------

# RSS -> 스크랩핑을 해라 라고 재공해주는 것, 기본은 XML, 제공해 주는것이 많지는 않음, 기상청같은경우 RSS를 이용해 크롤링 해야함
import urllib.request as req
import urllib.parse as pa # 나중에 주소와 아이디를 합치기 위함
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp" # ?stnId=109 이부분은 나중에 따로 사용할 예정
values = { # 딕셔너리로 만듬
    "stnId" : 109
    }
params = pa.urlencode(values)
url = url + "?" + params # 주소를 합침
# print(url)

data = req.urlopen(url).read().decode("utf-8") # 주소를 읽어들임
# print(data) # 데이터 양이 많음

with open("whether.txt", "w", encoding="utf-8") as f : # 파일을 저장
    f.write(data) # 저장할 필요는 없음, 데이터 확인용

soup = bs(data , "html.parser") # 데이터를 자름

title = soup.find("title")
print("<<" + title.string + ">>")

cities = soup.find_all("city") # city를 다 뽑음
# for city in cities : # 반복문으로 돌려 city 만뽑음
#     print(city.string)
    
datas = soup.find_all("data") # data를 다 뽑음
for data in datas : # 반복문을 새로 돌림
    print(data.parent.city.string, end="\t") # city 와 data가 동일선상에 놓여있음, 출력하고 탭을함
    print(data.tmef.string, "\t", data.wf.string,   # 시간을 뽑음, 그후 탭을 한후 날씨를 뽑음
          "\t", data.tmn.string, "\t", data.tmx.string) # 최저기온과 최고기온을 뽑음
print()
#------------------------------------------------------------------------------------------------------