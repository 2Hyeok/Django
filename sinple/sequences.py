#sequence.py
# 열겨형 나열형
from itertools import count

#문자열
# name = "홍길동"
# age = 20
# print("name : " + name + " age : " + str(age)) # age는 문자열이기 때문에 강제형변환 해줌
# print("=" * 20) # 문자를 곱하기 한 만큼 풀력해라
# print("name : %s age : %d" %(name, age)) # format과 같이 쓸수 있는 다른방법
# print("name : {0} age : {1}".format(name, age)) # format을 사용한 방법
# print("name : {name} age : {age}".format(name="홍길동", age="30"))
#
# a="Hello"
# print("{0:10}".format(a))
# print("{0:<10}".format(a))  # 왼쪽 정렬
# print("{0:>10}".format(a))  # 오른쪽 정렬
# print("{0:^10}".format(a))  # 가운대 정렬
# print("{0:=^10}".format(a)) # 빈칸을 =로채워라
# print("{0:-^10}".format(a)) # 빈칸을 -로채워라
# print("{0:x^10}".format(a)) # 빈칸을 x로채워라

# 문자열 관련 함수
# a="Hello Python"
# print(a.lower()) # 대문자를 소문자로 바꿔라
# print(a.upper()) # 소문자를 대문자로 바꿔라
# print(a.title()) # 첫글자를 대문자로 바꿔라
# print(a.swapcase()) # 대문자는 소문자로 소문자는 대문자로
# print(a.islower()) # 모든 문자가 소문자면 True 반환
# print(a.count("o")) # 특정 문자열의 갯수를 구해라
# # print(a.index("a")) # 예외 처리를 해주어야함
# print(",".join(a)) # a라는 애한테 ,를 넣어주어라
#
# b="    b     b    b    "
# print(b.lstrip(" ")) # 왼쪽 공백을 지워라, 띄어쓰기 영역을 주어야함
# print(b.rstrip(" ")) # 오른쪽 공백을 지워라
# print(b.strip(" ")) # 양쪽다 공백을 지워라
# print(a.replace("o", "a")) # o를 a로 바꾸겠다.
# print(a.split()) # 띄어쓰기 기준 자르겠다
# print(a.split("o")) # o를 기준으로 자르겠다 
#
# c="ABC123"
# print(c.isalnum()) # 알파벳과 숫자인가
# print(c.isalpha()) # 전부다 알파벳 인가
# print(c.isidentifier() ) # 변수로 사용할 수 있느냐
# print(c.isdigit()) # 숫자로 되어있느냐
#
# print()
# print("0abc".isidentifier()) # 해당문자열을 변수로 사용할 수 있느냐 -> x 앞에 숫자이기때문
# print(" abc".isidentifier()) # 띄어쓰기 불가능
# print("_abc".isidentifier())
# print("a+bc".isidentifier()) # 연산자는 변수에 쓸 수없다
# print("a$b".isidentifier()) # 자바만 가능하기에 불가능
# print("가나다".isidentifier()) # 유니코드 체제이기에 가능
#
# # 인덱싱
# # 인덱스를 가지고 데이터를 처리하는것
# # 0   1   2   3   4   5   6   7   8   9   10  11   12
# # H | e | l | l | o |   | P | y | t | h | o | n | \0 | 배열 리스트
# print(a[0]) # a의 0번
# # print(a[12]) # 범위를 넘어 사용불가
# print(a[11])
#
# # 슬라이싱
# # 세로 가로로 자르는것이 가능
# # 리스트가 1차원이기에 데이터를 자를것
# print( a[:] ) # 전체를 다 출력해라
# print( a[3:] ) # 3번째부터 찍어라
# print( a[:10] ) # 맨 앞부터 10까지 찍어라 끝 인덱스는 빠져서 o가 아닌 h까지 출력
#                 # 문자열은 두글자 이상, 문자열은 메모리를 얼마나 잡아야할지 정해지지 않음
#                 # a="ABC" 방이 4개가 잡힘
#                 # 메모리 관리때문에 생김 항상 null이 있음, 자바는 출력이 가능함, 하지만 파이썬은 출력 불가
#                 # end index = -1 이다
#
# print( a[2:10] ) # 2부터 10까지, 맨끝은 -1
# print( a[:-1]) # 끝자리 n이 빠짐
# print( a[:-2]) # 끝자리 on이 빠짐
#
# # 리스트
# # 임의의 객체를 순차적으로 저장하는 집합적 자료형
# # 대괄호 [] 는 리스트를 의미
# print()
# fruits = ["banana", "apple", "orange", "pear", "grape"]
# print("banana" in fruits) # 안에 있냐
# print("melon" in fruits) # 안에 없으니 false
#
# print( fruits[3]) # fruits의 3번을 꺼내라
# fruits[3] = "melon" # 3번방에 melon을 넣어라
# print(fruits)
#
# # 리스트의 슬라이싱
# print(fruits[:]) # 전체 출력
# print(fruits[2:])
# print(fruits[:3]) # -1이라 orange 까지 찍힘
# print(fruits[:-2])
# print(fruits[4][1]) # 4번째꺼의 1번 r
#
# print(len(fruits))
# print(max(fruits)) # 아스키코드값 한글자씩 서로 비교함 제일 큰것 -> orange
# print(min(fruits)) # 아스키코드값 제일 작은것 -> apple
#
# print(fruits)
# fruits.append("pear") # 맨 뒤로 추가해라, 리턴값이 없기에 프린트 사용x
# print(fruits)
# fruits.insert(2, "watermelom") # 다음 순번으로 밀림
# print(fruits)
# # fruits.extend("apple") # 문자열이 따로 따로 들어감
# # print(fruits)
# print(fruits.count("apple")) # 몇개있는지
# print(fruits.index("apple")) # 찾고싶은 위치
# print(fruits.pop()) # 맨 끝에 잇는것을 꺼내고 지워라
#                     # 스텍에서 많이씀
#                     # 넣을때는 put
# fruits.remove("apple") # 지워라
# print(fruits)
#
# fruits.sort() # 알파벳 순으로 정렬해라
# print(fruits)
#
# fruits.sort(reverse=True) # 내림차순으로 정렬해라
# print(fruits)
#
# shop=["라면", "햇반", "김치"]
# shoplist = [fruits, shop]
# print(shoplist) # 2차원으로 나옴
#
# # 인덱싱
# print(shoplist[1][1] ) #1행의 1열데이터
# print(shoplist[1][1][1]) #1행의 1열 1면
#
# # 슬라이싱
# print(shoplist[1][:2]) #1행의 2까지 찍어라
# shoplist[1].append("대파")
# print(shoplist)
# print(shoplist[:2][:2]) # 4개가 안나옴 나중엔 numfine을 써야함
# print(shoplist[0][:len(shoplist[0])]) # 0번행의 배열의 길이만큼 찍어라

