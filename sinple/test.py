# a=10
# print(a)


# import keyword
# print(keyword.kwlist) # 키워드 보기
# print(len(keyword.kwlist)) # 키워드들의 갯수 보기

# print(type(10)) # 정수
# print(type(10.5)) # 실수
# print(type("ABC")) # 문자
# print(type('ABC')) # 문자 하나
# print(type(10 + 10j)) # 복소수
# print(type(1234567890123456789)) # 값을 벗어나지만 파이썬은 정수라고 표시
# print(type(5/2)) # 정수인지 실수인지 확인  2.5
#
# # a = 10, b = 20 # 자바, 파이썬은 불가
#
# a, b = 10, 20 # 튜플이 있기에 이렇게 써야함
#
# # 교환
# c = 0
# c = a
# a = b
# b = c
# print(a, b)
# a, b = b, a
# print(a, b)
#
# del a, b # 지우다
# print(a, b) 

# 한줄씩 해석하기에 한줄이 넘어가는경우
# 엔터로 내리면 안됨
# 그럴경우 역슬레시를 쳐쥼
# print("우리나라 \
# 대한민국")
#
# # 여러줄
# # """ 혹은 ''' 써주어야함 띄어쓰기 까지 먹음
# # API 만드는 용도
# a = """
#     우리나라
#     대한민국
# """
# print(a)
#
# # 강제 형변환
# print(type(10.5)) # float
# print(type( int(10.5))) # 앞에 int 라고 써줌
# print(type(float(10))) # float
# print(type(str(10))) # str
#
# #print(type( int('ABC'))) # 단 숫저로 되어있는것만 정수형 변경 불가능
# print(type( int('123')))

# 진수 변환
# print(int("1111", 2)) # 2진수를 10진수를표현
#
# # 8진수 표현시 앞에 0을 붙인다.
# # 16진수 표현시 0x 를 붙인다.
# print(int("ff",16)) # 16진수를 10진수로 표현
#
# print(oct(20)) # 8진수
# print(hex(20)) # 16진수
# print(bin(20)) # 2진수


# 출력시 콤마출력
# print("ABC","DEF") # 콤마사용
# print("ABC" + "DEF") # 콤마대신 + 사용, 문자를 붙일때
# #print("ABC" + 10) # 에러남
# print("ABC" + str(10)) # 형변환을 꼭 주어야함
# print("{0}{1}".format("ABC", "DEF")) # 포멧
# print("{1}{0}".format("ABC", "DEF")) # 출력시 순서를 바꿔줌
#
# print("{0:s}{1:s}".format("ABC", "DEF")) # 1번에 있는것을 문자로 찍겠다. s는 앞에다 숫자를 줄 수 있음
# print("{0:10s}{1:10s}".format("ABC", "DEF")) # s는 자리 잡기위해 사용
#
# print("{0:f}".format(1234.5678)) # 시각화 , f는 실수를 찍어라 기본적으로 6자리까지 찍음
# print("{0:.2f}".format(1234.5678)) # 소수점


# 연산자
# a=10
# print(a**2)
# print(5/2) # 자바에서는 2 파이썬은 2.5
# print(5.0/2)
# print(5//2)
# print(5.0//2) # 예는 2.5가 아닌 2.0이 나옴
#
# # and
# print(0 and 0) # 거짓 거짓
# print(0 and 1) # 거짓 참
# print(1 and 0) # 참 거짓
# print(1 and 1) # 참 참
#
# #or
# print(False or False) # 거짓 거짓
# print(False or True) # 거짓 참
# print(True or False) # 참 거짓
# print(True or True) # 참 참
#
#
# print("H" in "Hello") # Hello 안에 H가 있느냐
# print("H" not in "Hello") # Hello 안에 H가 포함이 아니냐
#
# a="Hello"
# b="Hello"
# print(a is b) # 주소비교
# print(a == b) # 내용비교
#
# a += "Python!"
# b += "Python!"
#
# print(a is b)
# print(a == b)

a=10
# print( a+= 10) # 연산하고 나온 값을 출력해라 해야함 이런식이면 에러남
a+=10; print( a )
a-=10; print( a )
a*=10; print( a )
a/=10; print( a )
a%=10; print( a )

# 쉬프트 대입연산자
a=20
a <<= 2; print(a)
a >>= 2; print(a)

# 비트논리 대입연산자
a = 10
a &= 10; print(a)
a |= 10; print(a)
a ^= 10; print(a)


