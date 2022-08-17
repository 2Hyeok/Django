# 클래스
# 캡슐화 상속 다형성

# private
__a = 10 # _ _ 두개가 private라는 뜻
def getA():
    return __a
print(getA())

# 단 __ 쓴다고해서 다 private가 아님 클래스가 있어야함
# 클래스 생성
class P: # 클래스 첫글자는 대문자
    __a = 10    # private
    b = 20
    
    # __a 를 꺼내오기 위해선 대신 접근하는것을 만들어주어야함
    def getA(self): # self를 다 명시해 주어야함
        return self.__a
    def getB(self):
        return self.b
    def setA(self, a):
        self.__a = a
p = P()
# print(p.__a) # private이기 때문에 접근 불가
print(p.b)
print(p.getA()) # 출력가능
print(p._P__a) # _클래스이름__객체이름?, private 멤버 접근 방법을 제겅, 완벽한 캡슐화는 불가능

# set 메소드
# p.__a = 100 # 안됨
p.setA(100)
print(p.getA())
print()

# 캡슐화
class Person :
    __name = ""
    __age = 0
    __height = 0.0
    
    # setter, getter 만들어줌
    def setName(self, name):
        # 추가
        if len(name) > 10 or name=="":
            print("이름을 바르게 입력하세요")
        else :
            self.__name = name
    def setAge(self, age):
        if age < 1 or age > 140 :
            print("나이를 바르게 입려하세요")
        else :
            self.__age = age
    def setHeight(self, height):
        if height < 40 or height > 200 :
            print("키를 바르게 입력하세요")
        else :
            self.__height = height
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getHeight(self):
        return self.__height
    
kim = Person()
# 잘못 설계한 데이터
# 이렇게 큰 데이터 가 들어가면 안됨
# 이런 데이터를 막지를 못함
kim.setName("홍길동홍길동홍길동홍길동홍길동홍길동홍길동홍길동홍길동")
kim.setAge(150)
kim.setHeight(300)
print("이름 : ",kim.getName())
print("나이 : ",kim.getAge())
print("키 : ",kim.getHeight())

lee = Person()
lee.setName("이순신")
lee.setAge(30)
lee.setHeight(180)
print("이름 : ",lee.getName())
print("나이 : ",lee.getAge())
print("키 : ",lee.getHeight())


#         생성자 - 객체 초기화   /  소멸자 - 메모리 정리
# c++     Person()         /     ~Person()
# Java    Person()         /      없음
# Python  __init__         /     __del__


# 변수를 따로 안만들어도됨
class User :
    def __init__(self, name="", age=0, tel=""):
        print("생성자") # 객체마다 생성자 호출
        self.name = name
        self.age = age
        self.tel = tel
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getTel(self):
        return self.tel
    # def __del__(self): # c에선 포인터가 충돌이나면 에러가 나기에 만들어줌 하지만 안만들어줘도됨 
    #     print("소멸자") # 객체마다 소멸자 호출
        
kim = User()
lee = User("이순신")
hong = User(age=20, tel="1111-1111")
# 스텍영역이라 생성자 -> 소멸자 -> 생성자 -> 소멸자 순으로 안나옴
# 이름만 스텍이 아니라 원래 스텍의 특징을 가지고있음
# 스텍의 특징 스텍은 쌓는다는 의미 넣을때 ABC 꺼낼때는 CBA 나중에 잡은애가 먼저 사라짐

print("이름 : ",hong.getName()) # 이름을 넣은게 없기에 출력안함
print("나이 : ",hong.getAge())
print("전화번호 : ",hong.getTel())

# static
# 쓸수 있는데 특징을 다 쓰지 못함
# 모든 겍체가 공유하는것이 static
# 메모리 영역 중에 static 영역이 할당됨
# 메모리는 하나만 할당됨
# 먼저 할당 됨
# 파이썬은 static 을 명시할 필요가 없다.

print()
class Member :
    name = "홍길동"       # 맴버변수, 믈래스변수, static 변수
    count = 0           # 직접 변수를 잡아주면 스테틱이다.
    def __init__(self,age = 0, cnt=0): # 지역변수 
        self.age = age
        self.cnt = cnt
        Member.count += 1
        self.cnt += 1
        
    def getCnt(self):
        return self.cnt
    def getCount(self):
        return Member.count # 스테틱이라 하더라도, self 쓰면 누적이 안됨, 클레스명으로 잡아 주어야 한다.
    
print(Member.name) # 객체생성 없이도 클래스이름.맴버변수, 스테틱이기 때문
# print(Member.age) # 지역변수 이기때문에 실행 불가

Member.name = "이순신" # 한번에 다 바뀌게됨 홍길동 -> 이순신

lee = Member()
print(lee.name) # 이렇게 해도 상관없음, 단 메모리가 하나밖에 잡히지 않아서 모두 홍길동(초기값)으로 나옴 -> 이순신
print(lee.getCount()) # 1씩 증가
print(lee.getCnt()) # 1만 출력

hong = Member()
print(hong.name)
print(hong.getCount())
print(hong.getCnt())

park = Member()
print(park.name)
print(park.getCount())
print(park.getCnt())

# self를 붙이면 지역변수
# 클래스명을 붙이면 statuc 변수
# static 메소드
class Customer :
    name = "홍길동" # 스테틱 변수
    def setName(self, name): # 지역변수
        self.name = name
    def getName(self):
        return self.name
    @staticmethod # 이런식으로 붙여 사용해도 사용가능 -> 스테틱 메소드를 사용하겠다는 뜻
    def dispName(): # static 함수, 스테틱은 공유하는 메소드이기에 self를 안써줌, 스테틱 메소드로 만들어주어야 애러가 안남
        return Customer.name 
    #dispName = staticmethod(dispName)
    
