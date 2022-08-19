# 추상화 abstract
# 추상함수라고 잘 안부름(자바에서는 추상메소드)
from abc import abstractmethod, ABCMeta
from ntpath import split
from cgi import logfile

class Animal (metaclass=ABCMeta):  # 추상 클래스라는 명시를 해주어야함, 임포트 필요, 단 객체 생성 불가
    def __init__ (self, name="", age=0):
        self.name = name
        self.age = age
        
    @abstractmethod # 임포트 필요
    def disp(self):
        # print("Animal : ", self.name, self.age) # 추상메서드, 구현은 가능하나 쓸대가없음(구현할 필요가 없음) 그래서 pass를 줌
        pass # 내용을 안넣음, 호출이 안됨 구현할필요가 없음

# animal = Animal()    # 추상 클래스, ABCMeta 사용시 객체를 생성할 수 없다.
# print(animal.disp()) # 비어있기에 none 출력

class Dog (Animal) : # 상속받음
    # 추상화라 해줄핗요 X
    # 자바의 경우에는 구현 필요(반드시 있어야함)
    # 하지만 python은 생략이 가능하다
    # def __init__(self, name, age): # 상속받을때 자동으로 만들어짐
    #     Animal.__init__(self, name, age)
    # pass
    # 추상메소드 구현 필요
    def disp(self): # 추상메서드는 반드시 구현 해야한다.
        print(self.name, self.age)

class Cat(Animal):
    def disp(self): # 추상메서드는 반드시 구현 해야한다.
        print(self.name, self.age)

dog = Dog("양규호", 5)
dog.disp()
cat = Cat("임두혁", 3)
cat.disp()
#---------------------------------------------------

import traceback
# 예외처리
# C                 경고    에러    예외(정의해야 한다)
# Java              에러    에러    예외(정의되어 있다)
# Python            에러    에러    에러

# syntax error -> 오타, 문법이 틀린경우
# semantic error -> 예외, 실행중 문제가 발생하는 경우

# ZeroDivisionError
# a = 4 /0 # 무조건 나는 에러, 0으로 나눌 수 없음

try :
    # a = 4/0 # ZeroDivisionError
    # a = 4/ "2" # TypeError
    a = 4 / 2
    
# except Exception : # 단 순서가 중요함 예외처리를 또 해줄 수없어 밑으로 주어야함
#     traceback.print_exc()
except ZeroDivisionError :
    print("0으로 나눌 수 없습니다")
except TypeError :
    print("정수로만 나눌 수 있습니다.")
except Exception : # 모든 예외를 다 잡을 수 있는 최상위
    traceback.print_exc() # 실행할때 문제가 생긴것을 확인해라
    
else : # else 도 넣어줄 수 있음
    print("값 : ", a)
    
finally: # 예외가 있든 없든 무조건 실행
    print("프로그램 끝")

#-------------------------------------------------------------------
    
# 사용자 정의 예외
# 예외가 아닌데 예외로 정의한것

# class NumberException(Exception):
#     pass
# class InputException(Exception):
#     pass
#
# try :
#     a = input("단 : ")
#     # print(a)
#
#     if not a.isdigit() : # 기본함수, 숫자가 아닌가, eval X 
#         raise NumberException() # 강제로 발생시킴
#     elif int(a)<2 or int(a)>9 : # 형변환 필요
#         raise InputException()
# except NumberException :
#     print("숫자만 입력 가능합니다")
# except InputException :
#     print("2~9 사이만 입력하세요")
# else :
#     for i in range(1, 10) :
#         print(a, "*", i, "=", int(a)*i) # 연산이기에 형변환 필요
# finally :
#     print("프로그램 끝")
    
#--------------------------------------------------------------------

# 모듈       파일
# 패키지      폴더
# Java      부품의 단위 - 클래스
# Python    부품의 단위 - 모듈


