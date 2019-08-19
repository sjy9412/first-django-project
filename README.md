# First-django-project

## Django

* *Framework* vs library

*  동적으로 사용할 수 있도록 해줌



## MTV (Model Template View)

* 데이터를 관리 / 사용자가 보는 화면 / 중간 관리자



## 1. Django 시작하기

해당 project에서만 사용하는 라이브러리르 사용하기 위해 가상환경(venv 폴더)를 만들어줌

다양한 버전을 사용했을 때 충돌하지 않도록 하기 위해

* deactivate : 비활성화
* venv : 활성화

```bash
$ pip install django
```

* 현재 활용하고 있는 버전은 다음과 같다.
  * python 3.7.4
  * django 2.2.4

  ### 프로젝트 만드는 순서
  
  1. 폴더 만들기 (mkdir __)
  2. 가상환경 만들기 (python -m venv venv)
     1. `.gitignore`에 venv/ 추가 (git에 올릴경우)
  3. 가상환경 실행 (source venv/Scripts/activate)
  4. 원하는 django 버전 설치 (pip install django)
  5. 프로젝트 생성 (django-admin startproject __)
  6. app 생성 및 등록
  7. url 설정 (7 ~ 10 반복)
  8. view.py 설정
  9. templates 설정
  10. 서버 실행
  


### 0. 가상환경 실행 + .gitignore

> 가상환경을 사용하는 이유는 프로젝트마다 활용되는 라이브러리(pip)가 다르고, 동일한 라이브러리라도 버전이 다를 수 있다.
>
> 따라서, 프로젝트 하면서 라이브러리 삭제 혹은 변경을 하는 것이 아니라 각 프로젝트마다 독립된 가상환경을 부여하여 의존성을 없앤다.
>
> 항상 django 실행할 때마다 가상환경을 활성화 시키는 것을 습관화 하자!
>
> 추후에 DS(data science)/ML/DL -> anaconda를 활용하기도 한다.