kim = Customer()
kim.setName("김유신") # 지역변수에 넣음
print(kim.getName())

# 메소드명 접근할때도. 클레스명.멤버로 접근
print(Customer.dispName())



# 클래스 메소드
# 클래스를 두개 잡음, 상속
print()
class Car :
    cc = "2000cc"
    @staticmethod # 스테틱 메소드
    def getStatic():
        return Car()
    
    @classmethod # 매개변수 하나를 줘야함, 클레스 메소드
    def getClass(cls): # cls 는 해당 클래스를 매개변수로 전달함
        return cls() # cls라는 객체 생성

    def getCc(self):
        return self.cc
    

class Truck(Car): # 상속을 이렇게줌, 상속을 받으면 부모꺼는 자신것
    cc = "3000cc"
a = Car.getStatic() # 객체를 받아만 놓음
b = Car.getClass()
print(a.getCc())    # 2000cc, Car클래스로 만든 객체
print(b.getCc())    # 2000cc, Car클래스로 만든 객체

c = Truck.getStatic()
d = Truck.getClass()
print(c.getCc())    # 2000cc, 강제로 Car클래스로 만든 객체
print(d.getCc())    # 3000cc, Truck 에서 만들어준것을 넘겼기에 3000 출력

# 클래스메소드는 클래스를 넘겨받아 객체를 만들고, Car클래스면 Car이고 Truck 클래스는 자식클레스에 3000이라고 만들었기에 3000이 넘어감



#---------------------------------------------------------------------------------------------------------
print()
# 상속
# 코드 재활용
# 부모 것은 내것
# class Animal() :
#     def __init__(self, name="") :
#         self.name = name
#         print("Animal 생성자") # 생성자 호출 순서 확인용
#     def getName(self):
#         return self.name
#
# class Cat (Animal):
# #    None # 생성자가 없어도 부모쪽 자동으로 넘어가 생성자를 먼저 실행함
#     def __init__(self, name=""): # 이름을 얘가 처리해도 되지만 부모쪽에서 처리해서 던질 수 있음
#         Animal.__init__(self, name) # 부모쪽에서 알아서 처리할것
#         print("Cat 생성자") # 생성자 호출 순서 확인용
#
# class Dog (Animal):
# #    None # 생성자가 없어도 부모쪽 자동으로 넘어가 생성자를 먼저 실행함
#     def __init__(self,name=""):
#         Animal.__init__(self, name) # 부모쪽에서 처리해라
#         print("Dog 생성자") # 생성자 호출 순서 확인용
                                 
# dog = Dog("양규호")
# print(dog.getName())
# cat = Cat("유제욱")
# print(cat.getName())





# 다중 상속
# c++            구현 O, 사용 X
# Java           구현 X, 사용 O(인터페이스 이용) -> final(값을 바꾸지마라, 고정된값에 사용), abstract
# Python         구현 O, 사용 O

class Animal :
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
class Pet :
    def __init__(self, kind):
        self.kind = kind
    def getKind(self):
        return self.kind
class Dog (Animal, Pet):
    def __init__(self, name, kind, color): # 데이터를 다 받아서 부모쪽으로 넘기라 해야함, 여기서 값을 넘기기에 만들어줌
        Animal.__init__(self, name) # Animal에 name을 넘겨줌
        Pet.__init__(self, kind) # Pet에 kind을 넘겨줌
        self.color = color
    def getColor(self):
        return self.color
    
    def getName(self):          # 재정의, 오버로드
        return "이름 : " + self.name
    def getKind(self):
        return "품종 : " + self.kind
    
dog = Dog("양규호", "시고르자브종", "빨간색")
print(dog.getName())
print(dog.getKind())
print(dog.getColor())



#------------------------------------------------------------------------------------------------------------
# 다형성
class Bread :
    def __init__(self, name=""):
        self.name = name
    def getName(self):
        return "Bread : " + self.name
    
    @classmethod        # 클래스 메소드를 추가해줌
    def getClass(cls, msg):
        return cls(msg)
    
class Toast(Bread):
    def getName(self):
        return "Toast : " + self.name
class Cake(Bread):
    def getName(self):
        return "Cake : " + self.name
class RedBean(Bread):
    def getName(self):
        return "RedBean : " + self.name

# 성립이 될라면 이런식으로 가야함
# Java 방식
# Bread bread = new Toast(); bread.getName()
# Bread bread = new Cake(); bread.getName()
# Bread bread = new RedBean(); bread.getName()

# Python방식
toast = Toast("햄치즈토스트")
print(toast.getName())

cake = Cake("치즈케이크")
print(cake.getName())

redbean = RedBean("팥빵")
print(redbean.getName())
print()

# 클래스 메소드 추가후
bread = Bread()
toast = Toast.getClass("콘치즈 토스트") # static메소드로 사용가능
print(toast.getName())

cake = Cake.getClass("생크림 케이크")
print(cake.getName())

redbean = RedBean.getClass("단팥빵")
print(redbean.getName())



# @property / property()
# private 인 경우는 접근이 불가능함
class Gamer():
    __name = ""
    __age = 0
    # getter setter 생성
    @property
    def setName(self, name):
        self.__name = name
        
    @property
    def setAge(self, age):
        self.__age = age
        
    @property
    def getName(self):
        return self.__name
    
    @property
    def getAge(self):
        return self.__age
    
    # # setter getter 쓰기 싫다!!
    # name = property(getName, setName)
    # age = property(getAge, setAge)
    
    
    
gamer = Gamer()
# gamer.setName("양규호")
# gamer.setAge(28)
# print(gamer.getName())
# print(gamer.getAge())

# print(gamer.__name)
gamer.name = "이순신"
gamer.age = 30
print(gamer.name)
print(gamer.age)
