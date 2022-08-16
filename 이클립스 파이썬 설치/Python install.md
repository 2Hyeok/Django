# Python

---

### 이클립스용 파이썬 설치

[https://www.python.org/downloads/release/python-3810/](https://www.python.org/downloads/release/python-3810/)

텐서플로우 → 딥러닝을 위한 라이브러리    파이썬 3.8에만 적용

3.8버젼 설치

- 이전에 파이썬을 설치 했다면 미리 지우고 설치를 진행
- 버전이 여러개가있으면 패스를 계속 바꿔야함
- pip인스톨시 계속 바꿔주어야함

download → windows

![image](https://user-images.githubusercontent.com/87698248/184868503-1a646795-0f6f-497d-8101-04a2fce05ad9.png)

![image](https://user-images.githubusercontent.com/87698248/184868546-d7650a25-0087-4412-a7f7-440781797cbf.png)

![image](https://user-images.githubusercontent.com/87698248/184868649-fcdfb667-fcac-437a-bdae-f32a8cc96309.png)

Add Python 3.8 to PATH 꼭체크 해줄것

안해주면 패스를 수동으로 설치 해야함

install 클릭

![image](https://user-images.githubusercontent.com/87698248/184868698-52fb9407-1aa3-48ab-b43f-05f64d319433.png)

설치 완료후 close

파이썬 경로 확인

![image](https://user-images.githubusercontent.com/87698248/184868730-b887e196-8af9-4451-adde-32b88f2f095a.png)

cmd → ptyhon - -version → 파이썬 설치 확인

![image](https://user-images.githubusercontent.com/87698248/184868763-fa649f5b-03d3-426d-a0f8-2b5f9a49d255.png)

cmd 창에서 python 코딩 가능

![image](https://user-images.githubusercontent.com/87698248/184868798-0031a6be-a275-48b0-b32b-90497b9cc6b1.png)

![image](https://user-images.githubusercontent.com/87698248/184868822-add3aa63-745d-46e8-86c9-d417c9252d29.png)

exit()로 나가기

---

### 추가설치

PyDev 설치

[https://sourceforge.net/projects/pydev/?source=typ_redirect](https://sourceforge.net/projects/pydev/?source=typ_redirect)

![image](https://user-images.githubusercontent.com/87698248/184868917-6c0b58d6-6f29-4aee-8f1d-eb3c66223069.png)

pydev 클릭

![image](https://user-images.githubusercontent.com/87698248/184868957-011fc8a8-d801-4d62-bf87-8dee8f9fcc93.png)

![image](https://user-images.githubusercontent.com/87698248/184868983-ead125d2-86c5-4fea-b751-c7ec0d7d1555.png)

이클립스도 다시 설치 해주어야함 → 버젼 문제로 적용이 안됨

![image](https://user-images.githubusercontent.com/87698248/184869563-1aa17977-a630-478d-b44f-c892402d04f6.png)

pydev도 9.3 으로 풀어줌

![image](https://user-images.githubusercontent.com/87698248/184869632-2b9c5f7e-745d-43ee-ac03-b013e51b85ab.png)

압축을 푼 후에 덮어쓰기를 해줌

![image](https://user-images.githubusercontent.com/87698248/184869618-00afb580-6bcf-4b18-9f92-6f93e51c141a.png)

파이썬 적용 완료

- 기존의 파일은 사라지는것이 아닌 파일이 추가가 되는것임

windows → preferences → PyDev  → interpreters → Python interpreters

![image](https://user-images.githubusercontent.com/87698248/184869681-4b951031-a7a5-4b3c-9c3e-899022b2fbc8.png)

![image](https://user-images.githubusercontent.com/87698248/184869710-c2bf0113-0ffa-4365-8c9d-30152ce88808.png)

파이썬 패스의 맨 위의 패스를 쓸것이다 라는 뜻

![image](https://user-images.githubusercontent.com/87698248/184869734-9cc03a19-e8a2-4304-a73e-1e2bfa056e0b.png)

이후 프로젝트 생성후 실행하면 잘 작동함

---

### 프로젝트 생성

file → other → pydev → ptdev project

![image](https://user-images.githubusercontent.com/87698248/184869760-3782396c-9e47-4e29-b5fa-c9482c15eed1.png)

![image](https://user-images.githubusercontent.com/87698248/184869784-126c5d13-92f1-42d4-ad9f-738c50888ed1.png)

이상태로 생성

![image](https://user-images.githubusercontent.com/87698248/184869811-d473bff8-4c33-4dc9-bde2-1d9fb8c49606.png)

기존프로젝트와 연결 할 것이냐 라는 뜻

연결 안할것 이기에 그냥 finish 해준다.

---

파일 하나를 모듈 이라고 부름

확장자는 .py

한 파일안에 다 들어감

파이썬은 모듈지향

파일 하나가 부품이됨

### 프로젝트 생성

PythonEx → 우클릭 → PyDev Package

![image](https://user-images.githubusercontent.com/87698248/184869859-dd60d8dd-7d96-4a0d-9d83-0bef0129dba3.png)

![image](https://user-images.githubusercontent.com/87698248/184869886-21d99d93-bf2d-4342-bc39-d26b9d829f69.png)

simple → 우클릭 → PyDev Module

![image](https://user-images.githubusercontent.com/87698248/184869904-0de11128-bfff-4692-b003-8bc36db29cec.png)

empty

![image](https://user-images.githubusercontent.com/87698248/184869925-bdb98892-49cb-4191-a910-1b32e73758be.png)

- 클래스 이름은 첫 글자는 대문자로 만들어야한다!!
- 이넡프리터 언어이기에 특징이 다른것이 있음
    - 컴파일 링크언어는 c 계열 이기에 무조건 코딩을 다 하고 전체를 컴파일 해야함 하지만
    - 파이썬은 한줄씩 컴파일을함 한줄을 코딩후 컴파일하면 에러를 확인함
        - 에러가 있어도 실행을 하는데 에러가 있는 부분에서 멈춤
        - 메모리할당부터 실행할때 결정을함
        - 미리 방의 크기를 잡아 주어야함 ex) int a = 10 → a = 10
        - 하지만 파이썬은 메모리의 크기를 잡아줄 필요가 없음
        - 데이터는 따지기는 따짐 자바처럼 세세하게 따지지는 않음
        - 정수, 실수, 숫자, 문자 만 따짐
        

### 실행 시작

```python
a=10
print(a)
```

ctrl + f11

![image](https://user-images.githubusercontent.com/87698248/184869969-01d5ad3f-e1d9-410c-9038-735edce25a1d.png)

한번은 이렇게 실행 해주어야함

![image](https://user-images.githubusercontent.com/87698248/184869988-b28d8aa3-9cf3-482b-80be-d40bee64d6ba.png)

but 한줄로 코딩할 때에만 세미콜론을 찍어주어야함

```python
a=10; print(a)
```

![image](https://user-images.githubusercontent.com/87698248/184870018-c8355df0-e6f5-4831-9b78-1ba5d5ab7289.png)

이상없이 잘 나옴

들여쓰기도 주의 해야함

탭을 누르게 되면 하위 영역이기에 잘 해주어야함

영역표시가 없어 들여쓰기 잘못하면 큰일남!