가상환경은 python에서 기본으로 제공하고 있는 [`venv`](https://docs.python.org/ko/3/tutorial/venv.html)를 활용한다. (python 3.5+)

1. 가상환경 생성

   원하는 디렉토리에서 아래의 명령어를 입력한다.

   ```bash
   $ python -m venv __venv__
   ```

   * `__venv__` 여기에 가상환경 이름을 작성하는데, 보통 `venv`라고 설정
   * `__venv__` 폴더가 생성되는데, 구조는 다음과 같다.
     * `Lib` : 가상환경에 설치된 라이브러리 모음
     * `Scripts` : 가상환경 실행과 관련된 파일

2. 가상환경 실행

   ```bash
   $ ls
   venv/ ..
   $ source venv/Scripts/activate
   (venv)
   $ python -V
   python 3.7.4
   ```

   * 반드시 해당 명령어는 `venv`폴더가 있는 곳에서 실행시킨다.
   * **`bash shell`에서는 `activate` 파일을 실행해야 한다.**
     * `cmd` : `activate.bat`
     * `power shell` : `activate.ps1`

3. 가상환경 종료

   ```bash
   $ deactivate
   ```

4. `.gitignore` 등록

   ```bash
   venv/
   ```

   * 추가적으로 visual studio code를 활요하는 경우에는 `.vscode/`
   * python 환경에서는 `__pycache__/`
   * pycharm 환경에서는 `idea/`

   위 폴더들은 `.gitignore`에 등록하는 습관을 가지자! 잘 모르겠으면  [gitignore.io](gitignore.io)에서 찾기

### 1. Django 프로젝트 시작

```bash
$ pip install django
```

* 처음 시작할 때 장고를 설치

  * 참고

    ```bash
    $ pip freeze > requirements.txt
    ```

    * 사용하는 패키지를 저장하여 확인가능

    ```bash
    $ pip install -r requirments.txt
    ```

    * 다른 가상환경에서 requirments에 저장된 패키지들을 설치할 수 있음

```bash
$ mkdir __프로젝트 이름/폴더 이름__
$ cd __프로젝트 이름/폴더 이름__
```

```bash
$ django-admin startproject __프로젝트 이름__.
```

* 프로젝트 이름으로 구성된 폴더와 `manage.py`가 생성
  * `__init__.py` : 해당 폴더가 패키지로 인식될 수 있게 작성되는 파일
  * `settings.py` : **djago 설정과 관련된 파일**
  * `urls.py` : **url 관리**
  * `wsgi.py` : 배포시 사용 (web server gateway interface: 파이썬에서 사용되는 웹 서버 구성)
  * `manage.py` : **django 프로젝트와 관련된 커맨드라인(명령어) 유틸리티**



### 2. 서버 실행

```bash
$ python manage.py runserver
```

* `localhost:8000`으로 들어가서 로켓 확인!
* 서버가 잘 실행되었는지 확인하기



### 3. App 생성

```bash
$ python manage.py startapp __app이름__
```

* `app이름`인 폴더가 생성되며, 구성하고 있는 파일은 다음과 같다.

  * `admin.py` : 관리자 페이지 설정

  * `apps.py` : app의 정보 설정. 직접 수정하는 경우 별로 없음

  * `models.py` : **MTV-Model을 정의 하는 곳**

  * `tests.py` : 테스트 코드를 작성하는 곳

  * `views.py` : **MTV-View를 정의 하는 곳**

    * 사용자에게 요청이 왔을 때, 처리되는 함수

      ```python
      def index(request):
          return render(request, index.html)
      ```

      request를 반드시 해줘야 함!!

**app을 만들고 나서 반드시 `settings.py`에서 `INSTALLED_APPS`에 app을 등록한다**

```python
# first_django/settings.py
# ..
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    # ...
]
# ..
```



## 2. 작성 흐름

### 1. URL 정의

```python
# first_django/urls.py
from pages import views

urlpatterns = [
    path('', views.index),	# 마지막에 ,를 작성해 주는 것이 좋음
]
```

* `urls.py`는 우리의 웹 어플리케이션 경로들을 모두 관리한다.
* 요청이 들어오면 `urls.py`의 `urlpatterns`에 정의된 경로로 매핑한다.
* path(`경로`, `views에 정의된 함수`)



### 2. View 정의

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

* `view.py`는 MTV에서 View에 해당한다.
* 일종의 중간관리자로 Model, Template 등의 처리를 담당한다.



### 3. Template 정의

* 기본적으로 app을 생성하면, `templates` 폴더가 없으므로 직접 생성해야 한다.

```html
<!-- pages/templates/index.html -->
<h1>
    장고 안녕!
</h1>
```



### 4. 서버 실행 및 확인

```bash
$ python manage.py runserver
```

`localhost:8000`에서 확인 해보자!



# Form 태그 사용

```html
<form action="/signup_result/" method="POST">    
```
* action : 요청 보내는 곳

* method : 요청 보내는 방식

  * GET : DB에서 어떠한 값을 꺼내오거나 단순 요청하는 경우

    * URL에 querystring으로 요청이 보내짐
      * python에서 `request.GET`하면 {'data': '안녕하세요'} 형태로 저장(QueryDict)
    * ?username=tak&password=123

  * POST : DB의 어떠한 값을 추가하거나 삭제하는 경우

    * HTTP 요청의 body (url에 보이지 않음)

    * django에서 POST 요청으로 form을 보내는 경우 보안상의 이유로 항상 csrf_tokem을 넣어줘야함

      ```html
      {% csrf_token %}
      ```

      

# 정적 파일 관리

* 정적 파일(static file) : img, css, js ..

1. app으로 등록된 폴더 안에서 static폴더 생성

2. 폴더를 불러옴

	```html
	{% load static %}
	```
	
3. 사용하려는 파일을 불러옴

   ```html
   <link rel="stylesheet" href="{% static 'stylesheets/signup.css' %}">
   ```

   * {% 폴더명 '내부 폴더명/파일명' %}