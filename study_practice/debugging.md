## 디버깅
노란색 오류 이름은 없습니다. 단순히 코드상에서 빠지거나 잘못 표기되는걸로 나올 것 같은거 위주로 정리

표시된 시험 팁!!
관통 프로젝트를 직접 작성하면서 복습하는 것을 추천드립니다.
Django ORM(Model.objects.filter 등) 사용법뿐만 아니라, 기본적인 SQL 구문(SELECT, JOIN, GROUP BY, ORDER BY 등) 작성 연습도 함께 해보면 도움이 됩니다.
같이 주어지는 샘플 문제도 반드시 풀어보면서 시험 유형 확인을 미리해주세요.

아래에는 장고 ORM, SQL 구문 등에 대해 다루지 않습니다. 진짜 오류 낼 것 같은 것들만 적혀 있어요
# 프로젝트
## settings
프로젝트 생성 시 생기는 파일   
1. 앱을 생성하면 INSTALLED_APPS 에 앱 이름을 추가해야 한다. 콤마 입력에 주의
2. 'DIRS': [BASE_DIR / 'templates'] - base.html을 프로젝트 생성과 같은 위치에 하였을 경우 작성. 수업시간에서 해당 위치에 생성하는 것으로 배웠으므로 작성하기
3. STATIC_URL = 'static/' - 브라우저에서 접근할 URL 주소 변수명부터 작성해야 한다.   
STATICFILES_DIRS = [
    BASE_DIR / 'static'
] - 정적파일 css, js, 이미지 등을 어디서 찾을지 알려주는 설정. 리스트 정의부터 작성해야 한다. 
4. AUTH_USER_MODEL = 'accounts.User' - 쟝고의 기본 User 대신 직접 만든 User를 사용하겠다는 뜻. models 에서 추가로 다룰 예정

## urls
1. include 함수를 import에 추가
2. include는 특정 앱의 urls로 연결하는 것 include를 대부분 사용하여 구분 하므로 include가 잘 사용되었는지 확인    
ex) path('accounts/', include('accounts.urls')) - accounts란 이름의 앱에 있는 urls로 연결 accounts의 url은 전부 'accounts/'로 시작한다.  
3. + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) - 뭔지모름 이런 것도 추가로 적는다.

# 앱
## models
1. from django.contrib.auth.models import AbstractUser - 유저 모델 선언시 필요(수기 입력 대체) 이걸 사용시 settings의 4번 입력 필요 클래스 선언은 2번
2. class User(AbstractUser): pass - 클래스 선언하는법이다. 괄호안 대문자 유의
3. models.ManyToManyField - 다대다 선언 
4. 
## forms 
1. from django.contrib.auth import get_user_model - 위 2번 선언을 forms로 가져올 땐 get_user_model 을 사용해야 한다. 
2. forms에서 만들어진 모델을 가져올 시 class 이름(방식): class Meta 구조가 필수다. 이 Meta 아래에 
3. model = get_user_model() 을 써야한다.
4. 위 처럼 Meta 사용시 model = 내가 선언한 모델명 fields = (사용자가 입력할 이름들 작성) 이 외에도 exclude로 제외, include로 포함 시킬 수 있다. 
## urls
1. app_name = 'accounts' - 앱 네임을 선언해야 한다. 추후에 views 와 html에 일치하게 작성해야 한다.(아마)
2. from . import views - 이걸 통해 views에 있는 함수를 들고와야한다.(아마 )
3. path('delete/', views.delete, name='delete') 셋 모두 일치하게 적는 것이 좋다. 이는 views의 함수명과도 일치해야 한다. 
4.  ```py
5.  path("<int:user_pk>/subscribe/", views.subscribe, name="subscribe")
``` - views 함수에서 받아야 할 인자가 추가로 있을경우 위처럼 ```<int:user_pk>``` 로 써야한다 혹은 ```<str:name>```도 있다.
## views
1. if request.method == 'POST': - POST인지 GET인지 바꿀 수 있을듯 
2. return redirect('todos:index') - redirect는 무조건 앱이름:함수명 으로 작성되어야 함 
3. def login(request): - 혹시나 request 빼먹은게 있지 않을까?
4. return render(request, 'accounts/login.html', context) - render의 경우 request와 이동할 html 파일 필수 (html파일의 주소는 템플릿 아래로부터 적으면 된다.) context는 있어도 되고 없어도 된다. 
5. context = {
        'form구분용문구': form
    } - context를 줄 경우 html에서는 'form구분용문구'로 적혀 있어야 한다. 
6. DB 변경시 if form.is_valid():
            user = form.save() - 저장했는지 확인  
7. def change_password(request, user_pk): - 인자를 이렇게 두개 받을 시 urls의 주소 부분에 ```<int:user_pk>```과 이름이 같은지, html에서 pk값을 넘겨주는지 확인  
## html
1. 
```html
<form action="{% url "todos:recommend" todo.pk %}" method="POST">
``` 
- forms 사용시 url 있는지 확인 뒷부분의 todos:recommend의 구조는 todos -> urls 에서 말한 app_name과 일치 해당 위치 app의 views 함수에 recommend가 있어야 한다. 해당 recommend 함수의 인자가 두개 이상일 경우(request 제외 더 필요한지) 필요한 매개변수 작성해주기 여기선 todo.pk 이다. 또한 POST인지 GET인지 확인 
2. {% csrf_token %} - POST 요청이라면 필수 꼭 확인하기  
## 파일 저장 위치
솔직히 이걸로는 시험에 안 나올듯 한데 혹시 모르니까   
templates, static의 폴더 위치, 이름 오타 없는지 확인하기   


## 부족한 점 
ORM, 일대다, 다대다, Auth 등에 대한 설명이 꽤 부족함. 일대다의 on_delete나 역참조, 비밀번호 변경 등에 쓰이는 from django.contrib.auth import logout as auth_logout 와 같은 것들은 추가 학습 필요 이 외에도 @로 쓰는 데코레이터(로그인 해야만 좋아요 가능 같은 것) 추가학습 하면 좋을 듯 합니다.  

위에서 언급한 것 이외에도 말 안한 것 많을듯 하니까 강사님 코드나 관통프로젝트 코드 보기 절대로 이거에 의존하면 안됩니다!!