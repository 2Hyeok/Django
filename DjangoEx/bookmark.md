
### 어플리케이션 생성

- cmd → python [manage.py](http://manage.py/) startapp bookmark
    
    ![image](https://user-images.githubusercontent.com/87698248/186077392-8ae7eaa1-12e6-4401-a043-b818dbc12816.png)
    
    ![image](https://user-images.githubusercontent.com/87698248/186077600-c8698db7-d3cc-474b-9703-bb524ed0a278.png)
    
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
    
    ![image](https://user-images.githubusercontent.com/87698248/186077618-592b278f-e1b0-4ec7-82d0-31e720ea40c2.png)
    


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
    
    ![image](https://user-images.githubusercontent.com/87698248/186077645-0f2d1fdb-05c5-4723-b7ae-b7c22dbcb1cd.png)
    
- cmd ->python [manage.py](http://manage.py/) makemigrations
    
    ![image](https://user-images.githubusercontent.com/87698248/186077663-abe9e0c5-ac3f-4151-950f-96586b71d927.png)
    
    ![image](https://user-images.githubusercontent.com/87698248/186077684-3d0d1340-b325-44a7-8313-b844dc15a729.png)
    
    아이디가 생성됨
    
    verbose는 보여주는 아이디
    
    직접 건드리면 안된다.
    
    - 다시 cmd → python [manage.py](http://manage.py/) migrate
        
        ![image](https://user-images.githubusercontent.com/87698248/186077707-3eeec487-fd2c-4d14-b60b-f1ce902745b5.png)
        
    
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
    
    ![image](https://user-images.githubusercontent.com/87698248/186077739-e3cf131a-b69e-4678-9b61-d7c92f588b9a.png)
    
    북마크 추가하기
    
    ![image](https://user-images.githubusercontent.com/87698248/186077751-3308dc50-8d82-4c70-9005-960a52d2dcd0.png)
    
    ![image](https://user-images.githubusercontent.com/87698248/186077773-4417979c-1e3e-486f-9fe3-ab5535be460b.png)
    

---
