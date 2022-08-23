---

### 어플리케이션 생성

- cmd → python [manage.py](http://manage.py/) startapp bookmark
    
   ![image](https://user-images.githubusercontent.com/87698248/186077392-8ae7eaa1-12e6-4401-a043-b818dbc12816.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/22205636-3bb6-4c09-b6fa-fe953ca046da/Untitled.png)
    
    생성 완료
    

디비부터 생성을 해주어야함

models → 모델

views → 흐름제어

프로젝트 이름과 같은 패키지는 전체세팅

새로만든 패키지는 해당 어플리케이션에 대한 세팅

전체 새팅을 걸어줌

- DjangoEx → [setting.py](http://setting.py) 기본 세팅값
    
    ```python
    # Application definition
    # 현재 설치되어있는 앱이 무엇인지
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'bookmark', # 새로 추가해줌
    ]
    
    ----------------------
    
    LANGUAGE_CODE = 'ko-kr' # 한국어
    
    TIME_ZONE = 'Asia/Seoul' # 한국시간
    
    USE_I18N = True
    
    USE_TZ = True
    
    ------------------------
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```
    

새팅이 바뀌었기에 서버를 재시작 해주어야함

- 한국어 변경 확인
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/83a2e8c3-3cb8-441a-8479-2888532fd0a8/Untitled.png)
    

---

### 디비생성

- models.py
    
    클래스 하나가 테이블 하나가됨
    
    ORM - 객체와 관계형 데이터 베이스를 연결해 주는역할
    
    데이터는 두개만 저장할예정
    
    ```python
    from django.db import models
    
    # Create your models here.
    
    class Bookmark(models.Model): # 모델을 상속 받으면됨
        title = models.CharField(max_length=100, blank=True, null=True)
        url = models.URLField('url', unique=True) # 유니크 를 줌
        def __str__(self):
            return self.title
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e9d59048-a1ec-40a5-9b4f-0b59bd177358/Untitled.png)
    
- cmd ->python [manage.py](http://manage.py/) makemigrations
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c9fbcc8-006e-41d2-a95c-33909137d6ef/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd6ab619-a874-4f32-bf0a-6d36b1f93e38/Untitled.png)
    
    아이디가 생성됨
    
    verbose는 보여주는 아이디
    
    직접 건드리면 안된다.
    
    - 다시 cmd → python [manage.py](http://manage.py/) migrate
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5a764d7-63c2-41a3-9842-743536e1eaab/Untitled.png)
        
    
    변경사항이 있기에 이런식으로 실행해 주어야 저장이됨
    
- 어드민에 보여라 하는 세팅을 해주어야함
    
    admin.py
    
    ```python
    from django.contrib import admin
    
    # Register your models here.
    from bookmark.models import Bookmark # 북마크의 모델스안에 있는 북마크라는 클래스를 임포트 
    
    class BookmarkAdmin(admin.ModelAdmin): # 모델 어드민을 상속
        # 보여줄 리스트를만듬
        list_display=("title", "url") # 튜플로 잡아줌
    
    # 클래스는 끝
    # 이제 밖에다 주어야한다
    admin.site.register( Bookmark, BookmarkAdmin) # 등록해라, 북마크와 북마크 어드민을
    ```
    
    페이지 다시 시작
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/24af7ed0-fa7d-4f83-9c5a-a1b1540abde7/Untitled.png)
    
    북마크 추가하기
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/003b80b4-4a6e-461f-98ce-b2618b7aa1cf/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63cb9fdd-9dfc-49e3-8fdc-eb757b8e33c1/Untitled.png)
    

---