# hello() # 에러남
# import simple.module.mymodule # 노란줄 신경 ㄴㄴ 이클립스가 인식을 못해서그럼
# simple.module.mymodule.hello() # 경로를 다 주어야함
# simple.module.mymodule.bye()
#
# user = simple.module.mymodule.User("양규호", 28)
# print(user.getName())
# print(user.getAge())
#
# # 너무 길어서 힘듬
# # 별칭을 줄 수 있음
# import simple.module.mymodule as my
# my.hello()
# my.bye()
# user = my.User("임두혁", 24)
# print(user.getName())
# print(user.getAge())
#
# # from 을써서 가까이감, 하지만 좋은방법은아님 필요없는것들도 다 가져오기때문
# from simple.module import mymodule
# mymodule.hello()
# mymodule.bye()
# user = mymodule.User("유제욱", 30)
# print(user.getName())
# print(user.getAge())
#
# from simple.module.mymodule import hello, bye, User # 따로따로 써줄경우 이런식으로 쓸것들만 가져옴
# hello()
# bye()
# user = User("김영식", 36)
# print(user.getName())
# print(user.getAge())
#
# from simple.module.mymodule import User as U # 별칭 표시도 가능
# user = U("함형일", 29)
# print(user.getName())
# print(user.getAge())


#-------------------------------------------------------------------------------------------

# 자주사용하는 모듈
import os
# print(os.__doc__)
# print(help(os)) # 좀더 자세하게 보여줌
# print(help(os.mkdir)) # mkdir 이라는 함수에 대한것만 알려줌
# python -m pydoc -p 3333

# 특정 경로의 파일 가져오기
path = "C:/"
for file in os.listdir(path): # 패스가 리스트로 들어옴 for문으로 프린트
    if os.path.isdir(path+file) : # 경로를 다 주어야함
        print("폴더 : ",file)
    else :
        print("파일 :",file)
    print(os.path.split(path + file)) # 파일따로 경로 따로 알려줌
    print(os.path.join(path + file)) # 문자열로된 경로를 하나로 합쳐줌(종종 사용함)
# 절대경로
print(os.path.abspath(path))
print(os.path.abspath(".")) # 현제 파일의 경로
if not os.path.exists("test"): # 폴더가 없으면
    os.mkdir("test") # 만들어라(test)라는 폴더를
    
if os.path.exists("test"): # 폴더가 있으면
    os.rmdir("test") # 지워라("test")라는 폴더를
    
#-------------------------------------------------------------------------
import sys
print(sys.exc_info()) # 실행할 때 예외정보를 알려줌
# sys.exit(0) # 프로그램 종료
print(sys.modules) # 사용가능한 모듈들을 알려줌
print(sys.path) # 사용할 수 있느 모듈들의 라이브러리 경로를 알려줌
print(sys.version)
print(sys.version_info)

#-------------------------------------------------------------------------
import logging, platform # os도 임포트 필요, 현재 플렛폼을 알고싶으면 platform
print(platform.platform())
if platform.platform().startswith("Window") : # 문자열 관련 함수, 어떠한 문자열로 시작하느냐 라는뜻
    # 윈도우인경우
    # 저장경로를 내 문서로 가져다가 만들것임
    logfile = os.path.join( os.getenv( "HOMEDRIVE" ), os.getenv( "HOMEPATH"), "test.log" ) # 홈드라이브, 환경변수를 가져옴, 이런식으로 저장경로를 만들어줌
else :
    # 윈도우가 아닌경우
    logfile = os.path.join( os.getenv( "HOME" ), "test.log" )
print(logfile)
logging.basicConfig(
        level = logging.ERROR,# 출력할레벨
        format = "%(asctime)s : %(levelname)s : %(message)s", # 시간, 레벨, 메시지가 출력 혹은 시스템의 메시지, 정해진 값
        filename = logfile,
        filemode = "w" # 쓰기모드
        # 코드 중간중간에 로그를 끼워넣어야함 
        # 
    )
logging.debug("디버그") # 순수하게 우리가 만듬
logging.info("정보")
logging.warning("경고")
logging.error("에러")
logging.critical("크리티컬")

#--------------------------------------------------------------------------------
# 데이터 타입 관련 모듈

from datetime import date, time, datetime, timedelta # 타임델타는 날짜 계산할때 주로 사용
now = date.today()
print(now) # 현제 날짜 출력
print(now.year, "년", now.month, "월", now.day, "일") # 따로 짤라서 사용가능

now = datetime.today()
print(now) # 100만분의 1초
print(now.year, "년", now.month, "월", now.day, "일",
      now.hour, ":", now.minute, ":", now.second, " ", now.microsecond)

import time
print(time.time()) # time은 따로 뽑아써야함
print(time.gmtime(time.time())) # 튜플
t = time.gmtime(time.time())
print(t.tm_hour + 9, "시") # 한국시가 아님


