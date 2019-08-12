import random
import datetime
from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')

    # 변수의 이름은 반드시 urls.py에서 지정해준 것과 같은 것으로 해줘야함
def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

def lotto(request):
    print(request)
    print(type(request))
    print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1, 46), 6))
    # 변수를 딕셔너리에 담아서(보통 context라고 부름)
    context = {'numbers': numbers}
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language(DTL)!
    return render(request, 'lotto.html', context)

def dinner(request):
    menus = ['롯데리아', '편도', '맘스터치', '떡볶이', '노은각', '피자', '치킨']
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'menus': menus,
        'users': [],
        'sentence': 'Life is short, You need Python + django!',
        'datetime_now': datetime.datetime.now(),
        'google_link': 'https://www.google.com',
        'django_link': 'https://docs.djangoproject.com/en/2.2/ref/templates/language/'
        }
    return render(request, 'dinner.html', context)

    # 기본적으로 template에서는 연산이 불가능함(라이브러리를 설치하면 가능)
    # 따라서 연산은 view에서 해주는 것이 좋음
def cube(request, number):
    context = {'number': number, 'cube_number': number**3, 'numbers': [1,2,3], 'students': {'3': 3, '5': 6}}
    return render(request, 'cube.html', context)

def about(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'about.html', context)