# # Map
# # java
# # int m[] = {10, 20, 30, 40, 50}
# from simple.sequences import values
#
# # Python
# # m = [10, 20, 30, 40, 50]
# kim = {"name" : "김유신", "age" : 30, "tel" : "1111-2222"} # map은 데이터 표시를 위해 중괄호를 사용
# print(type(kim))
#
# # 데이터를 꺼낼때
# print(kim["name"])
# # print(kim.name) # 자바에서의 사용법 이방법은 파이썬에선 에러가남
# print(kim.get("name"))
#
# # 값만 뽑는용
# keys = kim.keys()
# print(keys)
# print(type(keys))
#
# # 파이썬은 자료형변이 없가에 문자열, 정수, 문자열 이 섞어들어감
# # 제네릭은 강제성을 주기위해 줌
# # 자바에서는 다른 자료형을 주면 에러가나지만 파이선은 아님
# # 파이썬은 자료형 명시가 없기에 그냥 뽑으면됨
#
# # values
# values = kim.values()
# print(values)
# print(type(values))
#
# # 키의 유무확인
# # 키를 추가하는것
# # in, not in 연산가능
# if "id" not in kim.keys() :
#     kim["id"] = "aaa"
# print(kim)
# kim["id"] = "bbb"
# print(kim)
#
#
# # items
# # 튜플로 리턴
# # 키와 벨류
# for key, value in kim.items() :
#     print(key, value)
#
# # del - 메모리를 없애라
# # remove의 개념이 없음
# del kim["id"]
# print(kim)
#
# # 슬라이싱
# # 나열형 자료가 아니기에 사용불가
# # print(kim[1])
# # print(kim["name" : "age"])


# 제어문
# a = input("정수 : ")
# print(a)
# print(type(a))

# 형변환을 해주어야 연산이 가능하지만
# javascript 에서 사용한 eval 을 사용하여 가능
# 가장 많이 쓰는 방법임
# a = int(input("정수 : "))
# b = int(input("정수 : "))
# a = eval(input("정수 : "))
# b = eval(input("정수 : "))
# print( a + b )


# 조건문 (if문)
# 구구단
# a = eval(input("단 : "))
# if a >= 2 and a<= 9 :
#     # pass # pass가 없으면 에러남
#     for i in range(1, 10) : # end value - 1 = 1 ~ 9까지
#         print(a, "*", i, "=", a*i)
# else :
#     print("잘못 입력")

# else if
# age = eval(input("나이 : "))
# if age <= 20 :
#     print("어린이")
# elif age <= 40 :
#     print("청년")
# elif age <= 60 :
#     print("중년")
# else :
#     print("노년")

# 삼항연산
# 조건 ? 참 : 거짓
# 파이썬은 삼항연산이 없기에 다른방법
# 많이 씀
a = 6
print("짝수" if a%2==0 else "홀수") # 순서가 중요함 앞이 참 뒤가 거짓


# 반복문
for i in range(10) :
    print(i , end=" ") # 끝값은 -1이다
print()

for i in range(1, 11) :
    print(i, end=" ")
print()

# for i in range(10, -2) : # 10부터 -2 까지 라는뜻 앞에 추가해주어야함
for i in range(0, 10, 2) : # 0부터 10까지 2씩증가
    print(i , end=" ")
print()


for i in range(10, 0 , -1) : # 10 부터 0 까지 -1씩 감소
    print(i, end=" ")
print()

# 컬렉션도 들어갈 수 있음
# 나열형
m = [10, 20, 30, 40, 50]
print(type(m))
for a in m :
    print(a, end=" ")
print()

# 튜플
m = (10, 20, 30, 40, 50)
print(type(m))
for a in m :
    print(a, end=" ")
print()

# 문자열 나열형
m = "ABCDE"
print(type(m))
for a in m :
    print(a, end=" ")
print() # 문자열이 여러개 모인데이터

# set
# 인덱스가 없어서 순서가 없음
# 셋은 중복이 없어 값이 하나만 들어간다.
# 집합연산할때 사용한다.
m = set([10, 20, 30, 40, 50])
print(type(m))
for a in m :
    print(a, end=" ")
print()

# map
m = {"kim" : "김유신", "lee" : "이순신", "hong" : "홍길동"}
print(type(m))
for key, vlaue in m.items() :
    print(key, vlaue)
print()

# list 안에 튜플
m=[(1, 2), (3, 4), (5, 6)]
print(type(m))
for a in m :
    print(a[0],a[1])
print()

# 튜플을 받을땐 이방식으로
# 대신 갯수는 맞춰주어야한다.
for a, b in m :
    print(a, b)
print()

# 반복문 리스트 만들기
m = [i for i in range(1, 101)] # i값을 가지고 만들어라 1 ~ 100
m = [i*2 for i in range(1, 101)] # 2씩 증가
m = ["짝수" if i%2==0 else "홀수" for i in range(1, 101)]
print(m)

# 60점 이상이면 합격 아니면 불합격
scores = {'kim' : 89, 'lee' : 65, 'park' : 45, 'jung' : 96, 'choi' : 55,
          'cho' : 50, 'hong' : 44, 'hwang' : 60, 'ri' : 87, 'sung' : 35}

for key, value in scores.items() :
    if value>=60 : 
        print(key, "합격")
    else : 
        print(key, "불합격")
        
        
# while 문
# 변수가 있어야함
i = 0
while(i<3) :
    print(i)
    i += 1
print()

# else 가 들어갈 수 있음
# 하지만 잘 안씀
i = 0
while(i<3) :
    print(i)
    i += 1
else : 
    print(i)
print()

# break 사용
i = 0
while True: # 항상 돌아라, 무한루프임
    i += 1
    if i > 10 :
        break
    print(i, end=" ")
print()

# enumerate()
# 강제로 인덱스를 만들어줌
# 인덱스가 없는것에 인덱스를 만들어주는것
users = {"kim" : "김유신", "lee" : "이순신", "hong" : "홍길동"}
for i, user in enumerate(users) : # 인덱스랑 key만 나옴
    print(i, user, users[user]) # value 까지나옴
    print(i, user, users.get(user)) # 혹은 get메소드 사용해도 가능