# print(now + 30) # 날짜자료형과 int자료형 이기에 에러남
print(now + timedelta(30)) # 그럴때 쓰는것이 timedelta, 현재 날짜에서 30일 후

print(now.strftime("%y년 %m월 %d일 %H : %M : %S")) # 날짜 문자로 바꿔줌
s = "2022-8-18 13:05:30"
print(datetime.strptime(s, "%Y-%m-%d %H:%M:%S")) # 문자열을 날짜로 바꾸어줌, 형식도 맞춰주어야함
t=datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(type(t)) # 자료형 바뀐것 확인

#----------------------------------------------------------------------------------------
#난수
import random
# random.seed(0) # 고정값으로 랜덤값을 사용한다, 이래야 데이터를 활용할 수 있음
# for i in range(6) :
    # print(int(random.random() * 45) + 1) # 인트로 형변환 시 소수점 사라짐, 0~99(100으로 설정시) 이기에 1 부터 시작하기 위해 +1을함
lotto = random.sample(range(1, 46), 6) # 중복안되는값 리스트로 묶어 출력
# print(lotto.sort()) # 정렬, 하지만 none값 출력
print(sorted(lotto)) # 이렇게도 가능
random.shuffle(lotto) # 섞어줌
print(lotto)

for i in range(6) :
    # print(random.randint(1, 45)) # int형으로 출력
    print(random.uniform(1, 45)) # 범위 안에서 실수로 출력

#---------------------------------------------------------------------------------------
# 파일 입출력
# 프로젝트때 이미지가 안나오는 경우
# 서버에 올라가는 경우
# 이미지경로는 서버 경로를 주어야한다.
# getRealPath
# 혹은 상대경로로 주어야함

f = open("a.txt", "a", encoding="utf-8") # 현재 디렉토리에, 읽기 권한만, 파일 읽기, a라 쓸경우 계속 덮어씀
for i in range(1, 11) :
    f.write(str(i) + " ") # 문자열밖에 못받음
f.write("\r\n") # 한줄쓰고 줄 바꿔라 라는 표현
print("파일생성 완료")
f.close() # 열었기 때문에 반드시 해주어야함

# f =open("a.txt", "r", encoding="utf-8")
# while True :
#     data = f.read()
#     if data == "":
#         break
#     print(data, end=" ")
# print()
# f.close()

# f = open("a.txt", "r", encoding="utf-8")
# while True :
#     line = f.readline() # 한줄씩 읽어라
#     if line == "" :
#         break
#     print(line)
# f.close()

# f = open("a.txt", "r", encoding="utf-8")
# for line in f : # 읽기모드할때 f를 줌
#     print(line)
# f.close()


# 여러줄을 출력할 때
with open("a.txt", "r", encoding="utf-8") as f : # 영역이 끝나면 자동 close를 해줌, close를 줄 필요가 없음
    lines = f.readlines() # 여러줄을 출력해라
    for line in lines :
        print(line)
        
#------------------------------------------------------------------
# CSV
with open("lotto.csv", "w") as f :
    for i in range(10) :
        m = random.sample(range(1, 46), 6)
        m.sort()
        for i, a in enumerate(m) : # m 이라는 배열에서 값을 뽑아 저장
            f.write(str(a))
            if(i < len(m) -1 ) :
                f.write(",") # ,로 값을 나눠야해서 꼭 찍어줘야함
        f.write("\n")
        
with open("lotto.csv", "r") as f :
    for line in f : # 한줄 씩 읽을거다
        for a in line.split(",") :
            print(a, end="\t")
        print()


#------------------------------------------------------------------------
# 피클링   pickling      객체단위 입출력

# 바구니 생성
class User :
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel= tel
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getTel(self):
        return self.tel

import pickle
hong = User("홍길동", 20, "1111-2222")
with open("user.txt", "wb") as f : # 쓰기 바이너리 모드
    pickle.dump(hong, f) # hong이란것을 f를 이용해 저장해라
    
with open("user.txt", "rb") as f : # 파일을 읽어서 출력해라, 바이너리 모드
    user = pickle.load(f)
    print(user.getName(), user.getAge(), user.getTel())

users = [
        User("김유신", 20, "1111-1111"),
        User("이순신", 30, "2222-2222"),
        User("홍길동", 25, "2222-1111")
    ]

