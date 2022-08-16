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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d68291a-b3c3-4a00-a2ee-327a318a8d18/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f43c04a-3c9e-409f-b083-eb5a604541eb/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aa0e7ee5-cce7-467e-8e1c-b0b729ca3dc7/Untitled.png)

Add Python 3.8 to PATH 꼭체크 해줄것

안해주면 패스를 수동으로 설치 해야함

install 클릭

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/165f9ced-4d21-4d7b-983c-c3ed32a7e502/Untitled.png)

설치 완료후 close

파이썬 경로 확인

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/12a216b8-967f-43e7-9f38-7b0af1e5fe2f/Untitled.png)

cmd → ptyhon - -version → 파이썬 설치 확인

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5c1107db-81f0-42be-a745-417c6b746812/Untitled.png)

cmd 창에서 python 코딩 가능

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2213386c-92b1-4034-a22a-eb58bdd217bd/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/450378ce-0298-452e-8eb9-908a642aa801/Untitled.png)

exit()로 나가기

---

### 추가설치

PyDev 설치

[https://sourceforge.net/projects/pydev/?source=typ_redirect](https://sourceforge.net/projects/pydev/?source=typ_redirect)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f1940f3-f5f7-4473-b0dc-ccfc5ab4a085/Untitled.png)

pydev 클릭

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/815f0a5c-3771-4eea-a9ea-30bd028da43e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b2276b82-7c36-4cb0-bf49-36f5f471654d/Untitled.png)

이클립스도 다시 설치 해주어야함 → 버젼 문제로 적용이 안됨

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e19dd8b3-bf3b-4c3e-8a07-676eaed61a0a/Untitled.png)

pydev도 9.3 으로 풀어줌

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5b6725b4-197c-4dd7-bdaf-a4ec069b3475/Untitled.png)

압축을 푼 후에 덮어쓰기를 해줌

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7835bff6-5d31-4f18-be95-bb5c015a16ae/Untitled.png)

파이썬 적용 완료

- 기존의 파일은 사라지는것이 아닌 파일이 추가가 되는것임

windows → preferences → PyDev  → interpreters → Python interpreters

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51895484-a5b2-405f-989c-b1fbf4db356d/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/496bdfe9-6a7a-4821-a2f6-bd2cde068957/Untitled.png)

파이썬 패스의 맨 위의 패스를 쓸것이다 라는 뜻

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f676a36b-dfea-4265-85b9-0889797af3c5/Untitled.png)

이후 프로젝트 생성후 실행하면 잘 작동함

---

### 프로젝트 생성

file → other → pydev → ptdev project

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/82edff19-f86a-4460-8d05-f1296830f4bc/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/368c81c4-c5e0-46b0-b50d-f893ebed73f3/Untitled.png)

이상태로 생성

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/59abd7ea-480a-44da-84de-b180e8bcd8a4/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0c4eea37-7c20-4b3b-a9f6-bef8283471d2/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df782de7-d3b2-4549-9b3a-286c888caae7/Untitled.png)

simple → 우클릭 → PyDev Module

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd1afc11-94e2-4cc5-9f71-e0d888b03770/Untitled.png)

empty

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/493b513f-7a9b-4c72-8e01-2f3a35c88025/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0e88cca-76c8-47d9-97ec-1b9c63c4fba7/Untitled.png)

한번은 이렇게 실행 해주어야함

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/80b57fb2-9257-4fb3-8f25-a932973b4bb8/Untitled.png)

but 한줄로 코딩할 때에만 세미콜론을 찍어주어야함

```python
a=10; print(a)
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f14d04fc-6bda-4dbd-b281-800c16604664/Untitled.png)

이상없이 잘 나옴

들여쓰기도 주의 해야함

탭을 누르게 되면 하위 영역이기에 잘 해주어야함

영역표시가 없어 들여쓰기 잘못하면 큰일남!

[Python 기본](https://www.notion.so/Python-98f6e6bf3ff54b55b29488e4b4abc370)

[Python 자료형](https://www.notion.so/Python-16168a768e8149ec91f11cc2bfa574b3)

[Python 열거형 나열형](https://www.notion.so/Python-51b2c0a97c6d4884a52da2eb3d5dc373)

[Python Mappings](https://www.notion.so/Python-Mappings-ae3c3a751cf7435a8507c98941a54bab)

[Python 함수, 클래스, 모듈](https://www.notion.so/Python-2586ca9809494471a0912f4633fe7582)