# 튜플
# print()
# a, b = (10, 20)
# print(a, b)
#
# zoo = ("dog","cat", "monkey", "snake") # 전체를 하나의 이름으로 받겠다.
# a,b,c,d = zoo
# print(a)
# print(b)
# print(c)
# print(d)
#
# print(zoo[0]) # 인덱싱 가능
# print(zoo[:2]) # -1이기에 dog, cat만 나옴 출력시 소괄호 포함해서 나옴
# print(len(zoo))
#
# # list <==> tuple
# z=list(zoo)
# z.sort()
# print(z)
# print(type(z)) # 리스트로 나옴
# z.append("tiger")
# print(z)
#
# t=tuple(z) # 다시 튜플로 바꿈
# print(max(t))
# print(t.index("tiger"))
# print(t)
# print(type(t))

# 일반함수 구현
# 많이 쓰는 방법이니 알아둘것
def calc(a, b): # 들여쓰기는 영역이 중요
    return (a+b, a-b, a*b, a/b)

a,b,c,d = calc(5, 2) # 길이는 필수로 맞춰주어야함
print(a, b, c, d)

values = calc(5,2)
print(values[0])


# set
# 함수를 사용함
country = set(["korea", "japan", "russia","taiwan"])
print(type(country)) #타입은 set인걸 표현
country.add("korea")
print(country) # korea 가 이미 들어가 있어서 안들어감, 출력은 중괄호
nation = country.copy()
nation.add("USA") # 하나씩 밖에 못줌
print(nation) # 메모리에 저장된 순서대로 나옴
print(nation - country) # 차집합
print(nation | country ) # 합집합, 양쪽에 하나라도 들어있으면 참
print(nation & country) # 교집합, 둘다 참일경우
print()
print(nation.difference(country)) # 차집합
print(nation.union(country)) # 합칩합
print(nation.intersection(country)) # 교집합

nation.remove("USA")
print(nation)
nation.pop() # set 에서 pop은 임의로 하나 출력후 지워버림
print(nation)

print(nation.symmetric_difference(country)) # 대칭자를 만든다

print("korea" in nation)
print("korea" not in nation)