with open("user.txt", "wb") as f :
    pickle.dump(users, f)
with open("user.txt", "rb") as f :
    us = pickle.load(f)
    print(type(us)) # 리스트로 넘어옴
    for u in us :
        print(u.getName(), u.getAge(), u.getTel())

print()
#----------------------------------------------------------
# 정규 표현식    Regular Expression
import re

# match
p = re.compile("[a-z]+")
print(p.match( "" )) # 아무것도 없기 때문에 none출력
print(p.match(" ")) # none출력
print(p.match("a "))    # a만출력
print(p.match("python!!")) # !는 출력안됨 python만 출력
print(p.match("Python!!")) # none출력
print(p.match("pyThon!!")) # 매칭이 되는것만 찾아줌, py만 출력
print(p.match(" python!!")) # 앞에 띄어쓰기가 있기때문에 none출력


# search
print(p.search( "" )) # 아무것도 없기 때문에 none출력
print(p.search( " " )) # 아무것도 없기 때문에 none출력
print(p.search("a ")) # a만출력
print(p.search("python!!")) # !를 제외한 python 출력
print(p.search("Python!!")) # 중간부터 찾기에 ython 출력
print(p.search("pyThon!!")) # py출력
print(p.search(" python!!")) # python출력

word = p.search(" python!!")
print(word.start())
print(word.end())
print(word.span())
print(word.group())


s = "Life is too Short"
print(p.match(s)) # 첫글자가 대문자여서 매칭되는것이 없음
print(p.search(s)) # ife만 출력
print(p.findall(s)) # 리스트로 돌려줌
print(p.finditer(s)) # 이터레티어 객체로 돌려줌
for word in p.finditer(s) :
    print(word.group()) # 여러개를 돌려줌
    print(word)
    
    
p = re.compile("a.b") # 중간에 한글자가 꼭 들어와야함 \n 만아니면됨
print(p.search("ab")) # 매칭불가
print(p.search("ac")) # 매칭불가
print(p.search("acb")) # 매칭 가능
print(p.search("a0b")) # 문자가 아닌 숫자가 와도 가능
print(p.search("a$b")) # 특수문자도 가능
print(p.search("a\tb")) # 다른 제어문자 가능
print(p.search("a\nb")) # none 출력
print(p.search("accb")) # 여러개가 들어가도 매칭불가


s = """
    abc acb accb a
    cb a\nb a0b a\tb
"""

# findall로 찾아야함
print(p.findall(s))
p = re.compile("a.b", re.DOTALL) # re.s, 얘는 \n도 가능
print(p.findall(s))


# ignirecase
# 양도 많아짐
# 특수문자도 포함하기때문
p = re.compile("[A-Z]+") # 대문자가 하나이상
print(p.findall(s))
p = re.compile("[A-Z]+", re.IGNORECASE) # re.I 대소문자 상관없이
print(p.findall(s))


s = """python one
pythontwo
python
study python
python 1
life is too short"""
p = re.compile( "^python\s\w+" )
print( p.findall( s ) )
p = re.compile( "^python\s\w+", re.MULTILINE )  # re.M, 멀티라인이면 각각 다른문장으로 인식을함
print( p.findall( s ) )

#------------------------------------------------------------------------------------

# 이메일 유효성 검사
emails = """
aaa@aaa.com
aaa@a.com
AAA@AAA.com
1aa@1aa.com
&&&@&&&.com
aaa@@a.com
@aaa.com
aaa@aaa@aaa.com
aaaaaaaaaaaaaaaaaaaaa@a.com
aa1@aaa.com
aaa@aaa.7com
aaa@aaa.co.kr
"""
# 처음과 끝을 정해주어야함, 각각의 줄마다 다른것으로 인식해라, 첫글자는 문자, 두번째부터는 문자 or 숫자를 15까지 반복함, @ , 회사의 이름은 2글자 이상이기에 2, 라고만 표기, .은 문자이기에  \ 사용
p = re.compile("^[a-z][a-z0-9]{2,15}@[a-z0-9]{2,}\.[a-z]{2,}$", re.M) # co.kr은 따로 걸러야함
print(p.findall(emails))

p = re.compile("^[a-z][a-z0-9]{2,15}@[a-z0-9]{2,}\.[a-z]{2,}\.[a-z]{2,}$",re.M) # co.kr 골라내는 방법
print(p.findall(emails))
